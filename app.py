from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from mbti import get_mbti_info, get_mbti_details

# Initialize Flask app
app = Flask(__name__)

# Line Bot configuration
LINE_CHANNEL_ACCESS_TOKEN = 'ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU='
LINE_CHANNEL_SECRET = '3e49258295882026968a5788967a12f1'

line_bot_api = LineBotApi(LINE_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(LINE_CHANNEL_SECRET)

# Webhook route for Line Bot
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return 'Invalid signature', 400

    return 'OK', 200

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.strip()
    
    valid_mbti_types = [
        'ISTJ', 'ISFJ', 'INFJ', 'INTJ', 'ISTP', 'ISFP', 'INFP', 'INTP',
        'ESTP', 'ESFP', 'ENFP', 'ENTP', 'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ'
    ]
    
    if user_message.upper() in valid_mbti_types:
        # User input is an MBTI type
        basic_info = get_mbti_info(user_message.upper())
        response_message = (
            f"這是您選擇的類型 {user_message.upper()} 的基本資訊：\n{basic_info}\n\n"
            "請選擇下一步：\n"
            f"1. 想了解更多關於 {user_message.upper()}\n"
            "2. 想了解其他MBTI類型"
        )
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=response_message)
        )
    elif user_message.startswith('1') or user_message.startswith('想了解更多'):
        # User wants more details
        mbti_type = user_message.split()[-1].upper()  # Extract MBTI type
        options = '請選擇：愛情、工作、優缺點'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=options)
        )
    elif user_message in ['愛情', '工作', '優缺點']:
        # User selects a specific category
        mbti_type = 'TEMP_MBTI'  # Replace this with the saved MBTI type context
        details = get_mbti_details(mbti_type, user_message)
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=f"{mbti_type} 的 {user_message} 資訊：\n{details}")
        )
    else:
        # Invalid input or reset
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="請輸入正確的MBTI類型或選項！")
        )

if __name__ == "__main__":
    app.run(debug=True)
