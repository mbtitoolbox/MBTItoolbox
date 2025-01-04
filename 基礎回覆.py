import re
from flask import Flask, request, abort, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.models import TextMessage, TextSendMessage

app = Flask(__name__)

# 你的 Line Bot API 和 Handler 設定
line_bot_api = LineBotApi('你的Channel Access Token')
handler = WebhookHandler('你的Channel Secret')

# 定義正則表達式來檢查是否有中文
def contains_chinese(text):
    return bool(re.search('[\u4e00-\u9fff]', text))

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    # 確認 Webhook 的合法性
    try:
        handler.handle(body, signature)
    except:
        abort(400)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    
    # 檢查訊息是否包含中文
    if contains_chinese(user_message):
        reply_message = "請輸入您的MBTI類型"
    else:
        reply_message = "請輸入中文訊息"  # 這部分可以根據需求修改
    
    # 回傳訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_message)
    )

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
