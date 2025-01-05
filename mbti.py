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
        # Handle valid MBTI type
        mbti_traits = VALID_MBTI_TYPES[user_message]
        response_message = f"您是 {user_message} 類型！特質是：{mbti_traits}"
    else:
        # Handle invalid input
        response_message = "請輸入您的 MBTI 類型（例如：INTJ, ENFP 等）。"

    # Send the reply to the user
    line_bot_api.reply_message(
        reply_token,
        TextSendMessage(text=response_message)
    )
