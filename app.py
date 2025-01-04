from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from mbti import handle_mbtimessages  # 引入新的 MBTI 處理模組

app = Flask(__name__)

# LINE BOT 配置
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')  # 更換為您的 token
handler = WebhookHandler('YOUR_CHANNEL_SECRET')  # 更換為您的 secret

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
    
    # 呼叫新的處理函式來處理 MBTI 輸入
    handle_mbtimessages(user_message, reply_token)

if __name__ == "__main__":
    app.run(port=5000)
