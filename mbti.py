from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction

VALID_MBTI_TYPES = {
    "INTJ": {"trait": "戰略家，具有強烈的規劃能力與遠見。", "love": "愛情中的 INTJ 是理性且有原則的，通常比較慢熱但會深思熟慮。", "work": "工作中的 INTJ 擅長長期規劃，有極強的獨立性與目標感。", "pros_cons": "優點：邏輯強，分析能力強；缺點：過於冷靜，對情感不敏感。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "INTP": {"trait": "哲學家，喜歡分析與深度思考。", "love": "愛情中的 INTP 喜歡理性分析，有時表現出來比較冷淡。", "work": "工作中的 INTP 喜歡獨立思考，擅長解決複雜問題。", "pros_cons": "優點：思維深邃，創新；缺點：難以表達情感，容易冷漠。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ENTJ": {"trait": "指揮官，擅長領導與組織。", "love": "愛情中的 ENTJ 充滿魅力，具領導性，但有時可能過於強勢。", "work": "工作中的 ENTJ 善於組織與管理，是天然的領袖。", "pros_cons": "優點：領導力強，目標導向；缺點：過於直率，容易冷漠。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ENTP": {"trait": "辯論家，愛好討論與創新。", "love": "愛情中的 ENTP 喜歡挑戰，對感情有很強的探索欲。", "work": "工作中的 ENTP 擅長創新與解決問題，總是充滿活力。", "pros_cons": "優點：創意無限，思維敏捷；缺點：容易拖延，不夠穩定。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "INFJ": {"trait": "提倡者，具有強烈的理想主義與洞察力。", "love": "愛情中的 INFJ 是深情的，他們會把情感放在第一位。", "work": "工作中的 INFJ 喜歡幫助他人，並且總是尋找更有意義的工作。", "pros_cons": "優點：同理心強，有遠見；缺點：過於理想化，容易感到失望。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "INFP": {"trait": "調解者，深具同理心與創造力。", "love": "愛情中的 INFP 深情且理想化，但可能過於幻想。", "work": "工作中的 INFP 喜歡創造有意義的工作，並關心他人。", "pros_cons": "優點：富有創造力，同理心強；缺點：過於理想化，缺乏現實感。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ENFJ": {"trait": "主人公，具強大的領導力與同理心。", "love": "愛情中的 ENFJ 是充滿熱情與承諾的伴侶。", "work": "工作中的 ENFJ 是天生的領袖，並且重視團隊合作。", "pros_cons": "優點：有領導力，富有同理心；缺點：有時過於理想化，忽視自身需要。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ENFP": {"trait": "倡導者，樂觀開朗，充滿創意。", "love": "愛情中的 ENFP 充滿熱情，總是尋找情感的深度。", "work": "工作中的 ENFP 富有創意，並且在團隊中能帶來活力。", "pros_cons": "優點：充滿創意，富有熱情；缺點：容易焦慮，缺乏耐性。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ISTJ": {"trait": "檢察官，注重實際，忠誠可靠。", "love": "愛情中的 ISTJ 是穩定且忠誠的伴侶，雖然有時表現得比較內向。", "work": "工作中的 ISTJ 是極其負責且注重細節，擅長實施規劃。", "pros_cons": "優點：務實，忠誠；缺點：過於保守，缺乏靈活性。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ISFJ": {"trait": "守護者，富有同理心，注重他人。", "love": "愛情中的 ISFJ 是溫柔的，並且極為關心伴侶的需求。", "work": "工作中的 ISFJ 具有極高的責任心，並且注重細節。", "pros_cons": "優點：務實，有同理心；缺點：過於保守，易受壓力。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ESTJ": {"trait": "執行者，具組織能力，注重規範。", "love": "愛情中的 ESTJ 是直接且實際的，會努力保證伴侶的需求。", "work": "工作中的 ESTJ 喜歡計劃和管理，並且擅長領導。", "pros_cons": "優點：實際，負責；缺點：有時過於固執，不善於應對變化。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ESFJ": {"trait": "提供者，注重他人，喜歡社交。", "love": "愛情中的 ESFJ 充滿關懷，並且總是為伴侶提供支持。", "work": "工作中的 ESFJ 喜歡幫助他人，並且在團隊中扮演重要角色。", "pros_cons": "優點：關心他人，社交能力強；缺點：過度依賴他人意見，缺乏獨立性。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ISTP": {"trait": "工匠，務實且具有動手能力。", "love": "愛情中的 ISTP 喜歡保持空間，但也有深厚的情感。", "work": "工作中的 ISTP 喜歡動手操作，並且總是尋找實際解決方案。", "pros_cons": "優點：務實，解決問題能力強；缺點：不擅長表達情感，缺乏耐性。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ISFP": {"trait": "冒險家，感性且喜歡自由。", "love": "愛情中的 ISFP 充滿浪漫，但可能會比較害羞。", "work": "工作中的 ISFP 創造力豐富，喜歡自由的環境。", "pros_cons": "優點：有創造力，感性；缺點：缺乏規劃，容易感到無聊。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ESTP": {"trait": "促動者，喜歡刺激，善於應對挑戰。", "love": "愛情中的 ESTP 充滿熱情，且喜歡挑戰與刺激。", "work": "工作中的 ESTP 喜歡即時解決問題，並且總是能找到最直接的解決辦法。", "pros_cons": "優點：解決問題能力強，果斷；缺點：容易衝動，忽視後果。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"},
    "ESFP": {"trait": "表演者，充滿活力，喜歡社交。", "love": "愛情中的 ESFP 喜歡與伴侶共享美好時光，充滿激情。", "work": "工作中的 ESFP 喜歡與人互動，並且充滿創意。", "pros_cons": "優點：熱情，創意；缺點：過於衝動，容易焦慮。", "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"}
}


def handle_postback(event, line_bot_api):
    postback_data = event.postback.data
    reply_token = event.reply_token
    data = postback_data.split('_')
    action = data[0]
    mbti_type = data[1] if len(data) > 1 else None

    if mbti_type and mbti_type in VALID_MBTI_TYPES:
        mbti_data = VALID_MBTI_TYPES[mbti_type]

        if action == 'love':
            response_message = f"關於 {mbti_type} 的愛情：{mbti_data['love']}"
        elif action == 'work':
            response_message = f"關於 {mbti_type} 的工作：{mbti_data['work']}"
        elif action == 'pros_cons':
            response_message = f"關於 {mbti_type} 的優缺點：{mbti_data['pros_cons']}"
        else:
            response_message = "無效的操作，請再試一次。"
    else:
        response_message = "請輸入有效的 MBTI 類型，例如：ENFP、INTJ、ISFP 等。"

    line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))

    # 發送按鈕模板
    if mbti_type in VALID_MBTI_TYPES:
        mbti_image_url = VALID_MBTI_TYPES[mbti_type].get('image_url', '')  
        buttons_template = ButtonsTemplate(
            title=f"更多關於{mbti_type}",
            text=f"想了解更多關於 {mbti_type} 的內容？",
            thumbnail_image_url=mbti_image_url if mbti_image_url else "https://example.com/default_image.jpg",
            actions=[
                PostbackAction(label=f"想了解更多關於{mbti_type}愛情", data=f"love_{mbti_type}"),
                PostbackAction(label=f"想了解更多關於{mbti_type}工作", data=f"work_{mbti_type}"),
                PostbackAction(label=f"想了解{mbti_type}的優缺點", data=f"pros_cons_{mbti_type}"),
                PostbackAction(label="想了解其他MBTI類型", data="other_mbtis")
            ]
        )
        line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text=f"更多關於{mbti_type}", template=buttons_template))
