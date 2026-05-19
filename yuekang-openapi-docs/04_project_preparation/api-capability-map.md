# API 能力地圖

- 來源：`C:\xampp\htdocs\case0003_temp\yuekang-openapi-docs\00_source_docs\default_OpenAPI.json`
- 產出時間：2026-05-19 21:31:14
- API：悦康开放平台 OPEN-API SPECIFICATION `1.8.1-SNAPSHOT`
- 規模：181 paths / 207 operations / 486 schemas

## 模組能力總表

| 模組 | 業務能力 | Operations | Method 分布 | 前期優先級 | 說明 |
| --- | --- | ---: | --- | --- | --- |
| 01. 基础安全机制 | 授權與令牌 | 2 | POST:2 | 必做 | 所有對接的前置能力，用於取得與更新 token。 |
| 02. 基础运营数据 | 組織與基礎主檔 | 28 | GET:16, POST:7, PUT:4, DELETE:1 | 高 | 診所、部門、員工、角色、渠道與字典等初始同步資料。 |
| 03. 产品类目数据 | 產品、服務與物料主檔 | 31 | GET:10, POST:15, PUT:5, DELETE:1 | 高 | 產品分類、服務項目、物料、價格與相關配置。 |
| 04. 诊疗服务流程 | 預約與診療流程 | 23 | GET:10, POST:9, PUT:4 | 中高 | 預約、排班、到診、諮詢與診療執行流程。 |
| 05. 客户关系管理 | 客戶與會員資料 | 25 | GET:14, POST:6, PUT:3, DELETE:2 | 高 | 客戶、標籤、優惠券、積分與社群帳號等。 |
| 06. 销售财务数据 | 訂單、權益與財務 | 52 | GET:26, POST:22, PUT:3, DELETE:1 | 高 | 訂單、收款、退款、業績與財務報表。 |
| 07. 市场营销集成 | 市場與活動 | 8 | GET:7, POST:1 | 中 | 行銷活動與促銷整合能力。 |
| 08. 库存物料集成 | 庫存與供應鏈 | 15 | GET:9, POST:3, DELETE:3 | 中高 | 庫房、供應商、入庫、出庫與調撥。 |
| 10. 业务事件订阅 | 事件訂閱與 Webhook | 6 | GET:4, POST:2 | 必做 | 平台在業務變更時主動推送事件，也可查詢歷史事件做補償。 |
| 11. 电子健康档案 | 電子健康檔案 | 8 | GET:7, POST:1 | 視場景 | 診療計畫、處方、醫囑與病歷等敏感資料。 |
| 12. 云晰系统集成 | 雲晰系統集成 | 3 | POST:3 | 視場景 | 雲晰訂單、核銷與退款等定制流程。 |
| X1. 业务报表数据 | 業務報表 | 3 | GET:3 | 中 | 銷售業績、執行業績與往來帳報表。 |
| X2. SCRM集成服务 | SCRM 與微信粉絲 | 3 | GET:1, POST:2 | 視場景 | SCRM 代理、微信粉絲查詢與綁定。 |

## 前期解讀

- 這套 API 覆蓋主檔同步、流程操作、財務庫存與事件通知，不是單純查詢服務。
- 項目前期應先收斂場景：客戶同步、訂單財務、預約診療、庫存或事件訂閱。
- 事件訂閱是近即時同步的關鍵，需先驗證 callback、重試、簽名、冪等與補償。

## 模組端點樣本

### 01. 基础安全机制 - 授權與令牌

- 建議優先級：必做

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/auth/login` | 根据注册的APPID获取访问令牌（Token） |
| POST | `/api/v1/auth/refresh` | 在访问令牌（Token）过期之前，使用临时ticket更新令牌，可避免secret泄漏 |

### 02. 基础运营数据 - 組織與基礎主檔

- 建議優先級：高

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/foundation/channel` | 获取授权机构下的客户渠道信息 |
| POST | `/api/v1/foundation/channel` | 在指定层级下创建渠道新节点 |
| PUT | `/api/v1/foundation/channel/partial/{type}/{id}` | 部分修改指定渠道节点 |
| DELETE | `/api/v1/foundation/channel/{type}/{id}` | 删除指定层级的指定渠道节点 |
| PUT | `/api/v1/foundation/channel/{type}/{id}/active` | 改变指定渠道节点(不包含分类)启用状态 |
| GET | `/api/v1/foundation/clinic` | 获取授权机构下的诊所信息 |
| GET | `/api/v1/foundation/clinic/{id}` | 根据ID获取诊所信息 |
| GET | `/api/v1/foundation/clinic/{id}/room` | 查找指定诊所的治疗房间、手术房间 |
| GET | `/api/v1/foundation/code/{system}` | 获取授权机构下的指定字典数据 |
| POST | `/api/v1/foundation/department` | 在授权机构下新增组织节点 - 部门 |

### 03. 产品类目数据 - 產品、服務與物料主檔

- 建議優先級：高

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/catalog/category` | 指定类型下创建分类新节点 - 各类型通用 |
| GET | `/api/v1/catalog/category/goods/tree` | 获取授权机构下的物料类数据分类(树状结构) |
| GET | `/api/v1/catalog/category/service/tree` | 获取授权机构下的服务类项目分类(树状结构) |
| GET | `/api/v1/catalog/category/{id}` | 获取指定ID分类节点 - 各类型通用 |
| PUT | `/api/v1/catalog/category/{id}` | 修改指定ID分类节点 - 各类型通用 |
| DELETE | `/api/v1/catalog/category/{id}` | 删除指定ID分类节点 - 各类型通用 |
| POST | `/api/v1/catalog/product/clinic-sales-price/list` | 查询项目/商品下发 |
| POST | `/api/v1/catalog/product/clinic-sales-price/update` | 修改项目/商品下发 |
| GET | `/api/v1/catalog/product/goods` | 获取授权机构下的物料类数据 - 耗材、药品、药妆等受库存管控条目 |
| POST | `/api/v1/catalog/product/goods` | 新建物料类数据 |

### 04. 诊疗服务流程 - 預約與診療流程

- 建議優先級：中高

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/workflow/appointment` | 获取授权机构下的预约数据 - 列表 |
| POST | `/api/v1/workflow/appointment` | 创建预约 |
| POST | `/api/v1/workflow/appointment/getAppointmentFreeList` | 获取预约空闲时间段 |
| GET | `/api/v1/workflow/appointment/{id}` | 获取授权机构下的预约数据 - 单个 |
| PUT | `/api/v1/workflow/appointment/{id}/cancel` | 取消预约 |
| PUT | `/api/v1/workflow/appointment/{id}/confirm` | 确认预约 |
| PUT | `/api/v1/workflow/appointment/{id}/partial` | 修改预约 |
| POST | `/api/v1/workflow/archives/document/upload` | 上传档案文件 |
| GET | `/api/v1/workflow/consultation` | 获取授权机构下的咨询数据 |
| POST | `/api/v1/workflow/consultation` | 创建咨询 |

### 05. 客户关系管理 - 客戶與會員資料

- 建議優先級：高

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/crm/customer` | 获取授权机构下的客户数据 |
| POST | `/api/v1/crm/customer` | 在授权机构下创建新客户 |
| GET | `/api/v1/crm/customer/findByMobile` | 根据手机号码查询客户数据 |
| POST | `/api/v1/crm/customer/getOperatorLog` | 查询客户修改日志 |
| POST | `/api/v1/crm/customer/gift/add` | 增值金调整 |
| GET | `/api/v1/crm/customer/group` | 获取授权机构下的客户的分群标签 |
| GET | `/api/v1/crm/customer/group-definition` | 获取授权机构下的客户分群分组定义 - 分页 |
| POST | `/api/v1/crm/customer/membershipLevel` | 修改客户会员等级 |
| GET | `/api/v1/crm/customer/membershipLevel/list` | 获取会员等级目录 |
| GET | `/api/v1/crm/customer/merge-log` | 获取授权机构下的客户合并数据 |

### 06. 销售财务数据 - 訂單、權益與財務

- 建議優先級：高

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/account-item/balance/refund` | 储值金退款 |
| GET | `/api/v1/account-item/card/detail` | 查询权益 - 按ID查询卡项权益详情 |
| GET | `/api/v1/account-item/card/page` | 查询权益 - 按客户ID查询可用卡项 |
| POST | `/api/v1/account-item/card/redeem` | 卡项确认品项 |
| POST | `/api/v1/account-item/card/redeem-revoke` | 卡项作废确认品项 |
| GET | `/api/v1/account-item/card/redeemed/page` | 查询权益 - 支持查询卡项已兑换的单品权益 |
| GET | `/api/v1/account-item/product-item/byId` | 查询权益 - 按ID查询单品权益 |
| POST | `/api/v1/account-item/reward/adjust` | 增值金余额调整 |
| POST | `/api/v1/billing/customer/transfer/product-item` | 操作客户转疗（自动同意转疗） |
| GET | `/api/v1/billing/customer/{id}/esthetics/estimate-item` | 获取客户美学评估单特征 |

### 07. 市场营销集成 - 市場與活動

- 建議優先級：中

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/market/card` | 查询授权机构下的卡项信息 |
| GET | `/api/v1/market/card/prompt` | 根据条件查询可用卡项信息 |
| GET | `/api/v1/market/card/{id}` | 精确获取授权机构下的卡项信息 |
| GET | `/api/v1/market/coupon` | 获取授权机构下的优惠券信息 |
| GET | `/api/v1/market/coupon/{id}` | 精确获取授权机构下的优惠券信息 |
| GET | `/api/v1/market/promotion` | 获取授权机构下的促销信息 |
| POST | `/api/v1/market/promotion/active` | 促销启用/停用 |
| GET | `/api/v1/market/promotion/{id}` | 根据ID获取促销信息 |

### 08. 库存物料集成 - 庫存與供應鏈

- 建議優先級：中高

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/inventory/change-type/{bizType}` | 获取授权机构下出/入库类别，bizType参数: stock-in(入库), stock-out(出库) |
| GET | `/api/v1/inventory/outbound/all` | 获取提货单信息 - 翻页 |
| GET | `/api/v1/inventory/purchaseOrder` | 物资采购订单 |
| GET | `/api/v1/inventory/stock-item` | 获取授权机构下的所有库存条目信息 |
| GET | `/api/v1/inventory/stock-item/stock-in` | 物料入库记录 |
| POST | `/api/v1/inventory/stock-item/stock-in` | 物料入库操作 |
| DELETE | `/api/v1/inventory/stock-item/stock-in/{id}` | 作废物料入库记录 |
| GET | `/api/v1/inventory/stock-item/stock-out` | 物料出库记录 |
| POST | `/api/v1/inventory/stock-item/stock-out` | 物料出库操作 |
| DELETE | `/api/v1/inventory/stock-item/stock-out/{id}` | 作废物料出库记录 |

### 10. 业务事件订阅 - 事件訂閱與 Webhook

- 建議優先級：必做

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/event/event-history` | 获取历史事件分页列表 |
| GET | `/api/v1/event/event-history/single-entity` | 获取特定业务实体对应的历史事件列表 |
| GET | `/api/v1/event/subscribe` | 获取当前订阅列表 |
| POST | `/api/v1/event/subscribe` | 订阅系统业务事件主题，结果返回当前订阅 |
| GET | `/api/v1/event/topic` | 获取当前系统支持的事件主题 |
| POST | `/api/v1/event/unsubscribe/{id}` | 取消订阅系统业务事件主题 |

### 11. 电子健康档案 - 電子健康檔案

- 建議優先級：視場景

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/ehr/care-plan` | 在授权机构下的创建患者诊疗计划 |
| GET | `/api/v1/ehr/prescription` | 获取授权机构下的处方数据 |
| GET | `/api/v1/ehr/prescriptionNew` | 获取授权机构下的新版本医嘱服务的处方数据 |
| GET | `/api/v1/ehr/queryAdvicesOrderList` | 获取授权机构下医嘱服务的医嘱数据 |
| GET | `/api/v1/ehr/queryAdvicesOrderListByPatientId` | 获取授权机构下客户的医嘱服务的医嘱数据 |
| GET | `/api/v1/ehr/queryMedicalRecordDetail` | 获取授权机构下医嘱服务的病历数据明细 |
| GET | `/api/v1/ehr/queryMedicalRecordList` | 获取授权机构下医嘱服务的病历数据 |
| GET | `/api/v1/ehr/queryMedicalRecordListByPatientId` | 获取授权机构下客户的医嘱服务的病历数据 |

### 12. 云晰系统集成 - 雲晰系統集成

- 建議優先級：視場景

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/integration/yunxi/create-order` | 多品项开单，按品项拆分多个订单，成功后为已支付订单，忽略所有审批流程 |
| POST | `/api/v1/integration/yunxi/fulfillment` | 单订单（单品项）核销状态同步 |
| POST | `/api/v1/integration/yunxi/refund` | 单订单（单品项）全部或部分退款 |

### X1. 业务报表数据 - 業務報表

- 建議優先級：中

| Method | Path | Summary |
| --- | --- | --- |
| GET | `/api/v1/analytic/cash/performance/page` | 查询员工销售业绩数据 |
| GET | `/api/v1/analytic/execution/performance/page` | 查询员工执行业绩数据 |
| GET | `/api/v1/analytic/financial/accountDealing/page` | 查询往来账数据 |

### X2. SCRM集成服务 - SCRM 與微信粉絲

- 建議優先級：視場景

| Method | Path | Summary |
| --- | --- | --- |
| POST | `/api/v1/scrm/proxy` | scrm服务代理 |
| GET | `/api/v1/scrm/wechat-fan` | 查询授权机构下的微信公众号粉丝 |
| POST | `/api/v1/scrm/wechat-fan/bind` | 在授权机构下绑定微信公众号粉丝 |
