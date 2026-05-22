# otp_verification 任務列表

## 模組目標

發送與驗證 OTP，控管冷卻、有效期、發送上限與錯誤鎖定。此模組不建立會員綁定，也不理解預約流程細節。

## 依賴邊界

- 依賴 `SmsOtpGateway` 發送三竹簡訊。
- 透過 `OtpRepository` 保存 OTP 流程、發送狀態、驗證狀態、冷卻與上限。
- 可通知 `audit_operations` 保存 provider 回應摘要與異常，但不得輸出明文 OTP。

## 最小可執行任務

- [ ] OV-01 建立 `otp_verification` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] OV-02 定義 `OtpVerification`、`OtpAttempt`、`MaskedMobile` domain object / value object。
- [ ] OV-03 實作 OTP 狀態轉換：`send()`、`verify(code)`、`expire(now)`、`lock()`、`mark_failed(error)`。
- [ ] OV-04 實作安全規則：60 秒冷卻、5 分鐘有效、錯誤 5 次鎖定、單手機或單來源 IP 每日上限。
- [ ] OV-05 定義 OTP purpose，至少支援會員綁定手機驗證與非本人預約手機驗證。
- [ ] OV-06 定義 `SendOtpCommand` 與 `OtpService.send_otp()`，回傳發送結果、冷卻資訊與遮蔽手機。
- [ ] OV-07 定義 `VerifyOtpCommand` 與 `OtpService.verify_otp()`，回傳驗證成功 / 過期 / 鎖定 / 錯誤次數等明確結果。
- [ ] OV-08 定義 `OtpRepository` port：建立流程、保存發送結果、保存驗證結果、查冷卻、查每日上限。
- [ ] OV-09 建立 `otp_verifications` Django model 與 migration；不得保存明文 OTP，可保存 hash 與 provider 摘要。
- [ ] OV-10 實作 repository adapter，確保手機查詢使用 hash 或等效不可逆策略。
- [ ] OV-11 定義 `SmsOtpGateway` port 所需最小 DTO，實際 endpoint、編碼、帳密欄位以正式文件為準。
- [ ] OV-12 建立 fake `SmsOtpGateway`，讓 service test 不連外。
- [ ] OV-13 將簡訊供應商失敗、餘額不足、timeout 轉為 application 層結果與稽核紀錄。

## 測試清單

- [ ] 冷卻未到不可重發，回傳下次可發送時間。
- [ ] 發送 5 分鐘後驗證必定過期。
- [ ] 錯誤 5 次後流程進入鎖定，後續正確碼也不可通過。
- [ ] 單手機或單 IP 超過每日上限時拒絕發送。
- [ ] 驗證成功後不可重複使用同一 OTP。
- [ ] provider 失敗時保存錯誤摘要，但不輸出明文 OTP 或完整手機。
- [ ] fake gateway application service test 覆蓋發送成功、發送失敗、驗證成功、驗證失敗。

## 待確認不可自行補完

- [ ] 三竹正式 API endpoint、測試方式與環境。
- [ ] 三竹編碼設定為 Big5、UTF-8 或其他。
- [ ] OTP 簡訊文案是否需送審。
- [ ] 簡訊餘額不足時通知誰。

