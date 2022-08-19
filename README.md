# fmBot

1. 在BotFather申請/newbo，拿到token，然後把隱私模式/setprivacy關閉Disable
2. 對新的bot按/start，和bot對話，對話會更新到`https://api.telegram.org/bot<token>/getUpdates`
3. heroku新建app，取得heroku app網址，設定webhook `https://api.telegram.org/bot<token>/setwebhook?url=<yoururl>`，更新就會通知到heroku上
4. 拉下範例，改成你要的，丟到github上，部署到heroku，bot自動化done！
    
    - 使用flask，快速方便
    - [python包](https://docs.python-telegram-bot.org/en/stable/telegram.html)
    - [官方API](https://core.telegram.org/bots/api)
    
5. 打api主動控制bot
    - 發送消息`https://api.telegram.org/bot<token>/sendMessage?chat_id=<chat_id>&text=<text>`
   - 等等等等......[官方API](https://core.telegram.org/bots/api)
