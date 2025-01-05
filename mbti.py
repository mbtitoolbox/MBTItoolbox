from linebot.models import (
    TextSendMessage, 
    TemplateSendMessage, 
    ButtonsTemplate, 
    PostbackAction, 
    QuickReply, 
    QuickReplyButton
)

# 定義所有有效的 MBTI 類型
VALID_MBTI_TYPES = {
    "ENFP": {"trait": "倡導者，樂觀開朗，充滿創意。", "love": "愛情中的 ENFP 充滿熱情，總是尋找情感的深度。", "work": "工作中的 ENFP 富有創意，並且在團隊中能帶來活力。", "pros_cons": "優點：充滿創意，富有熱情；缺點：容易焦慮，缺乏耐性。", "image_url": "https://example.com/enfp.jpg"},
    # 可以補充其他 MBTI 類型
}

def handle_postback(event, line_bot_api):
    postback_data = event.postback.data
    reply_token = event.reply_token

    # 解析 postback_data
    data = postback_data.split('_')
    action = data[0]
    mbti_type = data[1] if len(data) > 1 else None

    if action == "select_mbtis":
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text="請輸入您的 MBTI 類型：")
        )
    elif action == "explore" and mbti_type in VALID_MBTI_TYPES:
        quick_reply_buttons = QuickReply(items=[
            QuickReplyButton(action=PostbackAction(label="優缺點", data=f"pros_cons_{mbti_type}")),
            QuickReplyButton(action=PostbackAction(label="愛情", data=f"love_{mbti_type}")),
            QuickReplyButton(action=PostbackAction(label="工作", data=f"work_{mbti_type}"))
        ])
        line_bot_api.reply_message(
            reply_token, 
            TextSendMessage(text=f"選擇你想了解的 ENFP 內容：", quick_reply=quick_reply_buttons)
        )
    elif action in ["pros_cons", "love", "work"] and mbti_type in VALID_MBTI_TYPES:
        mbti_data = VALID_MBTI_TYPES[mbti_type]
        if action == "pros_cons":
            response_message = f"{mbti_type} 的優缺點：{mbti_data['pros_cons']}"
        elif action == "love":
            response_message = f"{mbti_type} 的愛情：{mbti_data['love']}"
        elif action == "work":
            response_message = f"{mbti_type} 的工作：{mbti_data['work']}"
        line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))

def handle_message(event, line_bot_api):
    user_message = event.message.text.upper()
    reply_token = event.reply_token

    if user_message in VALID_MBTI_TYPES:
        mbti_data = VALID_MBTI_TYPES[user_message]
        buttons_template = ButtonsTemplate(
            title=f"{user_message} 的特質",
            text=f"想了解更多關於 {user_message} 嗎？",
            thumbnail_image_url=mbti_data["image_url"],
            actions=[
                PostbackAction(label=f"想了解更多關於 {user_message}", data=f"explore_{user_message}"),
                PostbackAction(label="想了解其他 MBTI 類型", data="select_mbtis")
            ]
        )
        line_bot_api.reply_message(
            reply_token,
            TemplateSendMessage(alt_text=f"{user_message} 的特質", template=buttons_template)
        )
    else:
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="請輸入有效的 MBTI 類型，例如：ENFP、INTJ、ISFP 等。")
        )
