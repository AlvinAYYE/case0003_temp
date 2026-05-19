# 悅康開放平台 API 資料專案

本目錄已整理為可排序的階段式資料夾，方便後續查閱、評估與對接開發。

## 資料夾說明

| 資料夾 | 用途 |
| --- | --- |
| `00_source_docs/` | 原始離線文檔與 Knife4j 匯出的 OpenAPI JSON |
| `01_openapi_swagger/` | 可匯入 Swagger UI / Postman / Apifox 的 OpenAPI JSON/YAML |
| `02_api_reports/` | API 總體報告與匯出摘要 |
| `03_endpoint_indexes/` | 全部端點與事件訂閱端點 CSV 索引 |
| `04_project_preparation/` | 項目前期評估、API 能力地圖、PoC 計畫與對接問題 |
| `05_gemini_validation/` | Gemini CLI 獨立產出與驗收參考 |
| `99_scripts/` | 輔助處理腳本 |

## 建議閱讀順序

1. 先看 `04_project_preparation/pre-project-assessment.md` 理解專案前期結論。
2. 再看 `04_project_preparation/api-capability-map.md` 了解 API 能力邊界。
3. 需要技術細節時看 `02_api_reports/api-report.md` 與 `03_endpoint_indexes/endpoints.csv`。
4. 要匯入工具時使用 `01_openapi_swagger/swagger.json` 或 `01_openapi_swagger/swagger.yaml`。

## 主要統計

- OpenAPI: `3.0.1`
- Paths: `181`
- Operations: `207`
- Schemas: `486`
