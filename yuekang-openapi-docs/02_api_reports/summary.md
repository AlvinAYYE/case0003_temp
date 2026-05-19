# 悅康開放平台 OpenAPI 匯出摘要

- 來源：C:\xampp\htdocs\case0003_temp\yuekang-openapi-docs\00_source_docs\default_OpenAPI.json
- 匯出時間：2026-05-19T13:02:08.613998+00:00
- OpenAPI 版本：3.0.1
- 文件版本：1.8.1-SNAPSHOT
- API 標題：悦康开放平台 OPEN-API SPECIFICATION
- Paths：181
- Operations：207
- Methods：DELETE 8, GET 107, POST 73, PUT 19
- Schemas：486
- 訂閱事件相關 Operations：6

## 分類統計

| Tag | Operations |
| --- | ---: |
| 06. 销售财务数据 | 52 |
| 03. 产品类目数据 | 31 |
| 02. 基础运营数据 | 28 |
| 05. 客户关系管理 | 25 |
| 04. 诊疗服务流程 | 23 |
| 08. 库存物料集成 | 15 |
| 07. 市场营销集成 | 8 |
| 11. 电子健康档案 | 8 |
| 10. 业务事件订阅 | 6 |
| 12. 云晰系统集成 | 3 |
| X1. 业务报表数据 | 3 |
| X2. SCRM集成服务 | 3 |
| 01. 基础安全机制 | 2 |

## 訂閱事件端點

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/event/event-history` | 获取历史事件分页列表 |
| GET | `/api/v1/event/event-history/single-entity` | 获取特定业务实体对应的历史事件列表 |
| GET | `/api/v1/event/subscribe` | 获取当前订阅列表 |
| POST | `/api/v1/event/subscribe` | 订阅系统业务事件主题，结果返回当前订阅 |
| GET | `/api/v1/event/topic` | 获取当前系统支持的事件主题 |
| POST | `/api/v1/event/unsubscribe/{id}` | 取消订阅系统业务事件主题 |
