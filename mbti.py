from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction

# 定義 16 個 MBTI 類型及其相關資料
VALID_MBTI_TYPES = {
    "INTJ": {
        "description": "戰略家，具有強烈的規劃能力與遠見。",
        "love": "INTJ 喜歡理性分析，對感情較為理智，較難表達情感，但對忠誠和長期關係有深刻的理解。",
        "work": "INTJ 工作上有高度的規劃能力，適合領導與規劃，追求卓越與高效率。",
        "pros_cons": "優點：冷靜理智，擅長策略規劃，缺點：對人情世故缺乏感知，可能顯得冷漠。"
    },
    "INTP": {
        "description": "哲學家，喜歡分析與深度思考。",
        "love": "INTP 喜歡理性思考和深度交流，對感情投入較為理智，追求心靈上的契合。",
        "work": "INTP 擅長分析，適合技術性或研究類工作，喜歡獨立思考和創新。",
        "pros_cons": "優點：創新、善於解決問題，缺點：過於理性，可能缺乏情感表達。"
    },
    "ENTJ": {
        "description": "指揮官，領導力與執行力出色。",
        "love": "ENTJ 在愛情中通常很直接，追求明確的目標，可能會對伴侶提出挑戰。",
        "work": "ENTJ 是天生的領導者，擅長制定戰略與達成目標，追求權力與控制。",
        "pros_cons": "優點：有遠見、執行力強，缺點：過於強勢，冷漠，可能忽略他人感受。"
    },
    "ENFP": {
        "description": "競選者，充滿熱情與想像力。",
        "love": "ENFP 在愛情中充滿激情，喜歡深入交流，熱衷於探索新鮮的事物。",
        "work": "ENFP 善於激勵他人，適合創意與人際互動的工作，具有強大的直覺力。",
        "pros_cons": "優點：有創意，熱情，能夠啟發他人，缺點：缺乏耐心，容易分心，對細節不夠關注。"
    },
    "ENFJ": {
        "description": "教導者，關心他人並致力於改善世界。",
        "love": "ENFJ 充滿熱情和關懷，會主動關心伴侶的情感需求，並為伴侶付出。",
        "work": "ENFJ 擅長人際互動，適合領導和教育領域，能夠感知他人需求並加以改變。",
        "pros_cons": "優點：富有同理心，擅長激勵他人，缺點：過於關心他人，可能忽略自己需求。"
    },
    "ISFJ": {
        "description": "守護者，謹慎且忠誠。",
        "love": "ISFJ 在愛情中比較內斂，但對伴侶非常忠誠，願意為關係付出。",
        "work": "ISFJ 擅長執行細節，適合照顧他人的職業，忠於自己的責任。",
        "pros_cons": "優點：細心、忠誠、負責任，缺點：容易被他人利用，對改變較為抗拒。"
    },
    "ISFP": {
        "description": "冒險家，喜歡探索並享受當下。",
        "love": "ISFP 喜歡自由，對愛情充滿浪漫，但有時不太願意表達情感。",
        "work": "ISFP 通常喜歡藝術性或創意型的工作，享受自己獨特的表達方式。",
        "pros_cons": "優點：敏感、善良，缺點：容易受情感波動影響，對現實缺乏規劃。"
    },
    "INFJ": {
        "description": "顧問，具備直覺與深刻洞察力。",
        "love": "INFJ 在愛情中尋求深刻的心靈契合，對愛情有高度的理想化要求。",
        "work": "INFJ 善於理解他人，適合從事幫助他人的職業，並且對事業有遠見。",
        "pros_cons": "優點：具深度、富有同理心，缺點：對自己和他人要求過高，容易感到孤獨。"
    },
    "INFP": {
        "description": "調解者，充滿理想與追求真理的心。",
        "love": "INFP 對愛情充滿幻想，忠誠且浪漫，喜歡與伴侶深入心靈交流。",
        "work": "INFP 擅長創造性和人文領域的工作，追求自己心中的理想。",
        "pros_cons": "優點：富有理想、創意，缺點：容易陷入情緒化和過於理想化。"
    },
    "ESTJ": {
        "description": "執行者，堅持秩序與責任。",
        "love": "ESTJ 在愛情中追求穩定與秩序，會主動照顧和保護伴侶。",
        "work": "ESTJ 善於管理和執行，適合領導型或組織管理型的工作。",
        "pros_cons": "優點：實事求是，負責任，缺點：過於固守規範，對變化不夠開放。"
    },
    "ESTP": {
        "description": "挑戰者，喜歡冒險與即時行動。",
        "love": "ESTP 在愛情中直率、開放，喜歡刺激和新鮮感。",
        "work": "ESTP 善於應對快速變化的環境，適合需要即時反應的工作。",
        "pros_cons": "優點：果斷、充滿活力，缺點：容易衝動、缺乏長遠計劃。"
    },
    "ESFJ": {
        "description": "社交者，注重他人需求與和諧。",
        "love": "ESFJ 在愛情中尋求穩定，會為伴侶付出並保持關係和諧。",
        "work": "ESFJ 擅長協作，適合以團隊為導向的工作，致力於促進和諧與合作。",
        "pros_cons": "優點：樂於助人，組織能力強，缺點：過於關心他人看法，可能過於依賴外界認可。"
    },
    "ESFP": {
        "description": "表演者，喜歡社交與享受當下。",
        "love": "ESFP 在愛情中追求快樂和激情，喜歡與伴侶共享美好時光。",
        "work": "ESFP 喜歡富有創意且互動性的工作，適合表現型或人際互動工作。",
        "pros_cons": "優點：樂觀、充滿活力，缺點：容易忽略長期規劃，過於衝動。"
    },
    "ENFJ": {
        "description": "指導者，具有強大的影響力和領導能力。",
        "love": "ENFJ 在愛情中非常關心伴侶，願意為了愛情做出巨大努力。",
        "work": "ENFJ 擅長領導，能夠激勵他人達成共同目標，對於他人需求十分敏感。",
        "pros_cons": "優點：具同理心，擅長激勵他人，缺點：有時會忽視自己的需求。"
    }
}

def handle_mbtimessages(user_message, reply_token, line_bot_api):
    """
    處理用戶發送的 MBTI 類型消息
    """
    user_message = user_message.strip().upper()

    if user_message in VALID_MBTI_TYPES:
        mbti_data = VALID_MBTI_TYPES[user_message]
        response_message = f"您是 {user_message} 類型！特質是：{mbti_data['description']}"

        # 根據用戶輸入的MBTI類型生成按鈕模板
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

        # 發送MBTI特質和按鈕模板
        line_bot_api.reply_message(
            reply_token,
            [
                TextSendMessage(text=response_message),
                TemplateSendMessage(alt_text=f"更多關於{user_message}", template=buttons_template)
            ]
        )
    else:
        # 無效的MBTI類型
        response_message = "請輸入您的 MBTI 類型（例如：INTJ, ENFP 等）。"
        line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))

def handle_post
