# notification_reminder 任務列表

## 模組目標

建立 LINE 通知紀錄、發送預約成功通知、排程與執行行前提醒。通知失敗不得反轉預約成功結果，也不做促銷推播。

## 依賴邊界

- 依賴 `LineMessagingGateway` 發送 LINE 訊息。
- 依賴 `NotificationRepository` 保存通知紀錄。
- 依賴 `ReminderRepository` 保存與更新提醒排程。
- 行前提醒必要時依賴 `ClinicAppointmentGateway` 校驗隔日預約狀態。
- 發送錯誤與批次異常寫入 `audit_operations`。

## 最小可執行任務

- [ ] NR-01 建立 `notification_reminder` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] NR-02 定義 `NotificationRecord` aggregate：通知對象、通知類型、狀態、LINE request id、錯誤摘要。
- [ ] NR-03 實作 `NotificationRecord.mark_sent(line_request_id)`、`mark_failed(error)`、`mark_retrying()`、`give_up()`。
- [ ] NR-04 定義 `ReminderSchedule` aggregate：預約快照 ID 或外部預約 ID、排程時間、狀態、最後錯誤。
- [ ] NR-05 實作 `schedule_for(time)`、`mark_sent()`、`mark_failed(error)`、`skip(reason)`。
- [ ] NR-06 定義 `SendNotificationCommand` 與 `NotificationService.send_notification()`。
- [ ] NR-07 實作預約成功通知：第三方建立成功後才可建立通知，內容至少包含分店、療程、醫師、日期時間、預約對象。
- [ ] NR-08 定義 `RunReminderBatchCommand` 與 `ReminderService.run_batch()`。
- [ ] NR-09 實作行前提醒批次：查詢到期提醒，每批 50 筆，批次間隔 2 秒，單筆失敗不中斷。
- [ ] NR-10 發送前必要時查第三方確認預約仍有效；狀態不符合時標記 `SKIPPED`。
- [ ] NR-11 定義 `NotificationRepository` 與 `ReminderRepository` ports。
- [ ] NR-12 建立 `notification_records`、`reminder_schedules` Django model 與 migration。
- [ ] NR-13 實作 repository adapter 與 fake `LineMessagingGateway` 測試替身。

## 測試清單

- [ ] 通知成功時保存 LINE request id。
- [ ] LINE user 封鎖官方帳號或 LINE API 失敗時，通知紀錄進入失敗狀態並保存摘要。
- [ ] 通知失敗不會反轉預約成功。
- [ ] 行前提醒每批最多 50 筆。
- [ ] 單筆提醒失敗不影響同批其他提醒。
- [ ] 第三方狀態不符合時提醒可 `SKIPPED`。
- [ ] 測試不依賴真實 LINE API。

## 待確認不可自行補完

- [ ] LINE 通知使用純文字或 Flex Message。
- [ ] LINE 封鎖事件是否需業務處理。
- [ ] 排程使用 VM Cron、Cloud Scheduler 或等效方式。
- [ ] 錯誤通知要通知誰，以及使用 Email、LINE 群或其他方式。

