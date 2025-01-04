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
    "ENTP": {
        "description": "ENTP 是一個喜歡挑戰、充滿創意的人，喜歡討論新點子。",
        "愛情": "ENTP 在愛情中富有創意，愛好探索與伴侶的相處方式，對於深刻的情感有著獨特的追求。",
        "人生觀": "ENTP 的人生觀重視挑戰和突破，喜歡在不同的領域中發揮創意和解決問題。"
    },
    "ENFP": {
        "description": "ENFP 是個充滿熱情和創意的夢想家，擅長與人建立深厚的情感聯繫。",
        "愛情": "ENFP 的愛情觀充滿激情和浪漫，期望愛情中的深度連結和自我實現。",
        "人生觀": "ENFP 的人生觀充滿冒險和創意，追求有意義和充滿活力的生活。"
    },
    "ISTJ": {
        "description": "ISTJ 是個踏實可靠，注重規則和紀律的人。",
        "愛情": "ISTJ 對愛情忠誠穩定，習慣以實際行動來表達愛。",
        "人生觀": "ISTJ 的人生觀非常務實，重視責任感和紀律，對未來的計劃有長遠的規劃。"
    },
    "ISFJ": {
        "description": "ISFJ 是個溫和、有責任心的人，擅長照顧他人。",
        "愛情": "ISFJ 對愛情忠誠，會用行動去表達深情。",
        "人生觀": "ISFJ 的人生觀重視穩定與家庭，喜歡在日常中幫助他人並保持秩序。"
    },
    "ESTJ": {
        "description": "ESTJ 是個實際、有組織的人，喜歡管理和領導。",
        "愛情": "ESTJ 在愛情中實際，喜歡透過建立穩定關係來增進互信。",
        "人生觀": "ESTJ 的人生觀注重效率和目標，強調負責任並解決實際問題。"
    },
    "ESFJ": {
        "description": "ESFJ 是個關懷他人，喜歡社交的人。",
        "愛情": "ESFJ 的愛情觀重視家庭和伴侶間的互動，會盡全力讓對方感受到愛。",
        "人生觀": "ESFJ 的人生觀是以服務他人為主，喜歡在社會和人際關係中扮演積極角色。"
    },
    "ISFP": {
        "description": "ISFP 是個內向而藝術感強的人，喜歡享受當下。",
        "愛情": "ISFP 的愛情觀浪漫且自由，對伴侶要求不多，但期望能有心靈的契合。",
        "人生觀": "ISFP 的人生觀強調自由和當下的體驗，重視情感和自我表達。"
    },
    "ISTP": {
        "description": "ISTP 是個冷靜、實用且擅長解決問題的人。",
        "愛情": "ISTP 在愛情中不喜歡表現太多情感，喜歡與伴侶保持某種自由空間。",
        "人生觀": "ISTP 的人生觀充滿實踐和探索，喜歡在現實中解決各種問題。"
    },
    "ENTJ": {
        "description": "ENTJ 是個有領導力且目標導向的人，擅長規劃與決策。",
        "愛情": "ENTJ 的愛情觀務實，會將愛情視為共同努力的事業，期待理性和情感的平衡。",
        "人生觀": "ENTJ 的人生觀非常目標導向，喜歡挑戰並努力達成大規模的成功。"
    },
    "ENFJ": {
        "description": "ENFJ 是個富有同情心、善於領導的人，擅長人際交往。",
        "愛情": "ENFJ 的愛情觀極為熱情和奉獻，會全力以赴地支持和照顧伴侶。",
        "人生觀": "ENFJ 的人生觀關注人際關係和共同目標，喜歡促進他人的成長。"
    },
    "ESTP": {
        "description": "ESTP 是個活躍、冒險且精力充沛的人。",
        "愛情": "ESTP 的愛情觀充滿激情，喜歡快速且直接的關係發展。",
        "人生觀": "ESTP 的人生觀追求刺激和挑戰，喜歡在現實中體驗和解決問題。"
    },
    "ESFP": {
        "description": "ESFP 是個樂觀、社交且喜愛冒險的人。",
        "愛情": "ESFP 的愛情觀充滿浪漫和即興，喜歡豐富多彩的感情體驗。",
        "人生觀": "ESFP 的人生觀充滿樂趣和即時行動，喜歡享受當下並追求新鮮感。"
    },
}


# 用來處理 MBTI 類型訊息的函式
def handle_mbtimessages(user_message, reply_token):
    # 檢查使用者輸入的訊息是否包含兩個MBTI類型
    if len([key for key in mbti_data.keys() if key in user_message]) > 1:
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="請輸入您的MBTI類型（一次只能輸入一個）。")
        )
        return
    
    # 檢查是否是有效的 MBTI 類型
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
        # 如果使用者輸入的不是有效的MBTI類型，回覆提示訊息
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="請輸入您的MBTI類型（例如 INFP）。")
        )
