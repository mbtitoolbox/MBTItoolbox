from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import PostbackEvent
from mbti import handle_postback  # 從mbti.py匯入handle_postback函數

app = Flask(__name__)

# LINE BOT API 初始化
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')  # 用您的 channel access token 替換
handler = WebhookHandler('YOUR_CHANNEL_SECRET')  # 用您的 channel secret 替換

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    
    try:
        # 驗證 LINE webhook 事件簽名
        events = handler.parse_events_from_signature(signature, body)
        
        # 處理每一個事件
        for event in events:
            if isinstance(event, PostbackEvent):
                # 當 postback 事件觸發時，調用 handle_postback 函數
                handle_postback(event, line_bot_api)
    except Exception as e:
        # 異常處理，顯示錯誤訊息
        print(f"Error: {e}")
        abort(400)
    
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
