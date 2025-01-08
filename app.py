from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, PostbackEvent, PostbackAction, TextSendMessage, ButtonsTemplate, MessageAction

import mbti  # 导入自定义的mbti数据和函数

app = Flask(__name__)

line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3e49258295882026968a5788967a12f1')

# 用户初始输入的MBTI类型
user_mbti = None

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    # 处理消息事件
    handler.handle(body, signature)
    return 'OK'
    
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global user_mbti
    
    user_message = event.message.text.strip().upper()  # 獲取用戶訊息並轉成大寫
    
    # 檢查是否為有效的 MBTI 類型
    if user_message in mbti.MBTI_TYPES:
        user_mbti = user_message
        mbti_info = mbti.get_basic_info(user_mbti)  # 獲取 MBTI 基本資訊
        
        # 準備按鈕樣板
        buttons_template = ButtonsTemplate(
            title=f"關於 {user_mbti}",
            text=mbti_info,
            actions=[
                PostbackAction(label=f"想了解更多關於 {user_mbti}", data=f"more_info_{user_mbti}"),
                PostbackAction(label="想了解其他 MBTI 類型", data="other_mbti")
            ]
        )
        line_bot_api.reply_message(
            event.reply_token,
            TemplateSendMessage(alt_text="MBTI 資訊選單", template=buttons_template)
        )
        return

    # 處理按鈕互動邏輯
    if user_message.startswith("more_info_"):
        mbti_type = user_message.split("_")[-1]  # 提取 MBTI 類型
        if mbti_type in mbti.MBTI_TYPES:
            more_info_buttons = ButtonsTemplate(
                title=f"更多關於 {mbti_type}",
                text="請選擇想了解的範疇",
                actions=[
                    MessageAction(label="愛情", text=f"{mbti_type} 愛情"),
                    MessageAction(label="工作", text=f"{mbti_type} 工作"),
                    MessageAction(label="優缺點", text=f"{mbti_type} 優缺點"),
                ]
            )
            line_bot_api.reply_message(
                event.reply_token,
                TemplateSendMessage(alt_text=f"{mbti_type} 更多資訊", template=more_info_buttons)
            )
        return

    # 處理其他輸入
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="請輸入有效的 MBTI 類型，例如：ENFP")
    )
