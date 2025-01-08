from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

# 使用你的 Channel Access Token 和 Channel Secret
LINE_CHANNEL_ACCESS_TOKEN = "你的 Channel Access Token"
LINE_CHANNEL_SECRET = "你的 Channel Secret"

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# 根路由（非必要，但可以提供簡單的服務狀態）
@app.route("/", methods=["GET"])
def index():
    return "MBTI Bot is running!", 200

# /callback 路由
@app.route("/callback", methods=["POST"])
def callback():
    # 1. 驗證簽名
    signature = request.headers.get("X-Line-Signature")
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return "OK"

# 2. 處理訊息事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.strip()  # 使用者輸入的訊息

    # 3. 根據使用者輸入處理邏輯
    if user_message in ["ENFP", "INTJ", "ISFJ"]:  # 範例 MBTI 類型
        reply_text = f"你選擇的是 {user_message}！想了解更多關於 {user_message} 的資訊嗎？"
    else:
        reply_text = "請輸入有效的 MBTI 類型！（例如：ENFP, INTJ, ISFJ）"

    # 4. 回覆訊息
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=reply_text)
    )

if __name__ == "__main__":
    app.run(debug=True)
