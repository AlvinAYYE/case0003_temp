# audit_operations 任務列表

## 模組目標

保存 OTP、通知、預約寫入失敗、第三方 API 錯誤與維運追蹤。此模組不保存完整敏感 payload，也不成為正式預約主資料來源。

## 依賴邊界

- 提供 `AuditLogRepository` 與 `ApiRequestLogRepository` 給其他模組使用。
- 可被 application service 或 gateway adapter 呼叫。
- 不直接呼叫外部 API。
- 不保存明文 OTP、完整手機、token、密碼、完整病歷或完整 provider payload。

## 最小可執行任務

- [ ] AO-01 建立 `audit_operations` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] AO-02 定義 `AuditLog`、`OperationalIssue`、`ApiErrorSummary`、`RequestTraceId` value object / entity。
- [ ] AO-03 定義敏感資料遮蔽 policy：手機、OTP、token、密碼、外部 payload、LINE user 相關資料。
- [ ] AO-04 定義 `AuditLogRepository` port：新增操作紀錄、錯誤紀錄、依 trace id 查詢、依類型與時間查詢。
- [ ] AO-05 定義 `ApiRequestLogRepository` port：新增 API request 摘要、更新 response 摘要、查 provider 錯誤。
- [ ] AO-06 建立 `audit_logs`、`api_request_logs` Django model 與 migration。
- [ ] AO-07 實作 repository adapter，所有寫入都先套用遮蔽 policy。
- [ ] AO-08 實作 `AuditService.record_event()` 與 `record_error()`，提供其他 application service 使用。
- [ ] AO-09 實作 `ApiRequestLogService` 或 decorator 支援 gateway adapter 自動記錄 trace id、duration、status 與錯誤摘要。
- [ ] AO-10 定義後台查詢 DTO，支援 OTP、LINE 通知、預約寫入失敗與第三方 API 錯誤摘要查詢。
- [ ] AO-11 實作錯誤嚴重度與維運狀態，但不自行定案通知對象或通知渠道。
- [ ] AO-12 建立固定測試 fixture，驗證遮蔽後資料仍可支援客服與維運追蹤。

## 測試清單

- [ ] 寫入 audit log 前會遮蔽完整手機。
- [ ] 寫入 audit log 前會移除明文 OTP。
- [ ] 寫入 request log 前會移除 token、密碼與完整 payload。
- [ ] trace id 可串接 application service 錯誤與 gateway request log。
- [ ] 可依錯誤類型、provider、時間區間查詢摘要。
- [ ] 後台查詢結果不暴露敏感資料。
- [ ] 單一 audit 寫入失敗不應讓核心預約流程誤判成功或失敗；應由呼叫端依流程決定補償。

## 待確認不可自行補完

- [ ] Log 保留天數與備份策略。
- [ ] 何種錯誤需要主動通知，以及通知窗口。
- [ ] 是否需要匯出稽核紀錄。
- [ ] 個資遮蔽規則是否需符合額外法務或院方規範。

