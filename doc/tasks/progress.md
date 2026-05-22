# 診所 LINE 預約系統任務總進度

> 來源文件：`proposal.md`、`docs/detail-design.md`  
> 本檔追蹤各模組「實作完成」狀態，不代表任務拆分文件是否完成。  
> 勾選完成前，該模組需至少通過對應的 domain unit test、application service test，以及必要的 repository / gateway fake 或 contract test。

## 完成判定規則

- [ ] 模組有清楚的 Django app 邊界，不直接依賴其他模組的 infrastructure 實作。
- [ ] Domain object 以 OOP 表達不變量與狀態轉換，且可不啟動 Django 直接測試。
- [ ] Application service 只編排 use case、交易邊界、repository port 與 gateway port。
- [ ] 外部 API schema 不滲透到 domain、application service 或前端 DTO。
- [ ] 個資與 OTP 不在 log、錯誤訊息、測試快照中輸出完整明文。
- [ ] 未確認的第三方欄位、錯誤碼、URL、訊息格式與部署細節以 `待確認` 標示，不自行補完。
- [ ] `pytest` 通過該模組測試；後續有程式碼時同步執行 `ruff` 與 `mypy`。

## 建議實作順序

1. `external_integration`：先建立 gateway port、錯誤轉換、request log 與 fake adapter。
2. `audit_operations`：建立跨模組稽核與遮蔽能力。
3. `otp_verification`：完成手機驗證核心規則。
4. `identity_binding`：完成 LINE 身份與會員綁定。
5. `customer_import`：完成匯入檢查與歷史資料查詢基礎。
6. `scheduling`：完成療程規則與可預約時段計算。
7. `appointment_snapshot`：完成第三方預約成功後的本地快照。
8. `notification_reminder`：完成通知紀錄與行前提醒批次。
9. `booking`：串接本人 / 非本人預約主流程。
10. `backoffice`：完成最小後台查詢、設定與權限。

## 模組完成狀態

- [ ] `identity_binding` - [identity_binding.md](identity_binding.md)
- [ ] `otp_verification` - [otp_verification.md](otp_verification.md)
- [ ] `customer_import` - [customer_import.md](customer_import.md)
- [ ] `booking` - [booking.md](booking.md)
- [ ] `scheduling` - [scheduling.md](scheduling.md)
- [ ] `appointment_snapshot` - [appointment_snapshot.md](appointment_snapshot.md)
- [ ] `notification_reminder` - [notification_reminder.md](notification_reminder.md)
- [ ] `backoffice` - [backoffice.md](backoffice.md)
- [ ] `external_integration` - [external_integration.md](external_integration.md)
- [ ] `audit_operations` - [audit_operations.md](audit_operations.md)

## 跨模組阻塞與待確認

- [ ] 第三方診所系統正式名稱、base URL、sandbox、token 規格、錯誤碼與欄位語意已確認。
- [ ] 第三方建立客戶與建立預約是否支援冪等鍵已確認。
- [ ] 第三方預約列表狀態值、取消 / 改期語意、webhook 或 event history 能力已確認。
- [ ] LINE Provider、Messaging API Channel、LINE Login Channel、LIFF App、Rich Menu 管理權限已確認。
- [ ] LINE 通知格式使用純文字或 Flex Message 已確認。
- [ ] 三竹正式 endpoint、測試方式、編碼設定、OTP 文案審核與餘額不足通知窗口已確認。
- [ ] 匯入來源格式、欄位定義、第三方客戶 ID 是否存在、驗收窗口已確認。
- [ ] 部署排程方式、固定出口 IP、Secret 管理、備份保留天數與錯誤通知方式已確認。

