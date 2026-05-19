# 專案介紹

這是一個我跟學長拿得案子，內容是診所的預約系統

# 專案目標與平台

網頁手機版，並且有預約功能
有line API

# 資料來源

你可以參考 `docs\我與學長的對話.txt`

API文件則是整理在 `yuekang-openapi-docs`中

# 開發限制
遵循Clean Code開發原則

使用 uv最為包管理工具，且安裝mypy、ruff、pytest，後端採用django

請使用DDD領域驅動開發，並且確保每一個對象都有完整的覆蓋測試。