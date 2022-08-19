import os
import telegram
from flask import Flask, request
from telegram.ext import Dispatcher, MessageHandler, Filters, Updater, CommandHandler

# Initial Flask app
app = Flask(__name__)

# 設定你的token
bot = telegram.Bot(token=('5727672477:AAHBnh3c_GO0ap5AU3NyEaLJcVKE0xh2OpA'))
bot.send_message(chat_id = '5441916130', text ='FM start')
bot.send_sticker(chat_id = '5441916130',sticker ='AAMCAgADGQEAAwxi_yLWbTTR4BWOkAFSwUkPa65jSQACBQADwDZPE_lqX5qCa011AQAHbQADKQQ')
updater = Updater('5727672477:AAHBnh3c_GO0ap5AU3NyEaLJcVKE0xh2OpA')

@app.route("/")
def hello_world():
    return "hello world!"

def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def reply_handler(update, context):
    """自動回復"""
    text = update.message.text
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
