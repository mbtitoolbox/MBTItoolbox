from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageAction

app = Flask(__name__)

# 使用你的 Channel Access Token 和 Channel Secret
LINE_CHANNEL_ACCESS_TOKEN = "ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU="
LINE_CHANNEL_SECRET = "3e49258295882026968a5788967a12f1"

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

    # 判斷是否為 MBTI 類型
    if user_message in BASIC_INFO.keys():  # 確認輸入是有效 MBTI 類型
        # 回覆 MBTI 基本資料
        reply_text = f"你選擇的是 {user_message}！\n{BASIC_INFO[user_message]}"
        
        # 創建按鈕選單
        buttons_template = ButtonsTemplate(
            title=f"{user_message} 的選項",
            text="請選擇你想了解的內容：",
            actions=[
                MessageAction(label="愛情", text=f"愛情:{user_message}"),
                MessageAction(label="工作", text=f"工作:{user_message}"),
                MessageAction(label="優缺點", text=f"優缺點:{user_message}")
            ]
        )
        
        template_message = TemplateSendMessage(alt_text=f"{user_message} 選單", template=buttons_template)
        
        # 回覆基本資料與按鈕選單
        line_bot_api.reply_message(
            event.reply_token,
            [TextSendMessage(text=reply_text), template_message]
        )
        return  # 防止進入後續邏輯
    
    # 處理按鈕選項的選擇
    elif user_message.startswith("愛情:") or user_message.startswith("工作:") or user_message.startswith("優缺點:"):
        # 根據選擇的類型回覆詳細資料
        try:
            category, mbti_type = user_message.split(":")
            detail_text = get_more_info(mbti_type, category)  # 從資料庫獲取詳細資訊
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=detail_text)
            )
        except ValueError:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="格式錯誤，請重新選擇。")
            )
        return
    
    # 當輸入無效時的回應
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入有效的 MBTI 類型！（例如：ENFP, INTJ, ISFJ）")
        )



