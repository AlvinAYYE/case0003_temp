# booking 任務列表

## 模組目標

編排本人 / 非本人預約，取得或建立預約對象客檔，送出正式預約。第三方診所系統建立預約成功才算第一階段預約成功。

## 依賴邊界

- 依賴 `identity_binding` 提供目前 LINE 使用者的啟用綁定。
- 非本人預約只接受 `otp_verification` 的驗證結果。
- 依賴 `scheduling` 查詢與驗證可預約時段。
- 依賴 `ClinicCustomerGateway` 取得或建立被預約人客戶資料。
- 依賴 `ClinicAppointmentGateway` 建立正式預約。
- 成功後委派 `appointment_snapshot` 保存快照，委派 `notification_reminder` 建立通知與提醒。

## 最小可執行任務

- [ ] BK-01 建立 `booking` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] BK-02 定義 `BookingSubject`，支援 `SELF` 與 `OTHER`，並在 domain 內限制非本人必須有姓名、生日、手機、OTP 驗證結果與外部客戶 ID。
- [ ] BK-03 定義 `BookingCommand`、`BookingResult`、預約失敗原因 enum 與使用者可理解錯誤摘要。
- [ ] BK-04 定義 `CreateAppointmentCommand`，輸入包含 LINE 身份、預約對象、分店、療程、醫師、時段、冪等鍵。
- [ ] BK-05 定義 `IdempotencyRepository` port；若資料表設計未定，先以 port 隔離，不併入 domain。
- [ ] BK-06 實作 `AppointmentBookingService.create_appointment()` 本人流程：驗證 LINE 身份、取得啟用綁定、組成本人預約對象。
- [ ] BK-07 實作非本人流程：驗證 OTP 結果、依手機查第三方客戶、查無時建立客檔、保存代約 LINE 帳號操作紀錄。
- [ ] BK-08 呼叫 `SchedulingService` 確認時段仍可預約；不可預約時回傳結構化原因，不呼叫建立預約 gateway。
- [ ] BK-09 實作後端冪等：相同冪等鍵與相同 request 回傳既有結果，避免重複建立第三方預約。
- [ ] BK-10 呼叫 `ClinicAppointmentGateway` 建立正式預約；第三方回成功才進入成功分支。
- [ ] BK-11 第三方建立成功後，保存 `AppointmentSnapshot` 與 `ReminderSchedule`；本地保存失敗時建立補償 / 稽核紀錄。
- [ ] BK-12 發送預約成功通知需非同步或由通知 service 接手；通知失敗不得反轉預約成功。
- [ ] BK-13 第三方回時段衝突、客戶資料錯誤、驗證失敗或 timeout 時，回傳失敗結果並保存錯誤紀錄。

## 測試清單

- [ ] 本人預約只能使用目前啟用綁定的第三方客戶 ID。
- [ ] 非本人未通過 OTP 不可建立預約。
- [ ] 第三方查無非本人客戶且建立客檔成功時，可使用新客戶 ID 建立預約。
- [ ] `SchedulingService` 回不可預約原因時，不呼叫 `ClinicAppointmentGateway`。
- [ ] 相同冪等鍵重送不會建立第二筆第三方預約。
- [ ] 第三方建立預約失敗時，本系統不得顯示預約成功。
- [ ] 第三方成功但本地快照保存失敗時，產生補償 / 稽核紀錄。
- [ ] LINE 通知失敗不影響預約成功結果。

## 待確認不可自行補完

- [ ] 第三方建立預約 request / response 欄位與錯誤碼。
- [ ] 第三方建立預約是否支援冪等鍵。
- [ ] 同時多人預約同一時段時第三方錯誤碼與建議處理。
- [ ] 取消與改期不是第一階段範圍，不得順手實作。

