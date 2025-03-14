from flask import Flask, request
import telegram
import os

app = Flask(__name__)
#TOKEN = os.getenv('BOT_TOKEN')
bot = telegram.Bot(token=TOKEN)

@app.route('/webhook', methods=['POST'])
def webhook():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    chat_id = update.message.chat.id
    text = update.message.text
    bot.send_message(chat_id=chat_id, text=f"Ты сказал: {text}")
    return 'OK'

if __name__ == '__main__':
    app.run(port=8080)