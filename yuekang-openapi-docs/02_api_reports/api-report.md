# 悅康開放平台 API 報告

## 1. 報告範圍

- 來源檔案： `C:\xampp\htdocs\case0003_temp\yuekang-openapi-docs\00_source_docs\default_OpenAPI.json`
- 產出時間： 2026-05-19 21:42:13
- API 文件標題： 悦康开放平台 OPEN-API SPECIFICATION
- API 文件版本： 1.8.1-SNAPSHOT
- OpenAPI 版本： 3.0.1
- Server： https://emuat01-ym-openapi-svc.lcuat.cn

本報告依據 Knife4j 匯出的 OpenAPI JSON 產生，重點在 API 結構、分類、授權方式、端點清單與訂閱事件接口。

## 2. 總覽

| 指標 | 數量 |
| --- | ---: |
| Paths | 181 |
| Operations | 207 |
| Schemas | 486 |
| 含 requestBody 的操作 | 90 |
| 含 parameters 的操作 | 128 |
| 缺 summary 的操作 | 0 |

| Method | Operations |
| --- | ---: |
| GET | 107 |
| POST | 73 |
| PUT | 19 |
| DELETE | 8 |

## 3. 認證與安全

| Scheme | Type | In | Name | Description |
| --- | --- | --- | --- | --- |
| x-access-token | apiKey | header | `x-access-token` | 授权令牌 |

- 全域 security： `[{"x-access-token": []}]`
- 實作整合時應在 HTTP header 帶入 `x-access-token`。

## 4. 業務模組分布

| 模組 | 說明 | Operations | GET | POST | PUT | DELETE |
| --- | --- | ---: | ---: | ---: | ---: | ---: |
| 01. 基础安全机制 | 获取API访问所需要的关键信息，用以支持三方集成 | 2 | 0 | 2 | 0 | 0 |
| 02. 基础运营数据 | API获取基础运营数据：组织结构、人员、角色、渠道等，用以支持三方集成 | 28 | 16 | 7 | 4 | 1 |
| 03. 产品类目数据 | API获取基础类目数据，用以支持三方集成 | 31 | 10 | 15 | 5 | 1 |
| 04. 诊疗服务流程 | 获取API同步诊疗服务流程数据，用以支持三方集成 | 23 | 10 | 9 | 4 | 0 |
| 05. 客户关系管理 | 获取API访问所需要的客户相关数据，用以支持三方集成 | 25 | 14 | 6 | 3 | 2 |
| 06. 销售财务数据 | API获取权益数据，用以支持三方集成 | 52 | 26 | 22 | 3 | 1 |
| 07. 市场营销集成 | 获取API访问所需要的市场营销数据，用以支持三方集成 | 8 | 7 | 1 | 0 | 0 |
| 08. 库存物料集成 | 获取API同步供应链数据，用以支持三方集成 | 15 | 9 | 3 | 0 | 3 |
| 10. 业务事件订阅 | 订阅业务变更数据，用以支持三方集成近实时同步/通知 | 6 | 4 | 2 | 0 | 0 |
| 11. 电子健康档案 | 获取API同步医疗电子健康档案数据，用以支持三方集成 | 8 | 7 | 1 | 0 | 0 |
| 12. 云晰系统集成 | 云晰直播业务流程集成定制接口 | 3 | 0 | 3 | 0 | 0 |
| X1. 业务报表数据 | API获取核心报表数据，用以支持三方集成 | 3 | 3 | 0 | 0 | 0 |
| X2. SCRM集成服务 | 通过API与SCRM进行集成 | 3 | 1 | 2 | 0 | 0 |

觀察：接口主要集中在財務、產品、基礎運營、客戶與診療流程類型，整體以查詢型 GET 與寫入型 POST 為主。

## 5. 訂閱事件接口

此模組用於訂閱業務變更資料，支援近即時同步與通知。

| Method | Path | Summary | OperationId | Request | Responses |
| --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/event/event-history` | 获取历史事件分页列表 | `pageEventHistory` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); startTime (query, 必填, string(date-time)); endTime (query, 選填, string(date-time)); topics (query, 選填, array<string>) | 200： PageEventHistoryDto |
| GET | `/api/v1/event/event-history/single-entity` | 获取特定业务实体对应的历史事件列表 | `pageEventHistory_1` | bizEntityId (query, 必填, string) | 200： array<EventHistoryDto> |
| GET | `/api/v1/event/subscribe` | 获取当前订阅列表 | `subscribeTopics_1` |  | 200： array<TopicSubscriptionDto> |
| POST | `/api/v1/event/subscribe` | 订阅系统业务事件主题，结果返回当前订阅 | `subscribeTopics` | application/json： CreateSubscriptionParams | 201： TopicSubscriptionDto |
| GET | `/api/v1/event/topic` | 获取当前系统支持的事件主题 | `listSupportedTopics` |  | 200： array<EventTopicDto> |
| POST | `/api/v1/event/unsubscribe/{id}` | 取消订阅系统业务事件主题 | `unsubscribeTopics` | id (path, 必填, string) | 202： TopicSubscriptionDto |

## 6. 資料模型使用概況

| 類型 | 前 15 個常見 Schema |
| --- | --- |
| Request Body | ActiveParams (2), RevokeCancelExecutionParams (2), AuthLoginParams (1), AuthRefreshParams (1), CreateChannelParam (1), PartialModifyChannelParam (1), ActiveChannelParams (1), CreateDepartmentParams (1), CreateEmployeeParams (1), ModifyEmployParams (1), ModifyEmployBaseParams (1), TagCreateParam (1), TagGroupCreateParam (1), TagGroupUpdateParam (1), TagUpdateParam (1) |
| Response Body | IdDto (28), GeneralYunxiResponse (4), array<AccountCouponDto> (3), PageSalesOrderDto (3), IdString (3), AuthResultDto (2), array<CategoryDto> (2), PageCustomerDto (2), string (2), PageExecutionRecordDto (2), ExecutionRecordRevokeResult (2), array<BillingApportionDto> (2), SalesOrderDetailDto (2), PageFusionCardDto (2), TopicSubscriptionDto (2) |

## 7. 文件品質與整合注意事項

- OpenAPI 結構完整，可直接匯入 Swagger UI、Knife4j、Postman、Apifox 等支援 OpenAPI 3 的工具。
- 規格宣告全域 `x-access-token` header，測試與正式呼叫都需要取得授權令牌。
- 報告未推測業務語意；端點說明、參數、request/response schema 均以 OpenAPI JSON 內容為準。
- 若下游工具只支援 Swagger 2.0，需要另外做 OpenAPI 3 到 Swagger 2.0 轉換。

## 8. 完整端點索引

### 01. 基础安全机制

获取API访问所需要的关键信息，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| POST | `/api/v1/auth/login` | 根据注册的APPID获取访问令牌（Token） | `login` |  | application/json： AuthLoginParams | 201： AuthResultDto |
| POST | `/api/v1/auth/refresh` | 在访问令牌（Token）过期之前，使用临时ticket更新令牌，可避免secret泄漏 | `refresh` |  | application/json： AuthRefreshParams | 201： AuthResultDto |

### 02. 基础运营数据

API获取基础运营数据：组织结构、人员、角色、渠道等，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/foundation/channel` | 获取授权机构下的客户渠道信息 | `findReferrerPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); enabled (query, 選填, boolean); keyword (query, 選填, string); channelCategoryId (query, 選填, string); channelId (query, 選填, string); referrerId (query, 選填, string) |  | 200： PageReferrerDetailDto |
| GET | `/api/v1/foundation/clinic` | 获取授权机构下的诊所信息 | `findClinicAll` | keyword (query, 選填, string) |  | 200： array<ClinicDto> |
| GET | `/api/v1/foundation/clinic/{id}` | 根据ID获取诊所信息 | `loadClinic` | id (path, 必填, string) |  | 200： ClinicDto |
| GET | `/api/v1/foundation/clinic/{id}/room` | 查找指定诊所的治疗房间、手术房间 | `findClinicRoom` | id (path, 必填, string) |  | 200： array<RoomDto> |
| GET | `/api/v1/foundation/code/{system}` | 获取授权机构下的指定字典数据 | `findCodedValuesAll` | system (path, 必填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageCodeValueDto |
| GET | `/api/v1/foundation/download/{fileId}` | 下载文件接口 | `download` | fileId (path, 必填, string) |  | 200 |
| GET | `/api/v1/foundation/employee` | 获取授权机构下的员工信息 | `findEmployeePaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); keyword (query, 選填, string); clinicId (query, 選填, string); onboard (query, 選填, boolean) |  | 200： PageEmployeeDto |
| GET | `/api/v1/foundation/employee/{id}` | 获取授权机构下的指定员工信息 | `findEmployee` | id (path, 必填, string) |  | 200： EmployeeDto |
| GET | `/api/v1/foundation/employee/{id}/roles` | 获取授权机构下的指定员工功能权限 | `findEmployeeRolePermissions` | id (path, 必填, string) |  | 200： EmployeeRolesDto |
| GET | `/api/v1/foundation/job` | 获取授权机构下的员工职位角色信息 | `findJobAll` |  |  | 200： array<JobRoleDto> |
| GET | `/api/v1/foundation/logo` | 获取授权机构的logo(Base64格式，空代表未设置) | `findLogo` |  |  | 200： StringData |
| GET | `/api/v1/foundation/medical-department` | 获取授权机构下医疗科室信息 | `listMedicalDepartment` |  |  | 200： array<MedicalDepartmentDto> |
| GET | `/api/v1/foundation/organization` | 获取授权机构下的组织架构，包括公司、区域、诊所、部门 | `findOrganizationAll` |  |  | 500： ErrorInfoDto |
| GET | `/api/v1/foundation/role` | 获取授权机构下的员工功能角色信息 | `findRoleAll` |  |  | 200： array<SecurityRoleDto> |
| GET | `/api/v1/foundation/role/{id}` | 获取授权机构下指定功能角色信息 | `findRole` | id (path, 必填, string) |  | 200： SecurityRoleDto |
| GET | `/api/v1/foundation/tagSets` | 获取标签信息 | `findTagSets` |  |  | 200： array<TagSetDto> |
| POST | `/api/v1/foundation/channel` | 在指定层级下创建渠道新节点 | `createChannel` |  | application/json： CreateChannelParam | 201： IdDto |
| POST | `/api/v1/foundation/department` | 在授权机构下新增组织节点 - 部门 | `createClinic` |  | application/json： CreateDepartmentParams | 201： IdDto |
| POST | `/api/v1/foundation/employee` | 在授权机构下创建员工 | `createEmployee` |  | application/json： CreateEmployeeParams | 201： IdDto |
| POST | `/api/v1/foundation/tagDict/create` | 创建标签 | `tagDictCreate` |  | application/json： TagCreateParam | 200： TagCreateResponse |
| POST | `/api/v1/foundation/tagDict/group/create` | 创建标签组 | `tagDictGroupCreate` |  | application/json： TagGroupCreateParam | 200： TagGroupCreateResponse |
| POST | `/api/v1/foundation/tagDict/group/update` | 修改标签组 | `tagDictGroupUpdate` |  | application/json： TagGroupUpdateParam | 200 |
| POST | `/api/v1/foundation/tagDict/update` | 修改标签 | `tagDictUpdate` |  | application/json： TagUpdateParam | 200 |
| PUT | `/api/v1/foundation/channel/partial/{type}/{id}` | 部分修改指定渠道节点 | `partialModifyChannel` | type (path, 必填, string); id (path, 必填, string) | application/json： PartialModifyChannelParam | 204 |
| PUT | `/api/v1/foundation/channel/{type}/{id}/active` | 改变指定渠道节点(不包含分类)启用状态 | `activeChannel` | type (path, 必填, string); id (path, 必填, string) | application/json： ActiveChannelParams | 204 |
| PUT | `/api/v1/foundation/employee/{id}` | 修改员工信息 | `modifyEmployee` | id (path, 必填, string) | application/json： ModifyEmployParams | 204 |
| PUT | `/api/v1/foundation/employeeBase/{id}` | 修改员工基础信息 | `modifyEmployeeBase` | id (path, 必填, string) | application/json： ModifyEmployBaseParams | 204 |
| DELETE | `/api/v1/foundation/channel/{type}/{id}` | 删除指定层级的指定渠道节点 | `deleteChannel` | type (path, 必填, string); id (path, 必填, string) |  | 204 |

### 03. 产品类目数据

API获取基础类目数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/catalog/category/goods/tree` | 获取授权机构下的物料类数据分类(树状结构) | `findGoodsCategoryPaged` |  |  | 200： array<CategoryDto> |
| GET | `/api/v1/catalog/category/service/tree` | 获取授权机构下的服务类项目分类(树状结构) | `findServiceCategoryTree` |  |  | 200： array<CategoryDto> |
| GET | `/api/v1/catalog/category/{id}` | 获取指定ID分类节点 - 各类型通用 | `loadCategory` | id (path, 必填, string) |  | 200： CategoryDto |
| GET | `/api/v1/catalog/product/goods` | 获取授权机构下的物料类数据 - 耗材、药品、药妆等受库存管控条目 | `findGoodsPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); keyword (query, 選填, string); categoryId (query, 選填, string); enabled (query, 選填, boolean); isPharmacy (query, 選填, boolean); businessTypeCodes (query, 選填, array<string>) |  | 200： PageProductSkuDto |
| GET | `/api/v1/catalog/product/goods/{id}` | 获取授权机构下的物料类数据 - 耗材、药品、药妆等受库存管控条目 | `findGoodsPaged_1` | id (path, 必填, string) |  | 200： ProductSkuDto |
| GET | `/api/v1/catalog/product/service` | 获取授权机构下的服务类项目数据 - 服务项目 | `findServicePaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); ids (query, 選填, array<string>); keyword (query, 選填, string); categoryId (query, 選填, string); enabled (query, 選填, boolean); businessTypeCodes (query, 選填, array<string>); liveShowFilter (query, 選填, boolean) |  | 200： PageCareServiceDto |
| GET | `/api/v1/catalog/product/service/findExecutionRole` | 查询操作人员职位 | `findExecutionRole` |  |  | 200： array<ExecutionRoleDto> |
| GET | `/api/v1/catalog/product/service/getOperationStepDictPageList` | 查询操作步骤 | `getOperationStepDictPageList` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); keyword (query, 選填, string) |  | 200： PageOperationStepDictListDto |
| GET | `/api/v1/catalog/product/service/price-rule` | 获取授权机构下的服务类项目数据 - 服务项目价格规则 | `findServicePriceRule` | ids (query, 選填, array<string>); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageCareServicePriceRuleDto |
| GET | `/api/v1/catalog/product/service/{id}` | 获取授权机构下的服务类项目数据 - 单个项目 | `loadServiceById` | id (path, 必填, string) |  | 200： CareServiceDto |
| POST | `/api/v1/catalog/category` | 指定类型下创建分类新节点 - 各类型通用 | `createCategory` |  | application/json： CreateCategoryParam | 201： IdDto |
| POST | `/api/v1/catalog/product/clinic-sales-price/list` | 查询项目/商品下发 | `listProductClinicSalesPrice` |  | application/json： QueryProductSalesPriceParams | 200： array<ProductClinicSalesPriceDto> |
| POST | `/api/v1/catalog/product/clinic-sales-price/update` | 修改项目/商品下发 | `updateProductClinicSalesPrice` |  | application/json： UpdateProductClinicSalesPriceParams | 200 |
| POST | `/api/v1/catalog/product/goods` | 新建物料类数据 | `createGoods` |  | application/json： CreateProdSpecParams | 201： IdDto |
| POST | `/api/v1/catalog/product/service` | 新建服务项目数据 | `createService` |  | application/json： CreateServiceParams | 201： IdDto |
| POST | `/api/v1/catalog/product/service/addMaterial` | 添加项目的使用耗材 | `addCareServiceMaterial` |  | application/json： CreateCareServiceMaterialParam | 200 |
| POST | `/api/v1/catalog/product/service/addOperator` | 添加项目的操作人员 | `addCareServiceOperator` |  | application/json： CreateCareServiceOperatorParam | 200 |
| POST | `/api/v1/catalog/product/service/addStep` | 添加项目的操作步骤 | `addCareServiceStep` |  | application/json： CreateCareServiceStepParam | 200 |
| POST | `/api/v1/catalog/product/service/deleteMaterial` | 删除项目的使用耗材 | `deleteCareServiceMaterial` |  | application/json： DeleteCareServiceMaterialParam | 200 |
| POST | `/api/v1/catalog/product/service/deleteOperator` | 删除项目的操作人员 | `deleteCareServiceOperator` |  | application/json： DeleteCareServiceOperatorParam | 200 |
| POST | `/api/v1/catalog/product/service/deleteStep` | 删除项目的操作步骤 | `deleteCareServiceStep` |  | application/json： DeleteCareServiceStepParam | 200 |
| POST | `/api/v1/catalog/product/service/price-rule/update` | 修改服务类项目价格规则 | `updateServicePriceRule` |  | application/json： UpdateCareServicePriceRuleParams | 200： CareServicePriceRuleModifyResultDto |
| POST | `/api/v1/catalog/product/service/updateMaterial` | 修改项目的使用耗材 | `updateCareServiceMaterial` |  | application/json： UpdateCareServiceMaterialParam | 200 |
| POST | `/api/v1/catalog/product/service/updateOperator` | 修改项目的操作人员 | `updateCareServiceOperator` |  | application/json： UpdateCareServiceOperatorParam | 200 |
| POST | `/api/v1/catalog/product/service/updateStep` | 修改项目的操作步骤 | `updateCareServiceStep` |  | application/json： UpdateCareServiceStepParam | 200 |
| PUT | `/api/v1/catalog/category/{id}` | 修改指定ID分类节点 - 各类型通用 | `modifyCategory` | id (path, 必填, string) | application/json： ModifyCategoryParam | 204 |
| PUT | `/api/v1/catalog/product/goods/{id}` | 修改物料类数据 | `activeGoods` | id (path, 必填, string) | application/json： ModifyProdSpecParams | 204 |
| PUT | `/api/v1/catalog/product/goods/{id}/active` | 停用、启用物料类数据 | `activeGoods_1` | id (path, 必填, string) | application/json： ActiveParams | 204 |
| PUT | `/api/v1/catalog/product/service/{id}` | 根据服务项目id更新服务项目 | `modifyService` | id (path, 必填, string) | application/json： ModifyServiceParams | 204 |
| PUT | `/api/v1/catalog/product/service/{id}/active` | 暂停/启用服务项目 | `activeService` | id (path, 必填, string) | application/json： ActiveParams | 204 |
| DELETE | `/api/v1/catalog/category/{id}` | 删除指定ID分类节点 - 各类型通用 | `deleteCategory` | id (path, 必填, string) |  | 204 |

### 04. 诊疗服务流程

获取API同步诊疗服务流程数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/workflow/appointment` | 获取授权机构下的预约数据 - 列表 | `findAppointmentPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); clinicId (query, 選填, string); customerId (query, 選填, string); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); ownerId (query, 選填, string); serviceKeyword (query, 選填, string); cancelled (query, 選填, boolean); careClass (query, 選填, array<string>); specialty (query, 選填, array<string>); operatorId (query, 選填, string); createStart (query, 選填, string(date-time)); createEnd (query, 選填, string(date-time)) |  | 200： PageAppointmentDto |
| GET | `/api/v1/workflow/appointment/{id}` | 获取授权机构下的预约数据 - 单个 | `findAppointmentById` | id (path, 必填, string) |  | 200： AppointmentDto |
| GET | `/api/v1/workflow/consultation` | 获取授权机构下的咨询数据 | `findConsultationPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); clinicId (query, 選填, string); customerId (query, 選填, string); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); methodCodes (query, 選填, array<string>); associatedId (query, 選填, string); creatorId (query, 選填, string); deal (query, 選填, boolean); arrive (query, 選填, boolean) |  | 200： PageConsultationDto |
| GET | `/api/v1/workflow/participant/status` | 获取授权机构下的现场人员空闲状态 - Experimental | `listOperatorStatus` | clinicId (query, 必填, string); roleCode (query, 必填, string) |  | 200： array<ParticipantStatusDto> |
| GET | `/api/v1/workflow/photoCompares` | 获取前后对比照数据 | `findPhotoCompares` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); customerId (query, 選填, string); organizationId (query, 選填, string); startTime (query, 選填, string(date-time)); endTime (query, 選填, string(date-time)) |  | 200： PagePhotoCompareDto |
| GET | `/api/v1/workflow/schedule` | 分页获取授权机构下的排班数据 | `ListSchedule` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); employeeId (query, 選填, string) |  | 200： PageScheduleItemDto |
| GET | `/api/v1/workflow/schedule-rule` | 分页获取授权机构下的班次信息 | `ListScheduleRule` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); clinicId (query, 選填, string) |  | 200： PageScheduleRuleDto |
| GET | `/api/v1/workflow/visit` | 获取授权机构下的到访数据 | `findVisitPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); clinicId (query, 選填, string); customerId (query, 選填, string); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); status (query, 選填, string); appointmentId (query, 選填, string) |  | 200： PageVisitDto |
| GET | `/api/v1/workflow/visit/customer-info` | 到访客户信息 | `todayVisitCustomerInfo` | customerNumber (query, 選填, string); phoneNumber (query, 選填, string) |  | 200： ApiResultTodayVisitCustomerDTO |
| GET | `/api/v1/workflow/visit/{customerId}/operation/token` | 到访操作token | `findOperationToken` | customerId (path, 必填, string) |  | 200： TokenDto |
| POST | `/api/v1/workflow/appointment` | 创建预约 | `createAppointment_1` |  | application/json： CreateAppointmentParams | 201： IdDto |
| POST | `/api/v1/workflow/appointment/getAppointmentFreeList` | 获取预约空闲时间段 | `getAppointmentFreeList` |  | application/json： AppointmentFreeParams | 200： AppointmentFreeDto |
| POST | `/api/v1/workflow/archives/document/upload` | 上传档案文件 | `documentUpload` | customerId (query, 必填, string); categoryType (query, 必填, string); organizationId (query, 必填, string) | application/json： object | 200： DocumentUploadDto |
| POST | `/api/v1/workflow/consultation` | 创建咨询 | `createConsultation` |  | application/json： CreateConsultationParams | 201： IdDto |
| POST | `/api/v1/workflow/modify/consultation` | 修改咨询 | `modifyConsultation` |  | application/json： ModifyConsultationParams | 200 |
| POST | `/api/v1/workflow/schedule` | 在授权机构下创建排班 | `createSchedule` |  | application/json： CreateScheduleParams | 201： IdDto |
| POST | `/api/v1/workflow/schedule-rule` | 在授权机构下创建班次 | `createScheduleRule` |  | application/json： CreateScheduleRuleParams | 201： IdDto |
| POST | `/api/v1/workflow/sign-in` | 创建签到 | `createSignIn` |  | application/json： SignInParams | 200： SignInDto |
| POST | `/api/v1/workflow/visit` | 创建到访 | `createAppointment` |  | application/json： CreateVisitParams | 201： IdDto |
| PUT | `/api/v1/workflow/appointment/{id}/cancel` | 取消预约 | `cancelAppointment` | id (path, 必填, string) | application/json： CancelAppointmentParams | 204 |
| PUT | `/api/v1/workflow/appointment/{id}/confirm` | 确认预约 | `confirmAppointment` | id (path, 必填, string) | application/json： ConformAppointmentParams | 204 |
| PUT | `/api/v1/workflow/appointment/{id}/partial` | 修改预约 | `modifyAppointment` | id (path, 必填, string) | application/json： ModifyAppointmentParams | 204 |
| PUT | `/api/v1/workflow/schedule-rule/{id}` | 在授权机构下修改班次 | `updateScheduleRule` | id (path, 必填, string) | application/json： UpdateScheduleRuleParams | 204 |

### 05. 客户关系管理

获取API访问所需要的客户相关数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/crm/customer` | 获取授权机构下的客户数据 | `findCustomerPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); birthday (query, 選填, Birthday); keyword (query, 選填, string); groupIds (query, 選填, array<string>); secondLevelChannelId (query, 選填, string); queryBinding (query, 選填, boolean); includeUnbound (query, 選填, boolean); bindingType (query, 選填, string) |  | 200： PageCustomerDto |
| GET | `/api/v1/crm/customer/findByMobile` | 根据手机号码查询客户数据 | `findByMobile` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); mobile (query, 選填, string); queryBinding (query, 選填, boolean); includeUnbound (query, 選填, boolean); bindingType (query, 選填, string) |  | 200： PageCustomerDto |
| GET | `/api/v1/crm/customer/group` | 获取授权机构下的客户的分群标签 | `findCustomerGroupByIds` | ids (query, 必填, array<string>) |  | 200： object |
| GET | `/api/v1/crm/customer/group-definition` | 获取授权机构下的客户分群分组定义 - 分页 | `findCustomerGroup` | name (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageCustomerGroupInfo |
| GET | `/api/v1/crm/customer/membershipLevel/list` | 获取会员等级目录 | `findMembershipLevel` | membershipLevelStatus (query, 選填, integer(int32)) |  | 200： array<MembershipDto> |
| GET | `/api/v1/crm/customer/merge-log` | 获取授权机构下的客户合并数据 | `findCustomerMergeLog` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); source (query, 選填, string); target (query, 選填, string); status (query, 選填, string) |  | 200： PageMergeLogDto |
| GET | `/api/v1/crm/customer/{id}` | 根据客户Id获取授权机构下的客户数据 | `findCustomerById` | id (path, 必填, string); queryBinding (query, 選填, boolean); includeUnbound (query, 選填, boolean); bindingType (query, 選填, string) |  | 200： CustomerDetailDto |
| GET | `/api/v1/crm/customer/{id}/account` | 根据客户Id获取授权机构下的账户余额 | `findAccountOfCustomer` | id (path, 必填, string) |  | 200： AccountDto |
| GET | `/api/v1/crm/customer/{id}/account/coupon/_list` | 根据客户ID查询券余 | `listAccountCoupon` | id (path, 必填, string); status (query, 選填, string) |  | 200： array<AccountCouponDto> |
| GET | `/api/v1/crm/customer/{id}/account/journal` | 根据客户Id获取授权机构下的账户余额变动数据 | `findAccountOfCustomer_1` | id (path, 必填, string); clinicId (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageAccountJournalDto |
| GET | `/api/v1/crm/customer/{id}/careClass` | 获取授权机构下根据客户Id获取客户当日到访类型 | `findCustomerCareClass` | id (path, 必填, string) |  | 200： array<CareClassDto> |
| GET | `/api/v1/crm/customer/{id}/expense/summary` | 根据客户ID获取客户汇总消费金额 | `queryCustomerExpenseSummary` | id (path, 必填, string) |  | 200： CustomerSummaryDto |
| GET | `/api/v1/crm/customerDetail` | 根据客户Id获取授权机构下的客户简单数据 | `findCustomerSimpleDetailById` | customerId (query, 必填, string) |  | 200： CustomerSimpleDetailDto |
| GET | `/api/v1/crm/customerList` | 获取授权机构下的客户列表数据 | `findCustomerList` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); birthday (query, 選填, Birthday); keyword (query, 選填, string); groupIds (query, 選填, array<string>); secondLevelChannelId (query, 選填, string) |  | 200： PageCustomerSimpleListDto |
| POST | `/api/v1/crm/customer` | 在授权机构下创建新客户 | `createCustomer` |  | application/json： CreateCustomerParams | 201： string |
| POST | `/api/v1/crm/customer/getOperatorLog` | 查询客户修改日志 | `getOperatorLog` | customerId (query, 必填, string); operatorBeginDate (query, 必填, string); operatorEndDate (query, 必填, string) |  | 200： array<TaskSnapshotOperateLogVo> |
| POST | `/api/v1/crm/customer/gift/add` | 增值金调整 | `addGift` |  | application/json： AddGiftReq | 200： boolean |
| POST | `/api/v1/crm/customer/membershipLevel` | 修改客户会员等级 | `updateMembershipLevel` | customerId (query, 選填, string); membershipLevel (query, 選填, string); note (query, 選填, string); obtainedDate (query, 選填, string); expireDate (query, 選填, string); give (query, 選填, boolean) |  | 200： string |
| POST | `/api/v1/crm/customer/{id}/account/coupon` | 根据客户ID绑定优惠券 - 返回账户未启用券列表 | `addAccountCoupon` | id (path, 必填, string) | application/json： BindCouponParams | 201： array<AccountCouponDto> |
| POST | `/api/v1/crm/customer/{id}/tag` | 在授权机构下根据客户ID添加自定义标签 | `addCustomerTag` | id (path, 必填, string) | application/json： AddCustomerTagParam | 201 |
| PUT | `/api/v1/crm/customer/{id}` | 在授权机构下修改客户 | `modifyCustomer` | id (path, 必填, string) | application/json： ModifyCustomerParams | 204 |
| PUT | `/api/v1/crm/customer/{id}/account/coupon/_unbind` | 根据客户ID解绑优惠券 - 返回账户未启用券列表 | `revokeAccountCoupon` | id (path, 必填, string) | application/json： UnbindCouponParams | 201： array<AccountCouponDto> |
| PUT | `/api/v1/crm/customer/{id}/account/credit` | 根据客户ID进行积分增减操作 | `changeCredit` | id (path, 必填, string) | application/json： ChangeCreditParams | 204 |
| DELETE | `/api/v1/crm/customer/{id}` | 在授权机构下删除客户 | `deleteCustomer` | id (path, 必填, string) |  | 204 |
| DELETE | `/api/v1/crm/customer/{id}/tag` | 在授权机构下根据客户ID删除标签 | `deleteCustomerTag` | id (path, 必填, string) | application/json： DeleteCustomerTagParam | 204 |

### 06. 销售财务数据

API获取权益数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/account-item/card/detail` | 查询权益 - 按ID查询卡项权益详情 | `cardDetail` | id (query, 必填, string) |  | 200： CardItemDetailDto |
| GET | `/api/v1/account-item/card/page` | 查询权益 - 按客户ID查询可用卡项 | `pageCard` | customerId (query, 必填, string); clinicId (query, 選填, string); orderId (query, 選填, string); status (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageCardItemDto |
| GET | `/api/v1/account-item/card/redeemed/page` | 查询权益 - 支持查询卡项已兑换的单品权益 | `pageCardRedeemedItems` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); customerId (query, 選填, string); storeId (query, 選填, string); rootId (query, 選填, string); includeCompleted (query, 選填, boolean); start (query, 選填, string(date)); end (query, 選填, string(date)) |  | 200： PageAccProductItemDto |
| GET | `/api/v1/account-item/product-item/byId` | 查询权益 - 按ID查询单品权益 | `accountItemDetail` | id (query, 必填, string) |  | 200： AccProductItemDto |
| GET | `/api/v1/billing/customer/{id}/esthetics/estimate-item` | 获取客户美学评估单特征 | `queryEstimateItemPage` | id (path, 必填, string); organizationIdList (query, 必填, array<string>); estimateId (query, 選填, string); estimateDateStart (query, 選填, string(date-time)); estimateDateEnd (query, 選填, string(date-time)); statusList (query, 選填, array<string>) |  | 200： array<QueryEstimateListDto> |
| GET | `/api/v1/billing/customer/{id}/execution-record` | 根据客户Id获取授权机构下的客户项目执行数据 | `findExecutionRecordOfCustomer` | id (path, 必填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageExecutionRecordDto |
| GET | `/api/v1/billing/customer/{id}/prepaid-order` | 根据客户Id获取授权机构下的客户充值订单数据 | `findPrepaidOrderOfCustomer` | id (path, 必填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)) |  | 200： PageSalesOrderDto |
| GET | `/api/v1/billing/customer/{id}/sales-order` | 根据客户Id获取授权机构下的客户销售订单数据 | `findSalesOrderOfCustomer` | id (path, 必填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)) |  | 200： PageSalesOrderDto |
| GET | `/api/v1/billing/customer/{id}/transfer/product-item` | 获取客户可转疗项目 | `findCustomerTransferProductItems` | id (path, 必填, string) |  | 200： CustomerTransferProductItemDto |
| GET | `/api/v1/billing/esthetics/order-relation` | 获取订单与美学规划关联关系 | `queryEstimateItemOrderLineRelation` | estimateId (query, 選填, string); orderId (query, 選填, string) |  | 200： QueryEstimateItemOrderLineRelationDto |
| GET | `/api/v1/billing/exchange/page` | 获取换购记录 | `page` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); customerId (query, 選填, string); clinicIds (query, 選填, array<string>); exchangeStatuses (query, 選填, array<string>); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)) |  | 200： PageExchangeDto |
| GET | `/api/v1/billing/execution-item` | 获取授权机构下的可执行条目信息 - 订单中的项目条目 | `findOrderItemPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); customerId (query, 選填, string); ids (query, 選填, array<string>); status (query, 選填, array<string>); keyword (query, 選填, string); orderId (query, 選填, string) |  | 200： PageExecutionItemDto |
| GET | `/api/v1/billing/execution-item/transfer` | 获取授权机构下的可执行条目转赠记录 | `findOrderItemPaged_1` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); giverId (query, 選填, string); receiverId (query, 選填, string); sourceClinicId (query, 選填, string); targetClinicId (query, 選填, string); status (query, 選填, string) |  | 200： PageItemTransferDto |
| GET | `/api/v1/billing/execution-record` | 获取授权机构下的客户项目执行数据 | `findExecutionRecordPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); customerId (query, 選填, string); cancelled (query, 選填, boolean); status (query, 選填, array<string>); itemIds (query, 選填, array<string>) |  | 200： PageExecutionRecordDto |
| GET | `/api/v1/billing/execution-record/{id}` | 获取授权机构下的客户项目执行数据 | `findExecutionRecord` | id (path, 必填, string) |  | 200： ExecutionRecordDto |
| GET | `/api/v1/billing/financial/billing-apportion` | 获取收退款分摊信息 | `paymentBillingApportion` | billingId (query, 選填, string) |  | 200： array<BillingApportionDto> |
| GET | `/api/v1/billing/financial/refund-order-billing-apportion` | 获取退款订单分摊信息 | `refundOrderBillingApportion` | refundOrderId (query, 必填, string) |  | 200： array<BillingApportionDto> |
| GET | `/api/v1/billing/payment` | 获取授权机构下的收银摘要数据 - 收银摘要列表 | `findPaymentPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); customerId (query, 選填, string); orderNumber (query, 選填, string); orderIds (query, 選填, array<string>); includeRefund (query, 選填, boolean) |  | 200： PagePaymentDetailDto |
| GET | `/api/v1/billing/payment-method` | 获取授权机构下的支付方式 | `findPaymentMethodAll` |  |  | 200： array<PaymentMethodDto> |
| GET | `/api/v1/billing/payment/{id}` | 获取授权机构下的收银摘要数据 - 收银详细信息 | `findPaymentById` | id (path, 必填, string) |  | 200： PaymentDetailDto |
| GET | `/api/v1/billing/refund` | 获取授权机构下的退款数据 - 退款列表 | `findRefund` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); customerId (query, 選填, string); status (query, 選填, array<string>); type (query, 選填, array<string>); bizType (query, 選填, string); withLinePayment (query, 選填, boolean) |  | 200： PageRefundDto |
| GET | `/api/v1/billing/refund/{id}` | 获取授权机构下的退款数据 - 单个退款 | `findRefundById` | id (path, 必填, string) |  | 200： RefundDto |
| GET | `/api/v1/billing/sales-order` | 获取授权机构下的销售订单摘要数据 - 订单摘要信息 | `findOrderPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); customerId (query, 選填, string); number (query, 選填, string); status (query, 選填, array<string>); type (query, 選填, array<string>); visitId (query, 選填, string) |  | 200： PageSalesOrderDto |
| GET | `/api/v1/billing/sales-order/{id}` | 根据订单ID获取销售订单详细数据 - 订单详细信息 | `findOrderById` | id (path, 必填, string) |  | 200： SalesOrderDetailDto |
| GET | `/api/v1/billing/sales-order/{id}/refund` | 根据订单ID获取销售订单退款详细数据 - 订单退款详细信息 | `findRefundByOrderId` | id (path, 必填, string) |  | 200： array<RefundDto> |
| GET | `/api/v1/billing/transfer` | 获取授权机构下转诊/转疗数据 | `findPagedTransferRecords` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); fromClinicId (query, 選填, string); toClinicId (query, 選填, string); customerId (query, 選填, string); type (query, 選填, string); status (query, 選填, array<string>) |  | 200： PageTransferRecordDto |
| POST | `/api/v1/account-item/balance/refund` | 储值金退款 | `accountRefund` |  | application/json： CreateAccountRefundParams | 200： IdDto |
| POST | `/api/v1/account-item/card/redeem` | 卡项确认品项 | `accountItemRedeem` |  | application/json： BundleItemRedeemParam | 200： array<AccProductItemDto> |
| POST | `/api/v1/account-item/card/redeem-revoke` | 卡项作废确认品项 | `accountItemRedeemRevoke` |  | application/json： BundleItemRedeemRevokeParam | 200 |
| POST | `/api/v1/account-item/reward/adjust` | 增值金余额调整 | `rewardAdjust` |  | application/json： BalanceAdjustParams | 200： AccountJournalEntryInfo |
| POST | `/api/v1/billing/customer/transfer/product-item` | 操作客户转疗（自动同意转疗） | `transferCustomerProductItem` |  | application/json： TransferCustomerProductItemReqParams | 201： IdDto |
| POST | `/api/v1/billing/esthetics/plan` | 获取客户美学方案 | `queryEstimatePlanPage` |  | application/json： QueryEstheticsPlanParams | 200： array<QueryEstheticsPlanProductDto> |
| POST | `/api/v1/billing/exchange/list-by-target-ids` | 换入订单ID查询换购记录 | `findByTargetOrderIds` | targetOrderIds (query, 必填, string) | application/json： string | 200： array<ExchangeDto> |
| POST | `/api/v1/billing/execution-record` | 在授权机构下创建项目执行记录数据 | `createExecutionRecord` |  | application/json： CreateExecutionParams | 201： IdDto |
| POST | `/api/v1/billing/execution-record/fulfillment/detail` | 查询执行记录的履约明细 | `fulfillmentDetail` |  | application/json： array<string> | 200： array<FulfillmentDetailDto> |
| POST | `/api/v1/billing/free-order` | 创建免单订单，创建后为支付完成，忽略所有审批流程 | `createFreeOrder` |  | application/json： CreateFreeOrderParams | 201： IdDto |
| POST | `/api/v1/billing/order/performance-allocation` | 订单业绩分配 | `orderPerformanceAllocation` |  | application/json： OrderPerformanceAllocationParams | 200： IdString |
| POST | `/api/v1/billing/order/refund` | 订单退款V2，仅支持原路退，忽略审批流程 | `orderRefundV2` |  | application/json： CreateRefundOrderParams | 200： IdString |
| POST | `/api/v1/billing/order/refund/v3` | 订单退款V3，支持统一退。忽略审批流程 | `orderRefundV3` |  | application/json： CreateRefundOrderParamsV3 | 200： IdString |
| POST | `/api/v1/billing/payment/discard` | 作废收款单 | `discardPayment` |  | application/json： BillingPaymentDiscardParam | 200 |
| POST | `/api/v1/billing/payment/list-signature` | 获取支付的签名图片（包含无有效签名结果） | `listBillingSignature` |  | application/json： ListBillingSignatureParams | 200： array<PaymentSignatureDto> |
| POST | `/api/v1/billing/prepaid-order` | 创建储值金订单，创建后为待支付订单，忽略所有审批流程 | `createPrepaidOrder` |  | application/json： CreatePrepaidOrderParams | 201： IdDto |
| POST | `/api/v1/billing/sales-order` | 创建销售订单，创建后为待支付订单，忽略所有审批流程 | `createOrder_1` |  | application/json： CreateSalesOrderParams | 201： IdDto |
| POST | `/api/v1/billing/sales-order/list-invoices` | 根据订单ID获取销售订单发票明细 | `findInvoiceByOrderId` |  | application/json： ListInvoiceParams | 200： array<SalesOrderInvoiceDto> |
| POST | `/api/v1/billing/sales-order/{id}/payment` | 销售订单支付，支付后为已支付订单，忽略所有审批流程 | `payOrder` | id (path, 必填, string) | application/json： PayOrderParam | 201： SalesOrderDetailDto |
| POST | `/api/v1/billing/sales-order/{id}/payment/by-line` | 销售订单分行支付，支付后为已支付订单，忽略所有审批流程 | `payOrderByLine` | id (path, 必填, string) | application/json： PayOrderByLineParam | 201： IdDto |
| POST | `/api/v1/billing/service-fee/order` | 根据订单ID查询服务费 | `findByOrderId` |  | application/json： ServiceFeeByOrderQueryParams | 200： array<ServiceFeeDto> |
| POST | `/api/v1/billing/service-fee/page` | 分页查询服务费 | `pageServiceFee` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) | application/json： ServiceFeeQueryParams | 200： PageServiceFeeDto |
| PUT | `/api/v1/billing/esthetics/order-relation` | 修改订单与美学规划关联关系 | `saveEstimateItemAndOrderLineRelation` |  | application/json： SaveEstimateOrderLineRelationParams | 204 |
| PUT | `/api/v1/billing/execution-record/cancel` | 作废执行记录 | `cancel` |  | application/json： RevokeCancelExecutionParams | 204： ExecutionRecordRevokeResult |
| PUT | `/api/v1/billing/execution-record/revoke` | 撤回执行记录 | `revoke` |  | application/json： RevokeCancelExecutionParams | 204： ExecutionRecordRevokeResult |
| DELETE | `/api/v1/billing/sales-order/{id}` | 销售订单废弃，未支付订单可废弃，废弃后订单不可操作 | `cancelOrder` | id (path, 必填, string) |  | 204 |

### 07. 市场营销集成

获取API访问所需要的市场营销数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/market/card` | 查询授权机构下的卡项信息 | `findCardPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 必填, string); keyword (query, 選填, string); status (query, 選填, string); liveShowFilter (query, 選填, boolean) |  | 200： PageFusionCardDto |
| GET | `/api/v1/market/card/prompt` | 根据条件查询可用卡项信息 | `findUsableCardPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); customerId (query, 必填, string); clinicId (query, 必填, string); keyword (query, 選填, string); orderTypes (query, 選填, array<string>) |  | 200： PageFusionCardDto |
| GET | `/api/v1/market/card/{id}` | 精确获取授权机构下的卡项信息 | `loadCard` | id (path, 必填, string) |  | 200： FusionCardDto |
| GET | `/api/v1/market/coupon` | 获取授权机构下的优惠券信息 | `findCouponPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); type (query, 必填, string); clinicId (query, 選填, string); keyword (query, 選填, string); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); status (query, 選填, string) |  | 200： PageCouponDto |
| GET | `/api/v1/market/coupon/{id}` | 精确获取授权机构下的优惠券信息 | `loadCoupon` | id (path, 必填, string) |  | 200： CouponDetailDto |
| GET | `/api/v1/market/promotion` | 获取授权机构下的促销信息 | `findPromotionPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); type (query, 選填, string); status (query, 選填, string); minPrice (query, 選填, number); maxPrice (query, 選填, number); keyword (query, 選填, string); liveShowFilter (query, 選填, boolean) |  | 200： PagePromotionDto |
| GET | `/api/v1/market/promotion/{id}` | 根据ID获取促销信息 | `loadPromotion` | id (path, 必填, string) |  | 200： PromotionDto |
| POST | `/api/v1/market/promotion/active` | 促销启用/停用 | `activePromotion` |  | application/json： SalesPromotionActiveParam | 204 |

### 08. 库存物料集成

获取API同步供应链数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/inventory/change-type/{bizType}` | 获取授权机构下出/入库类别，bizType参数: stock-in(入库), stock-out(出库) | `findChangeType` | bizType (path, 必填, string) |  | 200： array<ChangeTypeDto> |
| GET | `/api/v1/inventory/outbound/all` | 获取提货单信息 - 翻页 | `getPagedOutboundRequisition` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); organizationId (query, 選填, string); customerId (query, 選填, string); orderTimeStart (query, 選填, string(date-time)); orderTimeEnd (query, 選填, string(date-time)) |  | 200： PageOutboundRequisitionInfoDto |
| GET | `/api/v1/inventory/purchaseOrder` | 物资采购订单 | `purchaseOrder` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); id (query, 選填, string); supplierId (query, 選填, string); status (query, 選填, string) |  | 200： PagePurchaseOrderDto |
| GET | `/api/v1/inventory/stock-item` | 获取授权机构下的所有库存条目信息 | `findStockItemPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); categoryId (query, 選填, string); branchId (query, 選填, string); warehouseId (query, 選填, string); hasStock (query, 選填, boolean); isDrug (query, 選填, boolean); isShortage (query, 選填, boolean); isEnabled (query, 選填, boolean); keyword (query, 選填, string); ids (query, 選填, array<string>) |  | 200： PageStockItemDto |
| GET | `/api/v1/inventory/stock-item/stock-in` | 物料入库记录 | `findStockInRecords` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); warehouseId (query, 選填, string); isPharmacy (query, 選填, boolean); supplierId (query, 選填, string); categoryIds (query, 選填, array<string>); id (query, 選填, string); includeRollback (query, 選填, boolean); changeTypeCode (query, 選填, string); number (query, 選填, string) |  | 200： PageStockInOrderDto |
| GET | `/api/v1/inventory/stock-item/stock-out` | 物料出库记录 | `findStockOutRecords` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); warehouseId (query, 選填, string); isPharmacy (query, 選填, boolean); supplierId (query, 選填, string); categoryIds (query, 選填, array<string>); id (query, 選填, string); includeRollback (query, 選填, boolean); changeTypeCode (query, 選填, string); number (query, 選填, string); takeUserId (query, 選填, string); customerId (query, 選填, string) |  | 200： PageStockOutOrderDto |
| GET | `/api/v1/inventory/stock-item/transfer` | 物料调拨记录 | `findStockTransferRecords` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); id (query, 選填, string); number (query, 選填, string); isPharmacy (query, 選填, boolean); fromWarehouseId (query, 選填, string); toWarehouseId (query, 選填, string) |  | 200： PageStockTransferOrderDto |
| GET | `/api/v1/inventory/supplier` | 获取供应商信息 - 翻页 | `pageSupplier` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageSupplierDto |
| GET | `/api/v1/inventory/warehouse` | 获取授权机构下的所有库房信息 | `listAllWarehouse` |  |  | 200： array<WarehouseDto> |
| POST | `/api/v1/inventory/stock-item/stock-in` | 物料入库操作 | `stockInItem` |  | application/json： StockInParams | 200： IdDto; 201： IdDto |
| POST | `/api/v1/inventory/stock-item/stock-out` | 物料出库操作 | `stockOutItem` |  | application/json： StockOutParams | 200： IdDto; 201： IdDto |
| POST | `/api/v1/inventory/stock-item/transfer` | 物料库存调拨 | `transferItem` |  | application/json： StockTransferParams | 200： IdDto; 201： IdDto |
| DELETE | `/api/v1/inventory/stock-item/stock-in/{id}` | 作废物料入库记录 | `revokeStockIn` | id (path, 必填, string) |  | 200： IdDto; 204 |
| DELETE | `/api/v1/inventory/stock-item/stock-out/{id}` | 作废物料出库记录 | `revokeStockOut` | id (path, 必填, string) |  | 200： IdDto; 204 |
| DELETE | `/api/v1/inventory/stock-item/transfer/{id}` | 作废物料调拨记录 | `revokeStockTransfer` | id (path, 必填, string) |  | 200： IdDto; 204 |

### 10. 业务事件订阅

订阅业务变更数据，用以支持三方集成近实时同步/通知

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/event/event-history` | 获取历史事件分页列表 | `pageEventHistory` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); startTime (query, 必填, string(date-time)); endTime (query, 選填, string(date-time)); topics (query, 選填, array<string>) |  | 200： PageEventHistoryDto |
| GET | `/api/v1/event/event-history/single-entity` | 获取特定业务实体对应的历史事件列表 | `pageEventHistory_1` | bizEntityId (query, 必填, string) |  | 200： array<EventHistoryDto> |
| GET | `/api/v1/event/subscribe` | 获取当前订阅列表 | `subscribeTopics_1` |  |  | 200： array<TopicSubscriptionDto> |
| GET | `/api/v1/event/topic` | 获取当前系统支持的事件主题 | `listSupportedTopics` |  |  | 200： array<EventTopicDto> |
| POST | `/api/v1/event/subscribe` | 订阅系统业务事件主题，结果返回当前订阅 | `subscribeTopics` |  | application/json： CreateSubscriptionParams | 201： TopicSubscriptionDto |
| POST | `/api/v1/event/unsubscribe/{id}` | 取消订阅系统业务事件主题 | `unsubscribeTopics` | id (path, 必填, string) |  | 202： TopicSubscriptionDto |

### 11. 电子健康档案

获取API同步医疗电子健康档案数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/ehr/prescription` | 获取授权机构下的处方数据 | `findPrescriptionPaged` | page (query, 選填, integer(int32)); size (query, 選填, integer(int32)); start (query, 選填, string(date-time)); end (query, 選填, string(date-time)); clinicId (query, 選填, string); patientId (query, 選填, string); type (query, 選填, string) |  | 200： PagePrescriptionDto |
| GET | `/api/v1/ehr/prescriptionNew` | 获取授权机构下的新版本医嘱服务的处方数据 | `findPrescriptionNewPaged` | clinicId (query, 必填, string); page (query, 必填, integer(int32)); size (query, 必填, integer(int32)); start (query, 必填, string(date-time)); end (query, 必填, string(date-time)) |  | 200： PageSupervisionDataOrderDto |
| GET | `/api/v1/ehr/queryAdvicesOrderList` | 获取授权机构下医嘱服务的医嘱数据 | `queryAdvicesOrderList` | clinicId (query, 選填, string); orderNoList (query, 選填, array<string>); page (query, 必填, integer(int32)); size (query, 必填, integer(int32)); start (query, 必填, string(date-time)); end (query, 必填, string(date-time)) |  | 200： PageSupervisionAdvicesOrderDto |
| GET | `/api/v1/ehr/queryAdvicesOrderListByPatientId` | 获取授权机构下客户的医嘱服务的医嘱数据 | `queryAdvicesOrderListByPatientId` | patientId (query, 選填, string); orderNoList (query, 選填, array<string>) |  | 200： array<SupervisionAdvicesOrderDto> |
| GET | `/api/v1/ehr/queryMedicalRecordDetail` | 获取授权机构下医嘱服务的病历数据明细 | `queryMedicalRecordDetail` | medicalRecordNo (query, 選填, string) |  | 200： PatientMedicalRecordDto |
| GET | `/api/v1/ehr/queryMedicalRecordList` | 获取授权机构下医嘱服务的病历数据 | `queryMedicalRecordList` | clinicId (query, 必填, string); page (query, 必填, integer(int32)); size (query, 必填, integer(int32)); start (query, 必填, string(date-time)); end (query, 必填, string(date-time)) |  | 200： PageMedicalRecordPatientListDto |
| GET | `/api/v1/ehr/queryMedicalRecordListByPatientId` | 获取授权机构下客户的医嘱服务的病历数据 | `queryMedicalRecordListByPatientId` | patientId (query, 選填, string) |  | 200： array<MedicalRecordPatientListDto> |
| POST | `/api/v1/ehr/care-plan` | 在授权机构下的创建患者诊疗计划 | `createCarePlan` |  | application/json： CreateCarePlanParams | 201： IdDto |

### 12. 云晰系统集成

云晰直播业务流程集成定制接口

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| POST | `/api/v1/integration/yunxi/create-order` | 多品项开单，按品项拆分多个订单，成功后为已支付订单，忽略所有审批流程 | `createOrder` |  | application/json： YunxiCreateOrderParams | 200： YunxiCreateOrderResponse; 400： YunxiCreateOrderResponse |
| POST | `/api/v1/integration/yunxi/fulfillment` | 单订单（单品项）核销状态同步 | `fulfillment` |  | application/json： YunxiFulfillmentParams | 200： GeneralYunxiResponse; 400： GeneralYunxiResponse |
| POST | `/api/v1/integration/yunxi/refund` | 单订单（单品项）全部或部分退款 | `refund` |  | application/json： YunxiRefundOrderParams | 200： GeneralYunxiResponse; 400： GeneralYunxiResponse |

### X1. 业务报表数据

API获取核心报表数据，用以支持三方集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/analytic/cash/performance/page` | 查询员工销售业绩数据 | `findCashPerformancePage` | startDate (query, 必填, string(date-time)); endDate (query, 選填, string(date-time)); performanceOrganizationId (query, 選填, string); roleCodes (query, 選填, array<string>); employeeId (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageEmployeeCashPerformanceDto |
| GET | `/api/v1/analytic/execution/performance/page` | 查询员工执行业绩数据 | `findExecutionPerformancePage` | startDate (query, 必填, string(date-time)); endDate (query, 選填, string(date-time)); performanceOrganizationId (query, 選填, string); roleCodes (query, 選填, array<string>); employeeId (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageEmployeeExecutionPerformanceDto |
| GET | `/api/v1/analytic/financial/accountDealing/page` | 查询往来账数据 | `findPage` | startDate (query, 必填, string(date-time)); endDate (query, 必填, string(date-time)); fromStoreId (query, 選填, string); toStoreId (query, 選填, string); customerId (query, 選填, string); page (query, 選填, integer(int32)); size (query, 選填, integer(int32)) |  | 200： PageAccountDealingDto |

### X2. SCRM集成服务

通过API与SCRM进行集成

| Method | Path | Summary | OperationId | Params | Request | Responses |
| --- | --- | --- | --- | --- | --- | --- |
| GET | `/api/v1/scrm/wechat-fan` | 查询授权机构下的微信公众号粉丝 | `queryWechatBindings` | appId (query, 必填, string); openId (query, 必填, string) |  | 200： array<SimpleBinding> |
| POST | `/api/v1/scrm/proxy` | scrm服务代理 | `proxy` |  | application/json： ScrmGatewayParams | default： ScrmResult |
| POST | `/api/v1/scrm/wechat-fan/bind` | 在授权机构下绑定微信公众号粉丝 | `createWechatFanBinding` |  | application/json： CreateBindingParams | 201： SimpleBinding |
