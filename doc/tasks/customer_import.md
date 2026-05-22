# customer_import 任務列表

## 模組目標

匯入既有客戶、歷史預約、歷史療程並保存稽核。第一階段不匯入病歷、財務、照片，也不得覆蓋未確認資料。

## 依賴邊界

- 透過 `ImportBatchRepository` 保存批次、檢查報告與匯入結果。
- 透過 `ImportedHistoryRepository` 提供歷史預約與療程查詢給 `scheduling`。
- 可寫入 `audit_operations` 保存匯入異常摘要。
- 匯入來源格式未確認前，先以 normalized row / fixture 為 application service 輸入，不自行定案 Excel、CSV 或資料庫匯出格式。

## 最小可執行任務

- [ ] CI-01 建立 `customer_import` app 邊界與目錄：`domain`、`application`、`ports`、`infrastructure`、`tests`。
- [ ] CI-02 定義 `ImportBatch` aggregate 與狀態：`UPLOADED`、`CHECKED`、`IMPORTED`、`FAILED`。
- [ ] CI-03 定義 `ImportedCustomer`、`ImportedAppointment`、`ImportedTreatmentHistory` domain / DTO。
- [ ] CI-04 實作 `ImportBatch.mark_checked(report)`、`mark_imported(summary)`、`mark_failed(error)`，並禁止未檢查批次直接匯入。
- [ ] CI-05 定義 `CheckImportBatchCommand`，輸入為已正規化資料參照或 rows，不綁定未確認的實體檔格式。
- [ ] CI-06 實作欄位檢查報告：必要欄位缺漏、手機格式錯誤、重複客戶、第三方客戶 ID 缺漏或格式異常。
- [ ] CI-07 定義 `ExecuteImportBatchCommand`，只接受已通過檢查或有明確可忽略錯誤規則的 batch。
- [ ] CI-08 實作匯入策略：新增匯入資料與歷史紀錄，不覆蓋既有未確認資料。
- [ ] CI-09 定義 `ImportBatchRepository` port：保存批次、保存檢查報告、保存匯入摘要、查詢批次。
- [ ] CI-10 定義 `ImportedHistoryRepository` port：依第三方客戶 ID、手機或本地匯入 ID 查歷史預約與療程。
- [ ] CI-11 建立 `import_batches`、`imported_customers`、`imported_appointments`、`imported_treatment_histories` Django model 與 migration。
- [ ] CI-12 實作 repository adapter，保留來源資料識別、批次 ID、成功 / 失敗筆數與錯誤原因。
- [ ] CI-13 提供後台或 CLI 可呼叫的 application entrypoint，但不自行定案正式檔案上傳 UI。

## 測試清單

- [ ] 未檢查批次不可執行匯入。
- [ ] 缺少姓名、手機或第三方客戶 ID 等必要欄位時產生錯誤報告。
- [ ] 手機格式錯誤會列入錯誤清單，不寫入有效客戶。
- [ ] 重複客戶可被偵測並出現在檢查報告。
- [ ] 匯入後可依手機或姓名查到客戶資料。
- [ ] 匯入後 `ImportedHistoryRepository` 可支援療程先決條件與安全間隔查詢。
- [ ] 匯入失敗時保留批次狀態與錯誤摘要。

## 待確認不可自行補完

- [ ] 來源資料格式：Excel、CSV、資料庫匯出或第三方 API。
- [ ] 匯入欄位正式定義與必要欄位。
- [ ] 第三方客戶 ID 是否已存在於來源資料。
- [ ] 匯入錯誤由誰修正、匯入驗收由誰確認。

