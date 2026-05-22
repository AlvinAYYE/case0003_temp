# appointment_snapshot 任務列表

## 模組目標

保存第三方正式預約建立成功後的本地快照與查詢索引。此模組不是正式預約主資料來源，也不提供取消或改期操作。

## 依賴邊界

- 依賴 `AppointmentSnapshotRepository` 保存與查詢本地快照。
- `booking` 在第三方建立成功後呼叫本模組保存快照。
- `MyAppointmentsService` 查詢時仍以 `ClinicAppointmentGateway` 為來源，不長期保存查詢結果。
- 可把外部取消 / 改期狀態映射為唯讀快照狀態。

## 最小可執行任務

- [ ] AS-01 建立 `appointment_snapshot` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] AS-02 定義 `AppointmentSnapshot` aggregate 與狀態：`CREATED`、`FAILED`、`EXTERNAL_CANCELLED`、`EXTERNAL_RESCHEDULED`。
- [ ] AS-03 實作 `mark_created(external_id)`，禁止缺少第三方預約 ID 的快照進入成功狀態。
- [ ] AS-04 實作 `mark_failed(error)`、`mark_external_cancelled()`、`mark_external_rescheduled()`。
- [ ] AS-05 定義保存快照的 application service 或協作介面，供 `booking` 成功分支呼叫。
- [ ] AS-06 定義 `ListMyAppointmentsQuery` 與 `MyAppointmentsService.list_my_appointments()`。
- [ ] AS-07 `MyAppointmentsService` 每次查詢都以綁定的第三方客戶 ID 呼叫 `ClinicAppointmentGateway`，不長期保存我的預約查詢結果。
- [ ] AS-08 定義第三方預約 DTO 到本系統唯讀 DTO 的轉換，不讓第三方 schema 直接回到前端。
- [ ] AS-09 定義 `AppointmentSnapshotRepository` port：保存快照、依外部預約 ID 查詢、依 LINE user 查詢本地追蹤資料。
- [ ] AS-10 建立 `appointment_snapshots` Django model 與 migration。
- [ ] AS-11 實作 repository adapter，保存建立者 LINE user、預約對象類型、分店、療程、醫師、時間與狀態。
- [ ] AS-12 本地快照保存失敗時，回傳可補償的錯誤並要求 `booking` 寫入稽核紀錄。

## 測試清單

- [ ] 沒有第三方預約 ID 不可標記建立成功。
- [ ] 外部取消或改期只做唯讀狀態，不提供本地操作入口。
- [ ] 保存快照時必要欄位缺漏會失敗。
- [ ] `MyAppointmentsService` 查詢時每次都呼叫第三方 gateway。
- [ ] 我的預約查詢結果不寫入長期保存資料表。
- [ ] 第三方未知狀態值會轉為明確的未知 / 待確認結果，不直接暴露 provider 原始值。

## 待確認不可自行補完

- [ ] 第三方預約列表狀態值。
- [ ] 取消狀態、改期狀態與時間欄位語意。
- [ ] 第三方是否提供查單筆預約與 event history。

