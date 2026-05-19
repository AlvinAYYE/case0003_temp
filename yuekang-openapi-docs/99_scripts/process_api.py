import json
import csv
import os
from pathlib import Path
from collections import defaultdict

file_path = str(Path(__file__).resolve().parents[1] / '00_source_docs' / 'default_OpenAPI.json')
output_dir = str(Path(__file__).resolve().parents[1] / '05_gemini_validation')

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

openapi_version = data.get('openapi', data.get('swagger', ''))
info = data.get('info', {})
title = info.get('title', 'Unknown Title')
version = info.get('version', 'Unknown Version')
description = info.get('description', '')

# Security
security_schemes = data.get('components', {}).get('securitySchemes', {})
if not security_schemes:
    security_schemes = data.get('securityDefinitions', {})
security_methods = list(security_schemes.keys())

endpoints = []
subscription_events = []
tag_counts = defaultdict(int)
methods_used = set()
total_paths = len(data.get('paths', {}))
operations_count = 0

for path, methods in data.get('paths', {}).items():
    if not isinstance(methods, dict): continue
    for method, op in methods.items():
        if method.lower() not in ['get', 'post', 'put', 'delete', 'patch', 'options', 'head']:
            continue
        operations_count += 1
        methods_used.add(method.upper())
        
        tags = op.get('tags', [])
        summary = op.get('summary', '')
        operation_id = op.get('operationId', '')
        tags_str = ', '.join(tags)
        
        endpoint = {
            'method': method.upper(),
            'path': path,
            'tags': tags_str,
            'summary': summary.replace('\n', ' '),
            'operationId': operation_id
        }
        endpoints.append(endpoint)
        
        for tag in tags:
            tag_counts[tag] += 1
            
        if any("10. 业务事件订阅" in t for t in tags):
            subscription_events.append(endpoint)

schemas = data.get('components', {}).get('schemas', {})
schemas_count = len(schemas)
if not schemas:
    schemas = data.get('definitions', {})
    schemas_count = len(schemas)

# 1. endpoints.csv
with open(os.path.join(output_dir, 'endpoints.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['method', 'path', 'tags', 'summary', 'operationId'])
    writer.writeheader()
    for ep in endpoints:
        writer.writerow(ep)

# 2. subscription-events.csv
with open(os.path.join(output_dir, 'subscription-events.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['method', 'path', 'tags', 'summary', 'operationId'])
    writer.writeheader()
    for ep in subscription_events:
        writer.writerow(ep)

# 3. api-report.md
md_lines = []
md_lines.append(f"# API 總覽報告\n")
md_lines.append(f"## 總覽 (Overview)")
md_lines.append(f"- **OpenAPI Version**: {openapi_version}")
md_lines.append(f"- **Title**: {title}")
md_lines.append(f"- **Version**: {version}")
md_lines.append(f"- **Description**: {description}\n")

md_lines.append(f"## 認證 (Authentication) & 安全 (Security)")
if security_methods:
    for method in security_methods:
        md_lines.append(f"- {method}")
else:
    md_lines.append("- 無特別指定安全機制")
md_lines.append("")

md_lines.append(f"## 模組統計 (Module Statistics)")
for tag, count in tag_counts.items():
    md_lines.append(f"- {tag}: {count} 個端點")
md_lines.append("")

md_lines.append(f"## 訂閱事件接口 (Subscription Event Endpoints)")
for ep in subscription_events:
    md_lines.append(f"- **{ep['method']}** `{ep['path']}`: {ep['summary']}")
md_lines.append("")

md_lines.append(f"## 完整端點索引 (Full Endpoint Index)")
for ep in endpoints:
    md_lines.append(f"- **{ep['method']}** `{ep['path']}`: {ep['summary']}")
md_lines.append("")

md_lines.append(f"## 整合注意事項 (Integration Notes)")
md_lines.append("- 請確保在使用 API 時提供正確的認證憑證。")
md_lines.append("- 訂閱事件接口可能需要特殊的 webhook 配置。")
md_lines.append("- 詳細參數說明請參考完整的 OpenAPI 規範檔案。\n")

with open(os.path.join(output_dir, 'api-report.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(md_lines))

# 4. validation-summary.json
validation_summary = {
     "openapi": openapi_version,
     "title": title,
     "version": version,
     "paths": total_paths,
     "operations": operations_count,
     "schemas": schemas_count,
     "methods": list(methods_used),
     "modules": len(tag_counts),
     "event_operations": len(subscription_events),
     "output_files": ["api-report.md", "endpoints.csv", "subscription-events.csv", "validation-summary.json"]
}

with open(os.path.join(output_dir, 'validation-summary.json'), 'w', encoding='utf-8') as f:
    json.dump(validation_summary, f, ensure_ascii=False, indent=2)

print(json.dumps(validation_summary, ensure_ascii=False, indent=2))
