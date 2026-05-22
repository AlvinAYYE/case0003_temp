# identity_binding 任務列表

## 模組目標

驗證 LINE 身份，建立 LINE user、手機、本地會員與第三方客戶 ID 的對照。此模組不負責發送簡訊、不計算可預約時段、不建立正式預約。

## 依賴邊界

- 依賴 `LineLoginGateway` 驗證可信 LINE identity。
- 依賴 `ClinicCustomerGateway` 查詢或建立第三方客戶。
- 只接受 `otp_verification` 產出的 OTP 驗證結果，不呼叫簡訊供應商。
- 透過 `MemberBindingRepository` 存取綁定資料。
- 寫入錯誤或敏感操作摘要時，透過 `audit_operations` port，不直接寫 log。

## 最小可執行任務

- [ ] IB-01 建立 `identity_binding` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] IB-02 定義 `LineUser`、`CustomerIdentity`、`MemberBinding` domain object 與狀態 enum。
- [ ] IB-03 在 `MemberBinding` 內實作 `activate()`、`deactivate()`、`mark_failed(reason)`，並禁止缺少 `line_user_id`、`mobile`、`external_customer_id` 的綁定進入 `ACTIVE`。
- [ ] IB-04 定義 `VerifyLineIdentityQuery` 與 `LineIdentityService`，後端只信任 `LineLoginGateway` 驗證結果，不信任前端直傳 UID。
- [ ] IB-05 定義 `GetBindingStatusQuery` 與 `MemberBindingService.get_binding_status()`，可查詢目前 LINE 使用者是否已有啟用綁定。
- [ ] IB-06 定義 `CreateMemberBindingCommand`，輸入只包含詳細設計已支持的欄位：LINE identity、姓名、性別、生日、手機、OTP 驗證結果。
- [ ] IB-07 實作建立綁定流程：先查本地 `ACTIVE` 綁定，再查第三方客戶；查無時呼叫第三方建立客檔。
- [ ] IB-08 客檔建立失敗時不得建立可用綁定，需保存失敗原因並回傳可理解的失敗結果。
- [ ] IB-09 定義 `MemberBindingRepository` port：依 LINE user 查、依手機查、保存綁定狀態、查啟用綁定。
- [ ] IB-10 建立 `member_bindings` Django model 與 migration，欄位以詳細設計資料模型為準，手機需有可查詢值與遮蔽 / hash 策略。
- [ ] IB-11 實作 repository adapter，讓 application service 不依賴 Django ORM 細節。
- [ ] IB-12 將重複綁定、客檔建立失敗、第三方錯誤轉為 application 層明確結果，不直接拋出 provider schema。
- [ ] IB-13 補上使用 fake gateway 與 fake repository 的 application service tests。

## 測試清單

- [ ] 缺少 `external_customer_id` 時 `MemberBinding` 不可 `ACTIVE`。
- [ ] 停用後的綁定不可用於新預約。
- [ ] `LineIdentityService` 在 LINE token 驗證失敗時不建立任何本地身份資料。
- [ ] 已有 `ACTIVE` 綁定時不重複建立第三方客戶。
- [ ] 第三方查無客戶且建立客戶成功時，才建立 `ACTIVE` 綁定。
- [ ] 第三方建立客戶失敗時，回傳失敗並留下稽核紀錄。
- [ ] 測試輸出與 log 不包含完整手機號碼。

## 待確認不可自行補完

- [ ] 第三方客戶欄位、建立客戶必填欄位與錯誤碼。
- [ ] 第三方建立客戶是否支援冪等鍵。
- [ ] LINE Login Channel、LIFF 驗證方式與測試帳號。

