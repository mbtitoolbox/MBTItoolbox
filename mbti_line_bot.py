from linebot import LineBotApi
from linebot.models import TextSendMessage, QuickReply, QuickReplyButton, MessageAction

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
    # 其他 MBTI 類型...
}

def handle_mbtimessages(user_message, reply_token):
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
