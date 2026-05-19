# PoC 計畫

## 目標

用最小成本確認這套 API 是否能支援正式整合。PoC 不做完整產品，只驗證關鍵技術風險。

## 建議時程

| 天數 | 任務 | 驗收標準 |
| --- | --- | --- |
| Day 1 | 授權與基礎查詢 | 可取得 token，成功呼叫 1-2 個 GET API |
| Day 2 | 主檔同步樣本 | 可同步診所/員工/客戶/產品任一主檔 |
| Day 3 | 事件訂閱 | 可查 topic，建立 subscription，準備 callback endpoint |
| Day 4 | Webhook 與補償 | 可接收事件或確認阻塞點，可用 event-history 補查 |
| Day 5 | 風險報告 | 產出可行性、問題清單與正式開發範圍建議 |

## PoC 範圍

- `POST /api/v1/auth/login`
- `POST /api/v1/auth/refresh`
- `GET /api/v1/event/topic`
- `POST /api/v1/event/subscribe`
- `GET /api/v1/event/event-history`

## 技術驗收點

- token 可取得且可刷新。
- 分頁、時間格式與 ID 格式清楚。
- webhook 有明確安全與重試策略。
- event-history 可支援漏接補償。
