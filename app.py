from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from mbti import handle_mbtimessages  # 引入新的 MBTI 處理模組

app = Flask(__name__)

line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')  # 替換為您的 Channel Access Token
handler = WebhookHandler('YOUR_CHANNEL_SECRET')  # 替換為您的 Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    handler.handle(body, signature)
    return 'OK'

if __name__ == "__main__":
    app.run(port=5000)
