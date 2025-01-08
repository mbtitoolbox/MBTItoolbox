import os
import logging
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction

# 設置日誌配置
logging.basicConfig(
    level=logging.INFO,  # 設置日誌記錄級別
    format='%(asctime)s - %(levelname)s - %(message)s',  # 日誌格式
    handlers=[
        logging.StreamHandler(),  # 輸出到控制台
        logging.FileHandler('app.log')  # 輸出到文件
    ]
)

app = Flask(__name__)

# LINE Bot 的 Channel Access Token 和 Channel Secret
LINE_CHANNEL_SECRET = '3e49258295882026968a5788967a12f1'  # 替換為你的 Channel Secret
LINE_CHANNEL_ACCESS_TOKEN = 'ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU='  # 替換為你的 Channel Access Token

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Webhook 端點，接收來自 LINE 伺服器的請求
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    logging.info("Received request body: %s", body)  # 記錄接收到的請求
    try:
        handler.handle(body, signature)
    except Exception as e:
        logging.error("Error processing the request: %s", e)  # 記錄錯誤
        abort(400)
    return 'OK'


# 處理文本消息的事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    logging.info("User message: %s", user_message)  # 記錄用戶發送的消息

    if user_message in mbti_data:
        mbti_type = user_message
        basic_info = get_mbti_info(mbti_type)
        logging.info("Sending response: %s", basic_info)  # 記錄回應的內容
        buttons_template = ButtonsTemplate(
            title=f"{mbti_type} 的資訊",
            text=basic_info,
            actions=[
                MessageTemplateAction(
                    label=f'想了解更多關於{mbti_type}的愛情',
                    text=f"更多關於 {mbti_type} 愛情"
                ),
                MessageTemplateAction(
                    label=f"想了解更多關於{mbti_type}的工作",
                    text=f"更多關於 {mbti_type} 工作"
                )
            ]
        )
        template_message = TemplateSendMessage(
            alt_text='MBTI 類型資訊',
            template=buttons_template
        )
        line_bot_api.reply_message(event.reply_token, template_message)

    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入有效的MBTI類型，例如: INFP")
        )
        logging.warning("User entered invalid MBTI type: %s", user_message)  # 記錄用戶輸入無效的 MBTI 類型


def get_mbti_info(mbti_type):
    """取得MBTI類型的基本資訊"""
    return mbti_data.get(mbti_type, {}).get('basic_info', '暫無相關資訊')


if __name__ == "__main__":
    app.run(port=5000)


