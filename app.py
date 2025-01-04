import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# Initialize LineBotApi and WebhookHandler with your credentials
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # 替換為你的 Channel Access Token
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # 替換為你的 Channel Secret

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route("/callback", methods=['POST'])
def callback():
    # Get the request body as text
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        # Handle the incoming webhook event
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Error:", e)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # 回應用戶的訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="請輸入您的MBTI類型")
    )

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port)
