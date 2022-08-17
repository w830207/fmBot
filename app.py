import os
import sys
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, Updater, CommandHandler
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

# Initial Flask app
app = Flask(__name__)

# 設定你的token
# bot = telegram.Bot(token=('5727672477:AAHBnh3c_GO0ap5AU3NyEaLJcVKE0xh2OpA'))
# bot.send_message(chat_id = '5441916130', text ='FM start')
updater = Updater('5727672477:AAHBnh3c_GO0ap5AU3NyEaLJcVKE0xh2OpA')

@app.route("/")
def hello_world():
    return "hello world!"

@app.route('/hook', methods=['POST'])
def webhook_handler():
    """Set route /hook with POST method will trigger this method."""
    if request.method == "POST":
        update = telegram.Update.de_json(request.get_json(force=True), bot)

        # Update dispatcher process that handler to process this message
        dispatcher.process_update(update)
    return 'ok'

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def reply_handler(update, context):
    """自動回復"""
    text = update.message.text
    GDriveJSON = 'fmtest-359707-28d1fe2042e6.json'
    GSpreadSheet = 'fm'
    try:
        print('打開Google試算表')
        scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
        key = SAC.from_json_keyfile_name(GDriveJSON, scope)
        gc = gspread.authorize(key)
        worksheet = gc.open(GSpreadSheet).worksheet("records")
    except Exception as ex:
        print('無法連線Google試算表', ex)
        sys.exit(1)

    # 從第二開始
    number = 2
    while True:
        if worksheet.acell("A"+str(number)).value =="":
            print('紀錄')
            worksheet.update_acell("A"+str(number), update.message.date)
            worksheet.update_acell("B"+str(number), update.message.from_user.id)
            worksheet.update_acell("C"+str(number), update.message.sender_chat.type)
            worksheet.update_acell("D"+str(number), update.message.from_user.first_name)
            worksheet.update_acell("E"+str(number), update.message.from_user.last_name)
            worksheet.update_acell("F"+str(number), update.message.from_user.username)
            worksheet.update_acell("G"+str(number), update.message.from_user.is_bot)
            worksheet.update_acell("H"+str(number), text)
            break
        else:
            number = number + 1

    update.message.reply_text(text)


# New a dispatcher for bot
# dispatcher = Dispatcher(bot, None)

# Add handler for handling message, there are many kinds of message. For this handler, it particular handle text
# message.
updater.dispatcher.add_handler(CommandHandler("help", help))
updater.dispatcher.add_handler(MessageHandler(Filters.text, reply_handler))
updater.start_polling()
# updater.idle()

if __name__ == "__main__":
    # Running server
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
