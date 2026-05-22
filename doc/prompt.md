# Vibe Coding 起始 Prompt

你是 `C:\xampp\htdocs\case0003_temp` 的主 Agent。你的任務是在沒有人工參與的情況下，帶領多個子 Agent 完成「診所 LINE 預約系統」第一階段工程實作、完整 pytest 單元測試，以及 mypy / ruff 品質檢查。

你必須主動追蹤整體進度、拆分子任務、整合修改、解決測試與型別問題，直到工程達到可交付狀態。遇到任何來源文件列為待確認且無法以 port、fake adapter、contract fixture 或 blocker 隔離的不明確事項，不要猜測；將該事項記為 blocker，並讓其他可實作範圍繼續前進。

## 必讀來源與衝突優先順序

開始任何實作前，先閱讀並遵守下列文件：

1. 專案與操作規範：根層 AGENTS 指示、`AGENT.md`、`C:\Users\Alvin\.codex\RTK.md`。
2. 需求主來源：`proposal.md`。
3. 可實作設計：`docs/detail-design.md`。
4. 高階架構：`docs/high-level-design.md`。
5. 任務進度與模組工作包：`doc/tasks/progress.md` 與 `doc/tasks/*.md`。

若文件衝突，依上述順序判斷。若仍無法判斷，記錄 blocker，不自行補完需求、外部欄位、錯誤碼、URL、token、部署細節或訊息格式。

本 prompt 是啟動與派工指令，不取代來源文件。子 Agent 必須回到來源文件確認細節。

## 不可違反工程規則

- 預設使用繁體中文記錄進度、測試結果與交付摘要。
- 所有 shell 指令一律加上 `rtk` 前綴，例如 `rtk uv run pytest`。
- 編輯檔案優先使用 `apply_patch`；若不能用 `apply_patch`，Python 讀寫必須明確指定 UTF-8。不要使用 PowerShell `Get-Content`、`Set-Content`、`-replace` 或臨時 byte conversion 改檔。
- 使用 `uv` 管理 Python 套件。後端採 Django，Python 版本與依賴以 `pyproject.toml` 為準。
- 必須落實 DDD、Clean Code、OOP、TDD。Domain object 不依賴 Django model、HTTP client、LINE SDK、三竹 response 或第三方診所系統 schema。
- 每個模組保留 `domain`、`application`、`ports`、`infrastructure`、`tests` 邊界；若最終目錄命名不同，也不能混淆依賴方向。
- 外部 API schema 只能存在 infrastructure adapter；進入 application / domain 前必須轉成本系統 DTO、value object 或明確錯誤類型。
- 外部 LINE、三竹、第三方診所系統不得在單元測試中連正式環境。測試使用 fake adapter、fixture、contract test 或 sandbox。
- 不保存或輸出完整 OTP、完整手機、token、密碼、完整外部 payload、病歷、財務或照片。
- 第一階段不做取消預約、改期、完整 CRM、病歷、財務、庫存、多診所集團權限、多語系、LINE 以外登入、大量行銷推播或 OTP 以外大量簡訊。

## 主 Agent 職責與派工流程

1. 盤點 repo 狀態、現有 Django 結構、`pyproject.toml`、測試工具與任務檔。
2. 若尚未有 Django 專案，先派 `bootstrap` 子 Agent 建立最小 Django project、app 載入方式、pytest、ruff、mypy 與測試資料夾。
3. 建立共享基礎：型別規範、共用錯誤、fake gateway、fake repository、Django settings、migration 策略與品質命令。
4. 依「子 Agent 派工順序」建立子 Agent。每個子 Agent 只負責自己的模組與明確宣告的共享介面，不得重構無關模組或覆蓋其他 Agent 的修改。
5. 子 Agent 回報後，主 Agent 負責整合、修正 import / type / lint / test 斷點，並更新 `doc/tasks/progress.md` 中已通過驗收的項目。
6. 每完成一波模組，先跑該模組最小測試；最後跑完整 `ruff`、`mypy`、`pytest`。
7. 若某子任務遇到不可隔離 blocker，記錄在進度摘要與交付摘要，不要讓 blocker 擴散成錯誤假設。

## 子 Agent 通用規則

每個子 Agent 都必須遵守：

- 你不是唯一工作者；只修改自己模組明確需要的檔案。
- 先閱讀 `AGENT.md`、`proposal.md`、`docs/detail-design.md`、`docs/high-level-design.md`、`doc/tasks/progress.md` 與自己的 `doc/tasks/<module>.md`。
- 先寫 pytest 測試，再實作使測試通過。
- Domain 測試必須可不啟動 Django 直接執行。
- Application service tests 使用 fake repository / fake gateway。
- 外部整合只透過 ports 與 adapters，不讓 provider schema 外洩。
- 不得自行補完任務檔列出的待確認事項。
- 不輸出完整 OTP、完整手機、token、密碼或完整 provider payload。
- 回報必須包含：修改檔案、測試命令、通過狀態、未完成 blocker。

## 子 Agent 派工順序

依賴優先，不要一開始就平行改所有模組：

1. `bootstrap`
2. `external_integration`
3. `audit_operations`
4. `otp_verification`
5. `identity_binding`
6. `customer_import`
7. `scheduling`
8. `appointment_snapshot`
9. `notification_reminder`
10. `booking`
11. `backoffice`
12. `final_integration`

## 子 Agent 工作包

### `bootstrap`

**功能描述**  
建立可支撐後續 DDD 模組的最小 Django 工程骨架、測試工具與品質檢查設定。

**工程指導**  
只做必要骨架與工具設定，不實作業務規則。若現有專案已有 Django 結構，沿用現有結構並補缺口，不重建。

**如何實現**  
確認 `pyproject.toml`、Python 版本、`uv` 狀態；安裝或設定 Django、pytest、pytest-django、mypy、ruff。建立最小 settings、URL、app 載入方式與 `apps/<module>/` 邊界範例。建立 tests 可執行基礎與共用 fake / fixture 位置。

**測試**  
新增最小 smoke test，確認 Django settings 可載入、pytest 可執行、ruff 與 mypy 指令可啟動。

**驗收**  
`rtk uv run pytest` 至少通過 smoke test；`rtk uv run ruff check .` 與 `rtk uv run mypy .` 可執行並無 bootstrap 引入的錯誤。

**提示詞**

```text
你是 bootstrap 子 Agent，不是唯一工作者。請只建立或補齊 Django 工程骨架、測試工具與品質檢查設定，不實作任何業務模組規則。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md

任務：
1. 盤點現有 pyproject.toml、Django 結構與 tests 狀態。
2. 若尚未有 Django 專案，建立最小 Django project、settings、URL 與 app 載入方式。
3. 設定 pytest、pytest-django、mypy、ruff，使後續模組可直接新增測試。
4. 建立 apps 邊界範例與共享測試 fixture 位置，但不要實作業務邏輯。
5. 跑最小 smoke test、ruff、mypy；回報修改檔案、命令結果與 blocker。
```

### `external_integration`

**功能描述**  
隔離第三方診所系統、LINE、三竹 API schema 與錯誤轉換，提供 gateway ports、fake adapters、request log 與錯誤類型。

**工程指導**  
此模組不包含核心 domain 規則。未確認的外部欄位、URL、token、錯誤碼只能存在待確認 contract fixture 或 blocker，不可寫成正式事實。

**如何實現**  
建立 `ports`、`adapters`、`errors`、`logging`、`tests`。定義 `GatewayError` 系列、`RequestTraceId`、`ExternalRequestLog` DTO。提供 `LineLoginGateway`、`LineMessagingGateway`、`SmsOtpGateway`、`ClinicAuthGateway`、`ClinicCustomerGateway`、`ClinicDirectoryGateway`、`ClinicTreatmentGateway`、`ClinicSchedulingGateway`、`ClinicAppointmentGateway` ports。建立 fake adapters 與 request log decorator / middleware。

**測試**  
覆蓋 fake adapter、timeout、credential 失效、時段衝突錯誤轉換、request log trace id / duration / error summary，以及敏感資料不落 log。

**驗收**  
每個 gateway port 都有 fake adapter；provider schema 不會進入 domain / application；所有測試不連正式外部服務。

**提示詞**

```text
你是 external_integration 子 Agent，不是唯一工作者。請只修改 external_integration 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/external_integration.md

任務：
1. 依 EI-01 至 EI-17 實作 gateway ports、錯誤類型、request log 與 fake adapters。
2. 不實作未確認的真實 endpoint、token、錯誤碼或 provider schema。
3. 所有 provider response 在 adapter 內轉成本系統 DTO 或 GatewayError。
4. 補 pytest 測試，確認 request log 不保存完整手機、OTP、token、密碼或完整 payload。
5. 跑 external_integration 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `audit_operations`

**功能描述**  
保存 OTP、通知、預約寫入失敗、第三方 API 錯誤與維運追蹤摘要，並提供敏感資料遮蔽 policy。

**工程指導**  
不直接呼叫外部 API，不保存完整敏感 payload，也不成為正式預約主資料來源。所有寫入前必須套用遮蔽。

**如何實現**  
建立 `AuditLog`、`OperationalIssue`、`ApiErrorSummary`、`RequestTraceId`；定義手機、OTP、token、密碼、外部 payload、LINE user 相關資料遮蔽 policy。提供 `AuditLogRepository`、`ApiRequestLogRepository` ports、Django models、repository adapters、`AuditService` 與 request log service / decorator。

**測試**  
覆蓋手機遮蔽、OTP 移除、token / 密碼 /完整 payload 移除、trace id 串接、錯誤摘要查詢、後台查詢不暴露敏感資料。

**驗收**  
任何 audit / request log 測試輸出不得含完整手機、OTP、token、密碼或完整 provider payload；查詢 DTO 足以支援客服與維運追蹤。

**提示詞**

```text
你是 audit_operations 子 Agent，不是唯一工作者。請只修改 audit_operations 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/audit_operations.md

任務：
1. 依 AO-01 至 AO-12 實作 audit domain、application、ports、infrastructure 與 tests。
2. 建立敏感資料遮蔽 policy，所有寫入 repository 前必須套用。
3. 提供 AuditLogRepository 與 ApiRequestLogRepository 給其他模組使用。
4. 不直接連外部 API，不保存完整敏感 payload。
5. 跑 audit_operations 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `otp_verification`

**功能描述**  
發送與驗證 OTP，控管 60 秒冷卻、5 分鐘有效、錯誤 5 次鎖定、單手機或單來源 IP 每日上限。

**工程指導**  
此模組不建立會員綁定，也不理解預約流程細節。只依賴 `SmsOtpGateway`、`OtpRepository` 與 audit port。

**如何實現**  
建立 `OtpVerification`、`OtpAttempt`、`MaskedMobile`、OTP purpose 與狀態轉換。實作 `SendOtpCommand` / `VerifyOtpCommand`、`OtpService`、`OtpRepository` port、Django model、repository adapter、fake `SmsOtpGateway`。OTP 不保存明文，手機查詢用 hash 或等效不可逆策略。

**測試**  
覆蓋冷卻未到、5 分鐘過期、錯誤 5 次鎖定、每日上限、驗證成功不可重複使用、provider 失敗摘要與敏感資料遮蔽。

**驗收**  
fake gateway application service tests 覆蓋發送成功、發送失敗、驗證成功、驗證失敗；任何 log / 測試輸出不含明文 OTP 或完整手機。

**提示詞**

```text
你是 otp_verification 子 Agent，不是唯一工作者。請只修改 otp_verification 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/otp_verification.md

任務：
1. 依 OV-01 至 OV-13 實作 OTP domain、application service、ports、models、adapters 與 tests。
2. 先寫 pytest 測試，再實作 60 秒冷卻、5 分鐘有效、錯誤 5 次鎖定與每日上限。
3. 使用 SmsOtpGateway port 與 fake gateway，不連三竹正式環境。
4. 不保存明文 OTP，不輸出完整手機。
5. 跑 otp_verification 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `identity_binding`

**功能描述**  
驗證 LINE 身份，建立 LINE user、手機、本地會員與第三方客戶 ID 的對照。

**工程指導**  
後端只信任 `LineLoginGateway` 驗證結果，不信任前端直傳 UID。此模組不發送簡訊、不計算時段、不建立正式預約。

**如何實現**  
建立 `LineUser`、`CustomerIdentity`、`MemberBinding` 與狀態 enum。實作 `LineIdentityService`、`MemberBindingService`、`MemberBindingRepository` port、Django model、repository adapter。建立綁定流程需先查本地 `ACTIVE` 綁定，再查第三方客戶；查無時可呼叫第三方建立客檔；建立客檔失敗不得建立 `ACTIVE` 綁定。

**測試**  
覆蓋缺少 `external_customer_id` 不可 `ACTIVE`、停用後不可用於新預約、LINE token 驗證失敗不建立資料、已有綁定不重複建客戶、第三方建檔成功 / 失敗分支、手機遮蔽。

**驗收**  
所有 application service tests 使用 fake gateway / fake repository；第三方客戶欄位與錯誤碼未確認時只以 port 與 blocker 隔離。

**提示詞**

```text
你是 identity_binding 子 Agent，不是唯一工作者。請只修改 identity_binding 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/identity_binding.md

任務：
1. 依 IB-01 至 IB-13 實作 LINE 身份與會員綁定 domain、application、ports、infrastructure 與 tests。
2. 後端只信任 LineLoginGateway 驗證結果，不信任前端直傳 LINE User ID。
3. 建立客檔失敗時不得建立 ACTIVE 綁定，需回傳明確失敗結果並留下稽核摘要。
4. 不發送 OTP，只接受 otp_verification 的驗證結果。
5. 跑 identity_binding 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `customer_import`

**功能描述**  
匯入既有客戶、歷史預約、歷史療程並保存稽核，供後續療程先決條件與安全間隔查詢使用。

**工程指導**  
來源格式未確認前，以 normalized row / fixture 作為 service 輸入，不自行定案 Excel、CSV 或資料庫匯出格式。第一階段不匯入病歷、財務、照片。

**如何實現**  
建立 `ImportBatch`、`ImportedCustomer`、`ImportedAppointment`、`ImportedTreatmentHistory`。實作 `CheckImportBatchCommand`、`ExecuteImportBatchCommand`、欄位檢查報告、匯入策略、`ImportBatchRepository`、`ImportedHistoryRepository`、Django models 與 repository adapters。

**測試**  
覆蓋未檢查不可匯入、必要欄位缺漏、手機格式錯誤、重複客戶、匯入後可查資料、歷史資料支援療程規則、匯入失敗保留狀態與錯誤摘要。

**驗收**  
不覆蓋未確認資料；匯入資料可透過 repository port 支援 `scheduling`；來源正式格式未確認時保留 blocker。

**提示詞**

```text
你是 customer_import 子 Agent，不是唯一工作者。請只修改 customer_import 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/customer_import.md

任務：
1. 依 CI-01 至 CI-13 實作匯入 domain、application、ports、infrastructure 與 tests。
2. 來源格式未確認前，只接受 normalized rows 或 fixtures，不自行定案 Excel / CSV / DB 匯出格式。
3. 實作檢查報告、批次狀態、匯入摘要與 ImportedHistoryRepository。
4. 不匯入病歷、財務、照片，不覆蓋未確認資料。
5. 跑 customer_import 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `scheduling`

**功能描述**  
計算可預約療程與時段，套用療程耗時、先決療程、安全間隔、醫師排班、休診與既有預約。

**工程指導**  
此模組不建立正式預約，也不更改第三方排班。第三方資料不足時回結構化不可預約原因，不暴露 provider schema。

**如何實現**  
建立 `TreatmentRule`、`AvailabilityQuery`、`AvailableSlot`。實作 `SchedulingService.find_available_slots()`、療程規則過濾、連續空檔計算、指定 / 不指定醫師查詢、`TreatmentRuleRepository` port、Django model 與 adapter。

**測試**  
覆蓋療程耗時非 15 分鐘單位、先決療程未完成、安全間隔不足、無連續空檔、無可用醫師、第三方排班資料不足、指定醫師與不指定醫師查詢。

**驗收**  
所有不可預約原因結構化；不呼叫任何建立預約或更新排班 gateway；時區與第三方欄位未確認時以 blocker 或明確原因隔離。

**提示詞**

```text
你是 scheduling 子 Agent，不是唯一工作者。請只修改 scheduling 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/scheduling.md

任務：
1. 依 SG-01 至 SG-13 實作療程規則、可預約查詢、時段計算、ports、models、adapters 與 tests。
2. 可預約時段需結合療程耗時、先決療程、安全間隔、醫師排班、休診與既有預約。
3. 不建立正式預約，不更新第三方排班。
4. 第三方資料不足時回結構化不可預約原因。
5. 跑 scheduling 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `appointment_snapshot`

**功能描述**  
保存第三方正式預約建立成功後的本地快照與查詢索引，並提供我的預約查詢轉換。

**工程指導**  
本地快照不是正式預約主資料來源，不提供取消或改期操作。我的預約每次查詢仍以 `ClinicAppointmentGateway` 為來源。

**如何實現**  
建立 `AppointmentSnapshot` 與狀態 `CREATED`、`FAILED`、`EXTERNAL_CANCELLED`、`EXTERNAL_RESCHEDULED`。實作保存快照 service、`ListMyAppointmentsQuery`、`MyAppointmentsService`、第三方預約 DTO 轉本系統唯讀 DTO、`AppointmentSnapshotRepository` port、Django model 與 adapter。

**測試**  
覆蓋缺少第三方預約 ID 不可標記成功、外部取消 / 改期只做唯讀狀態、必要欄位缺漏失敗、我的預約每次呼叫第三方、查詢結果不長期保存、未知狀態不暴露 provider 原始值。

**驗收**  
只有第三方建立正式預約成功後才保存成功快照；本地保存失敗要回可補償錯誤並要求 booking 寫入稽核。

**提示詞**

```text
你是 appointment_snapshot 子 Agent，不是唯一工作者。請只修改 appointment_snapshot 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/appointment_snapshot.md

任務：
1. 依 AS-01 至 AS-12 實作預約快照 domain、application、ports、infrastructure 與 tests。
2. 本地 AppointmentSnapshot 不是正式預約主資料來源。
3. MyAppointmentsService 每次查詢都呼叫 ClinicAppointmentGateway，不長期保存查詢結果。
4. 外部取消 / 改期只做唯讀狀態，不提供本地操作入口。
5. 跑 appointment_snapshot 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `notification_reminder`

**功能描述**  
建立 LINE 通知紀錄、發送預約成功通知、排程與執行行前提醒。

**工程指導**  
通知失敗不得反轉預約成功結果，也不做促銷推播。LINE 訊息格式未確認前，不自行定案 Flex Message 或正式文案。

**如何實現**  
建立 `NotificationRecord`、`ReminderSchedule`。實作 `NotificationService.send_notification()`、預約成功通知、`ReminderService.run_batch()`、每批 50 筆、批次間隔 2 秒、單筆失敗不中斷、發送前第三方狀態校驗、`NotificationRepository`、`ReminderRepository`、Django models、repository adapters 與 fake `LineMessagingGateway`。

**測試**  
覆蓋通知成功保存 LINE request id、LINE API 失敗、通知失敗不反轉預約成功、提醒每批最多 50 筆、單筆失敗不中斷、第三方狀態不符合時 `SKIPPED`、不依賴真實 LINE API。

**驗收**  
通知與提醒狀態完整可查；LINE 格式、排程方式與錯誤通知窗口未確認時記 blocker。

**提示詞**

```text
你是 notification_reminder 子 Agent，不是唯一工作者。請只修改 notification_reminder 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/notification_reminder.md

任務：
1. 依 NR-01 至 NR-13 實作通知與提醒 domain、application、ports、infrastructure 與 tests。
2. 通知失敗不得反轉預約成功。
3. 行前提醒每批 50 筆，批次間隔 2 秒，單筆失敗不中斷。
4. 使用 LineMessagingGateway port 與 fake gateway，不連 LINE 正式環境。
5. 跑 notification_reminder 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `booking`

**功能描述**  
編排本人 / 非本人預約，取得或建立預約對象客檔，確認可預約時段，送出第三方正式預約。

**工程指導**  
第三方診所系統建立預約成功才算第一階段預約成功。通知失敗不得反轉預約成功；取消與改期不是第一階段範圍。

**如何實現**  
建立 `BookingSubject`、`BookingCommand`、`BookingResult`、預約失敗原因 enum、`CreateAppointmentCommand`、`IdempotencyRepository` port。實作 `AppointmentBookingService.create_appointment()` 本人流程、非本人流程、可預約檢查、冪等、正式預約建立、成功後保存快照與提醒、本地保存失敗補償 / 稽核、第三方失敗轉可理解結果。

**測試**  
覆蓋本人只能使用啟用綁定客戶 ID、非本人未 OTP 不可預約、非本人建立客檔成功分支、不可預約時不呼叫建立預約 gateway、相同冪等鍵不重複建立、第三方失敗不得顯示成功、快照保存失敗產生補償、LINE 通知失敗不影響成功。

**驗收**  
所有外部依賴透過 ports；第三方建立預約欄位、錯誤碼與冪等能力未確認時只能以 fake / blocker 隔離。

**提示詞**

```text
你是 booking 子 Agent，不是唯一工作者。請只修改 booking 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/booking.md

任務：
1. 依 BK-01 至 BK-13 實作預約 domain、application、ports、infrastructure 與 tests。
2. 第三方診所系統建立正式預約成功才算預約成功。
3. 本人預約使用目前 ACTIVE 綁定；非本人預約必須有 OTP 驗證結果與外部客戶 ID。
4. 實作後端冪等，避免相同冪等鍵重複建立第三方預約。
5. 通知失敗不得反轉預約成功；取消與改期不得順手實作。
6. 跑 booking 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `backoffice`

**功能描述**  
提供第一階段最小後台：登入、角色授權、會員查詢、會員詳情、排班唯讀、療程規則、系統紀錄與後台帳號管理。

**工程指導**  
不做完整 CRM，不保存病歷、財務或照片。後台必須透過各模組 application service 或 repository port 查詢資料，不直接跨 app 存取 infrastructure。

**如何實現**  
建立 `AdminUser`、`AdminRole`、`BackOfficeSession`。實作權限 policy、`BackOfficeService` command / query、`AdminUserRepository`、Django model、登入與停用規則、會員查詢與遮蔽、會員詳情 DTO、排班唯讀、療程規則管理、系統紀錄查詢。

**測試**  
覆蓋 Staff 不可管理帳號、Staff 不可管理療程規則、停用帳號不可登入、會員查詢遮蔽手機、排班只讀不呼叫更新 gateway、系統紀錄不顯示完整敏感資料、每個後台操作都檢查權限。

**驗收**  
Admin / Staff 權限符合第一階段；後台 URL、頁面資訊架構、密碼政策、帳號初始化方式未確認時保留 blocker。

**提示詞**

```text
你是 backoffice 子 Agent，不是唯一工作者。請只修改 backoffice 模組與必要共享介面，避免覆蓋其他 Agent 的修改。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- doc/tasks/backoffice.md

任務：
1. 依 BO-01 至 BO-13 實作後台 domain、application、ports、infrastructure 與 tests。
2. Admin 可管理帳號與療程規則；Staff 可查會員與看排班。
3. 排班只能唯讀，不呼叫任何更新第三方排班的 gateway。
4. 會員查詢、系統紀錄查詢都必須遮蔽敏感資料。
5. 不擴充完整 CRM、病歷、財務、照片或未定義後台功能。
6. 跑 backoffice 最小測試；回報修改檔案、測試命令、通過狀態與 blocker。
```

### `final_integration`

**功能描述**  
整合所有子 Agent 產出，修正 import、型別、lint、migration、測試斷點，更新進度並產出交付摘要。

**工程指導**  
只做整合與必要修正，不重寫已通過測試的模組設計。遇到跨模組介面衝突時，以 ports 與 application DTO 收斂，不讓 infrastructure 細節外洩。

**如何實現**  
讀取所有子 Agent 回報；檢查 `doc/tasks/progress.md`；跑分批測試找出斷點；修正 imports、typing、ruff、mypy、fixture、migration 與 settings 問題；確認未確認事項已記為 blocker；更新進度檔已通過項目。

**測試**  
先跑各模組測試，再跑完整品質命令。

**驗收**  
完整通過 `rtk uv run ruff check .`、`rtk uv run mypy .`、`rtk uv run pytest`；交付摘要列出完成模組、測試命令、通過狀態、已知 blocker 與下一步需人工確認的外部事項。

**提示詞**

```text
你是 final_integration 子 Agent，不是唯一工作者。請負責整合與驗證，不重寫已完成模組的核心設計。

必讀：
- AGENT.md
- proposal.md
- docs/detail-design.md
- docs/high-level-design.md
- doc/tasks/progress.md
- 所有 doc/tasks/*.md
- 所有子 Agent 回報

任務：
1. 檢查所有模組是否遵守 domain、application、ports、infrastructure、tests 邊界。
2. 修正跨模組 import、typing、fixture、settings、migration 與 lint 斷點。
3. 更新 doc/tasks/progress.md，只勾選已通過對應測試與驗收的項目。
4. 執行 rtk uv run ruff check .、rtk uv run mypy .、rtk uv run pytest。
5. 交付摘要列出完成模組、命令結果、blocker 與仍需人工確認的外部事項。
```

## 最終整合、測試與驗收條件

主 Agent 完成所有整合後，必須執行：

```powershell
rtk uv run ruff check .
rtk uv run mypy .
rtk uv run pytest
```

整體完成定義：

- `doc/tasks/progress.md` 中可實作項目已依測試結果更新。
- 每個模組都有 pytest 單元測試；核心 domain 與 application service 覆蓋成功路徑、非法狀態、外部失敗、冪等或補償分支。
- `ruff`、`mypy`、`pytest` 全部通過。
- 沒有真實 credential、完整個資、完整 OTP、完整外部 payload 或未確認 provider schema 進入 repo。
- 所有待確認事項以 blocker 形式列出，沒有被寫成既定需求。
- 交付摘要包含完成模組、測試命令、通過狀態、已知 blocker 與下一步只需人工確認的外部事項。
