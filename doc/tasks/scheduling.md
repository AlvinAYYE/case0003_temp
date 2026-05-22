# scheduling 任務列表

## 模組目標

計算可預約療程與時段，套用療程耗時、先決療程、安全間隔與術前提醒。此模組不建立正式預約，也不更改第三方排班。

## 依賴邊界

- 依賴 `TreatmentRuleRepository` 讀寫療程規則。
- 依賴 `ImportedHistoryRepository` 查詢客戶歷史預約與療程。
- 依賴 `ClinicSchedulingGateway` 讀取醫師排班、休診與既有預約。
- 可依需要讀取 `ClinicTreatmentGateway` 或由外部 application 傳入可預約療程資料。

## 最小可執行任務

- [ ] SG-01 建立 `scheduling` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] SG-02 定義 `TreatmentRule` aggregate：療程 ID、耗時、先決療程、安全間隔、術前提醒。
- [ ] SG-03 實作 `TreatmentRule.is_satisfied_by(history)` 與 `unavailable_reasons(history)`。
- [ ] SG-04 限制 `duration_minutes` 必須以 15 分鐘為單位。
- [ ] SG-05 定義 `AvailabilityQuery` value object：分店、療程、日期區間、預約對象必填，指定醫師可選。
- [ ] SG-06 定義 `AvailableSlot` value object，可預約需有完整時間範圍，不可預約需有結構化原因。
- [ ] SG-07 定義 `FindAvailableSlotsQuery` 與 `SchedulingService.find_available_slots()`。
- [ ] SG-08 實作療程規則過濾：先決療程未滿足、安全間隔不足、規則資料不完整都回不可預約原因。
- [ ] SG-09 實作時段計算：依療程耗時、醫師排班、休診、既有預約找連續空檔。
- [ ] SG-10 支援指定醫師與不指定醫師兩種查詢，不指定時可回任一可用醫師或依前端需要回候選集合。
- [ ] SG-11 定義 `TreatmentRuleRepository` port 與 Django model `treatment_rules`。
- [ ] SG-12 實作 repository adapter，讓後台可設定療程耗時、先決療程、安全間隔與術前提醒。
- [ ] SG-13 將第三方資料不足、時區資料不明、醫師與分店關係不明轉為結構化不可預約原因。

## 測試清單

- [ ] 療程耗時不是 15 分鐘單位時建立規則失敗。
- [ ] 先決療程未完成時回不可預約原因。
- [ ] 安全間隔不足時回不可預約原因。
- [ ] 無連續空檔時回不可預約原因。
- [ ] 無可用醫師時回不可預約原因。
- [ ] 第三方排班資料不足時回結構化原因，不拋 provider schema。
- [ ] 指定醫師查詢只回該醫師可用時段。
- [ ] 不指定醫師查詢可回符合條件的醫師與時段。

## 待確認不可自行補完

- [ ] 第三方排班、休診、既有預約欄位語意與時區。
- [ ] 醫師 ID 與分店關係。
- [ ] 療程 ID、療程名稱、可預約條件欄位。
- [ ] 診所對耗時、先決條件、安全間隔的正式範例。

