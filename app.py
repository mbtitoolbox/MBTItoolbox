from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import PostbackEvent
from mbti import handle_postback  # 從mbti.py匯入handle_postback函數

app = Flask(__name__)

# LINE BOT API 初始化
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # 用您的 channel access token 替換
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # 用您的 channel secret 替換

# 根路徑處理
@app.route('/')
def home():
    return "LINE Bot is running!"

# 處理 LINE webhook 回調
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
