from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction
)

python line-bot-mbti .py
app = Flask(__name__)

# LINE BOT 配置
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3e49258295882026968a5788967a12f1')

# 儲存 16 種 MBTI 類型及其回覆內容
mbti_data = {
    "INFP": {
        "description": "INFP 是個好人，富有同情心和理想主義。",
        "愛情": "INFP 的愛情觀是感性而執著。今年可能會拖單，請耐心等待真愛！",
        "人生觀": "INFP 的人生觀充滿理想和夢想，追求意義深遠的生活。"
    },
    "INTJ": {
        "description": "INTJ 是個充滿計畫性且獨立思考的人。",
        "愛情": "INTJ 對愛情要求高，但願意為對的人付出深情。",
        "人生觀": "INTJ 的人生觀重視目標和效率，常以長遠眼光看待問題。"
    },
    # 添加其他 MBTI 類型...
    # "ESFP": {...},
    # "ENTP": {...},
}

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except Exception as e:
        print(f"Error: {e}")
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_token = event.reply_token

    # 判斷用戶輸入是否為 MBTI 類型
    if user_message in mbti_data:
        personality = mbti_data[user_message]
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(
                text=personality["description"] + " 你想了解哪方面？",
                quick_reply=QuickReply(items=[
                    QuickReplyButton(action=MessageAction(label="愛情", text=f"{user_message}_愛情")),
                    QuickReplyButton(action=MessageAction(label="人生觀", text=f"{user_message}_人生觀"))
                ])
            )
        )
    elif any(key in user_message for key in mbti_data.keys()):
        # 處理具體選項 (例如 "INFP_愛情")
        for mbti_type, details in mbti_data.items():
            if user_message == f"{mbti_type}_愛情":
                line_bot_api.reply_message(reply_token, TextSendMessage(text=details["愛情"]))
                return
            elif user_message == f"{mbti_type}_人生觀":
                line_bot_api.reply_message(reply_token, TextSendMessage(text=details["人生觀"]))
                return
    else:
        # 不理解用戶的輸入時的回覆
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="抱歉，我不太明白你的意思。可以輸入 MBTI 類型（例如 INFP）試試看！")
        )

if __name__ == "__main__":
    app.run(port=5000)'