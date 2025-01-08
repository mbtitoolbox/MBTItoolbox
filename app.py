import os
import logging
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage, TemplateSendMessage, ButtonsTemplate, MessageTemplateAction
from mbti import mbti_data
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
    
# 定期喚醒用funtion
@app.route("/", methods=['POST', 'GET'])
def CronUp():
    return 'Welcome to the MBTI Bot!'
    
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
                ),
                MessageTemplateAction(
                    label=f"想了解更多關於{mbti_type}的優缺點",
                    text=f"更多關於 {mbti_type} 優缺點"
                )
            ]
        )
        template_message = TemplateSendMessage(
            alt_text='MBTI 類型資訊',
            template=buttons_template
        )
        line_bot_api.reply_message(event.reply_token, template_message)
    elif user_message.startswith("更多關於"):
        # 用戶選擇了「愛情」、「工作」、「優缺點」選項
        mbti_type = user_message.split(" ")[1]  # 提取MBTI類型
        category = user_message.split(" ")[-1]  # 提取選擇的類別（愛情、工作、優缺點）
        if mbti_type in mbti_data:
            category_info = get_category_info(mbti_type, category)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text=category_info)
            )
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text="請輸入有效的MBTI類型。")
            )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入有效的MBTI類型，例如: INFP")
        )
        logging.warning("User entered invalid MBTI type: %s", user_message)  # 記錄用戶輸入無效的 MBTI 類型
def get_mbti_info(mbti_type):
    """取得MBTI類型的基本資訊"""
    return mbti_data.get(mbti_type, {}).get('basic_info', '暫無相關資訊')
def get_category_info(mbti_type, category):
    """根據選擇的類別返回相關的資訊"""
    if category == "愛情":
        return mbti_data.get(mbti_type, {}).get('details', {}).get('愛情', '暫無愛情資訊')
    elif category == "工作":
        return mbti_data.get(mbti_type, {}).get('details', {}).get('工作', '暫無工作資訊')
    elif category == "優缺點":
        return mbti_data.get(mbti_type, {}).get('details', {}).get('優缺點', '暫無優缺點資訊')
    else:
        return '無效的選項'
if __name__ == "__main__":
    app.run(port=5000)
    #app.run(host='0.0.0.0', port=5000)
