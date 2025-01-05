from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from mbti import handle_mbtimessages  # 引入處理 MBTI 訊息的函數

app = Flask(__name__)

# LINE BOT 配置
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # 替換為您的 Channel Access Token
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # 替換為您的 Channel Secret

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_token = event.reply_token
    
    # 呼叫處理 MBTI 訊息的函式
    handle_mbtimessages(user_message, reply_token)

if __name__ == "__main__":
    app.run(port=5000)
