# fmBot
## 串接Google sheet API

1. 到gcp平台新建專案
2. 啟用Google Sheets API、Google Drive API
3. 切換到**憑證**的頁面點選**建立憑證**的**服務帳戶**
4. **憑證**的頁面找到剛剛新建的服務帳號，點擊後**詳細資料**取得電子郵件、**金鑰**新增建立金鑰(JSON)
5. 新建個google sheet，共用添加上服務帳號的電子郵件
6. 金鑰丟入github bot專案
7. 使用python包：[gspread](https://docs.gspread.org/en/latest/index.html)
