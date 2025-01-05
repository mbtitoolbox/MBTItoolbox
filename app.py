from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import Event, MessageEvent, TextMessage
from mbti import handle_postback  # 從mbti.py匯入handle_postback函數

app = Flask(__name__)

# LINE BOT API 初始化
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # 用您的 channel access token 替換
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # 用您的 channel secret 替換

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the LINE bot!"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    
    try:
        # 驗證 LINE webhook 事件簽名
        handler.handle(body, signature)  # 使用新版 SDK 來處理請求

    except Exception as e:
        # 異常處理，顯示錯誤訊息
        print(f"Error: {e}")
        abort(400)
    
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)



