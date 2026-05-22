# backoffice 任務列表

## 模組目標

提供第一階段最小後台：登入、角色授權、會員查詢、會員詳情、排班唯讀、療程規則、系統紀錄與後台帳號管理。此模組不做完整 CRM，不保存病歷、財務或照片。

## 依賴邊界

- 依賴 `AdminUserRepository` 管理後台帳號、角色、狀態與登入資訊。
- 透過各模組 application service 或 repository port 查詢資料，不直接跨 app 存取 infrastructure。
- 排班唯讀透過 `ClinicSchedulingGateway` 或 scheduling application service。
- 療程規則管理透過 `scheduling` 的 `TreatmentRuleRepository` / service。
- 系統紀錄查詢透過 `audit_operations` 與 notification / otp 查詢 port。

## 最小可執行任務

- [ ] BO-01 建立 `backoffice` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] BO-02 定義 `AdminUser` aggregate、`AdminRole` enum 與 `BackOfficeSession` value object。
- [ ] BO-03 實作 `AdminUser.can_manage_rules()`、`can_view_members()`、`deactivate()`、`reset_password()`。
- [ ] BO-04 限制第一階段角色：Admin 可管理帳號與療程規則；Staff 可查會員與看排班。
- [ ] BO-05 定義 `BackOfficeService` 的查詢 / command 入口，每個操作都需檢查 session 與權限。
- [ ] BO-06 定義 `AdminUserRepository` port 與 `admin_users` Django model / migration。
- [ ] BO-07 實作後台登入與停用帳號不可登入規則；若整合 Django auth，仍保留 domain policy 可獨立測試。
- [ ] BO-08 實作會員查詢 use case：依姓名、手機、LINE 綁定狀態搜尋，輸出需遮蔽手機。
- [ ] BO-09 實作會員詳情 use case：顯示本地會員、匯入資料摘要、第三方客戶 ID 與預約查詢入口所需 DTO。
- [ ] BO-10 實作排班唯讀 use case：依分店與醫師查第三方排班，不提供本地編輯。
- [ ] BO-11 實作療程規則管理 use case：設定耗時、先決療程、安全間隔與術前提醒。
- [ ] BO-12 實作系統紀錄查詢 use case：OTP、LINE 通知、預約寫入失敗、第三方 API 錯誤摘要。
- [ ] BO-13 補上後台頁面或 API controller 時，不自行擴充第一階段未定義的 CRM 功能。

## 測試清單

- [ ] Staff 不可管理帳號。
- [ ] Staff 不可管理療程規則。
- [ ] 停用帳號不可登入。
- [ ] 會員查詢結果遮蔽手機與敏感資料。
- [ ] 排班功能只讀，不會呼叫任何更新第三方排班的 gateway。
- [ ] 系統紀錄查詢不顯示完整 OTP、完整手機或完整外部 payload。
- [ ] 每個後台操作都檢查權限。

## 待確認不可自行補完

- [ ] 後台正式登入方式與密碼政策。
- [ ] Admin / Staff 帳號初始化方式。
- [ ] 後台 URL、頁面資訊架構與 UI 細節。
- [ ] 哪些錯誤需要後台顯示，哪些只留維運查詢。

