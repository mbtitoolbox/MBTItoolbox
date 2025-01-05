from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction, QuickReply, QuickReplyButton

# MBTI 類型與特質映射
VALID_MBTI_TYPES = {
    "INTJ": "戰略家，具有強烈的規劃能力與遠見。",
    "INTP": "哲學家，喜歡分析與深度思考。",
    "ENTJ": "指揮官，領導力與執行力出色。",
    "ENTP": "辯論家，創意十足，擅長挑戰現狀。",
    "INFJ": "提倡者，富有洞察力並關注人際關係。",
    "INFP": "調停者，重視價值觀與內在和諧。",
    "ENFJ": "主人公，關心他人並激勵周圍的人。",
    "ENFP": "競選者，充滿熱情與想像力。",
    "ISTJ": "後勤師，務實、可靠且守規矩。",
    "ISFJ": "守護者，善良且富有責任感。",
    "ESTJ": "總經理，擅長組織與管理。",
    "ESFJ": "執政官，熱心助人並維持社交和諧。",
    "ISTP": "工匠，喜歡實驗與實踐。",
    "ISFP": "冒險家，感性且享受當下。",
    "ESTP": "企業家，冒險精神與行動力兼具。",
    "ESFP": "表演者，熱愛生活並傳遞歡樂。"
}

def handle_mbtimessages(user_message, reply_token, line_bot_api):
    user_message = user_message.strip().upper()

    if user_message in VALID_MBTI_TYPES:
        # 顯示該MBTI類型的介紹文字
        mbti_traits = VALID_MBTI_TYPES[user_message]
        response_message = f"您是 {user_message} 類型！特質是：{mbti_traits}"

        # 動態創建按鈕模板，根據用戶選擇的MBTI顯示對應的選項
        buttons_template = ButtonsTemplate(
            title=f"更多關於{user_message}",
            text=f"想了解更多關於 {user_message} 的內容？",
            actions=[
                PostbackAction(label=f"想了解更多關於{user_message}愛情", data=f"love_{user_message}"),
                PostbackAction(label=f"想了解更多關於{user_message}工作", data=f"work_{user_message}"),
                PostbackAction(label=f"想了解{user_message}的優缺點", data=f"pros_cons_{user_message}"),
                PostbackAction(label="想了解其他MBTI類型", data="other_mbtis")
            ]
        )

        # 發送MBTI特質文字和按鈕模板
        line_bot_api.reply_message(
            reply_token,
            [
                TextSendMessage(text=response_message),
                TemplateSendMessage(alt_text=f"更多關於{user_message}", template=buttons_template)
            ]
        )
    else:
        # 若用戶輸入無效MBTI類型，要求重新輸入
        response_message = "請輸入您的 MBTI 類型（例如：INTJ, ENFP 等）。"
        line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))


def handle_postback(postback_data, reply_token, line_bot_api):
    data = postback_data.split("_")
    
    if len(data) == 2:
        mbti_type = data[1]

        if data[0] == "love":
            # 回覆愛情特質
            love_message = f"{mbti_type} 的愛情特質是……"
            line_bot_api.reply_message(reply_token, TextSendMessage(text=love_message))
        elif data[0] == "work":
            # 回覆工作特質
            work_message = f"{mbti_type} 的工作特質是……"
            line_bot_api.reply_message(reply_token, TextSendMessage(text=work_message))
        elif data[0] == "pros_cons":
            # 回覆優缺點
            pros_cons_message = f"{mbti_type} 的優缺點是……"
            line_bot_api.reply_message(reply_token, TextSendMessage(text=pros_cons_message))

    elif postback_data == "other_mbtis":
        # 要求用戶重新輸入MBTI
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="請輸入您的 MBTI 類型（例如：INTJ, ENFP 等）。")
        )
