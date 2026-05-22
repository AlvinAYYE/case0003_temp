# external_integration 任務列表

## 模組目標

隔離第三方診所系統、LINE、三竹 API schema 與錯誤轉換。此模組不包含核心 domain 規則，只提供 gateway adapter、錯誤轉換、request log 與測試替身。

## 依賴邊界

- Domain 與 application service 只依賴 gateway port，不依賴 adapter 實作。
- Adapter 可依賴環境變數、HTTP client、credential provider 與 `ApiRequestLogRepository`。
- 外部 API 欄位、錯誤碼、URL、token 規格未確認前，只能建立 port、fake adapter 與待確認 contract test。

## 最小可執行任務

- [ ] EI-01 建立 `external_integration` app 邊界與目錄：`ports`、`adapters`、`errors`、`logging`、`tests`。
- [ ] EI-02 定義 `GatewayError`、`GatewayTimeoutError`、`GatewayAuthError`、`GatewayValidationError`、`GatewayConflictError` 與 `RequestTraceId`。
- [ ] EI-03 定義 `ExternalRequestLog` DTO，保存 provider、operation、trace id、status、duration、錯誤摘要，不保存完整敏感 payload。
- [ ] EI-04 定義 `LineLoginGateway` port：驗證 LIFF / LINE Login token，取得可信 LINE User ID。
- [ ] EI-05 定義 `LineMessagingGateway` port：發送預約成功通知與行前提醒，回傳 LINE request id 與錯誤摘要。
- [ ] EI-06 定義 `SmsOtpGateway` port：發送 OTP，處理 provider response 摘要。
- [ ] EI-07 定義 `ClinicAuthGateway` port：取得與刷新第三方診所系統 API token。
- [ ] EI-08 定義 `ClinicCustomerGateway` port：依手機查客戶、建立客戶、讀取客戶基本資料。
- [ ] EI-09 定義 `ClinicDirectoryGateway` port：讀取分店、醫師、科別或主檔。
- [ ] EI-10 定義 `ClinicTreatmentGateway` port：讀取分店可預約療程或服務項目。
- [ ] EI-11 定義 `ClinicSchedulingGateway` port：讀取醫師排班、休診、指定區間既有預約。
- [ ] EI-12 定義 `ClinicAppointmentGateway` port：建立正式預約、查預約列表、查單筆預約。
- [ ] EI-13 視第三方能力定義可選 `ClinicEventGateway` port；未確認前不得假設 webhook 存在。
- [ ] EI-14 建立 fake adapters，支援 domain / application service test 不連外執行。
- [ ] EI-15 實作 request log decorator / middleware，統一記錄 timeout、credential 錯誤、外部錯誤碼與 trace id。
- [ ] EI-16 實作 adapter 錯誤轉換規則，避免 provider schema 外洩到其他模組。
- [ ] EI-17 正式文件到位後，為每個 provider 補 contract test fixture，再實作真實 adapter。

## 測試清單

- [ ] 每個 gateway port 都有 fake adapter 可供 service test 使用。
- [ ] timeout 被轉為 `GatewayTimeoutError`。
- [ ] credential / token 失效被轉為 `GatewayAuthError`。
- [ ] 同時搶位或時段衝突可轉為 `GatewayConflictError`，實際錯誤碼待第三方確認。
- [ ] request log 保存 trace id、provider、operation、duration 與錯誤摘要。
- [ ] request log 不保存完整手機、OTP、token、密碼或完整外部 payload。
- [ ] adapter contract test 不依賴正式環境，除非 sandbox 與測試帳號已確認。

## 待確認不可自行補完

- [ ] 第三方診所系統正式產品名稱、API 文件版本、base URL、sandbox 與測試帳號。
- [ ] 第三方 token 取得、刷新與過期規格。
- [ ] 第三方所有 request / response 欄位與錯誤碼。
- [ ] LINE Channel、LIFF 與 Messaging API 權限。
- [ ] 三竹正式 endpoint、編碼、測試方式與供應商回應格式。

