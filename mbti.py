from linebot.models import TextSendMessage, TemplateSendMessage, ButtonsTemplate, PostbackAction


VALID_MBTI_TYPES = {
    "INTJ": {
        "trait": "戰略家，具有強烈的規劃能力與遠見。",
        "love": "愛情中的 INTJ 是理性且有原則的，通常比較慢熱但會深思熟慮。",
        "work": "工作中的 INTJ 擅長長期規劃，有極強的獨立性與目標感。",
        "pros_cons": "優點：邏輯強，分析能力強；缺點：過於冷靜，對情感不敏感。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ENTP": {
        "trait": "辯論家，愛好討論與創新。",
        "love": "愛情中的 ENTP 喜歡挑戰，對感情有很強的探索欲。",
        "work": "工作中的 ENTP 擅長創新與解決問題，總是充滿活力。",
        "pros_cons": "優點：創意無限，思維敏捷；缺點：容易拖延，不夠穩定。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "INFP": {
        "trait": "理想主義者，追求內心的價值觀與真理。",
        "love": "愛情中的 INFP 是深情且忠誠的，尋求與另一半的心靈契合。",
        "work": "工作中的 INFP 具有創意，通常會尋求能夠帶來意義的工作。",
        "pros_cons": "優點：富有同情心，具有理想；缺點：過於理想化，難以應對現實。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ENFP": {
        "trait": "探索者，充滿熱情，追求新奇與挑戰。",
        "love": "愛情中的 ENFP 是富有浪漫和冒險精神的，總是追求激情與新鮮感。",
        "work": "工作中的 ENFP 喜歡多變與創新，能夠應對各種不同的情境。",
        "pros_cons": "優點：充滿活力，創意無窮；缺點：容易分心，缺乏長期計劃。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "INFJ": {
        "trait": "提倡者，具有深刻的洞察力和理想主義。",
        "love": "愛情中的 INFJ 需要深層的情感聯繫，他們會以全心全意的方式去愛。",
        "work": "工作中的 INFJ 會尋求能夠帶來改變的工作，並且有強烈的使命感。",
        "pros_cons": "優點：同理心強，有洞察力；缺點：過於理想，容易過度付出。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ISFP": {
        "trait": "冒險家，隨性且享受當下。",
        "love": "愛情中的 ISFP 是敏感且浪漫的，喜歡在平靜的環境中建立深厚的感情。",
        "work": "工作中的 ISFP 喜歡靈活性，會在藝術或創意領域找到成就感。",
        "pros_cons": "優點：感性，善解人意；缺點：容易逃避現實，缺乏規劃。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ESFP": {
        "trait": "表演者，充滿活力和魅力。",
        "love": "愛情中的 ESFP 喜歡表達情感，會積極地展示愛與關懷。",
        "work": "工作中的 ESFP 追求活躍的環境，樂於與人合作。",
        "pros_cons": "優點：樂觀，擅長社交；缺點：容易分心，缺乏耐心。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ISTJ": {
        "trait": "檢查員，注重細節與秩序。",
        "love": "愛情中的 ISTJ 是忠誠且穩定的，他們會在穩定的環境中尋求幸福。",
        "work": "工作中的 ISTJ 追求效率和精確性，適合有結構和規範的工作。",
        "pros_cons": "優點：負責任，踏實；缺點：過於保守，缺乏創新。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ESTJ": {
        "trait": "主管，注重規則與效率。",
        "love": "愛情中的 ESTJ 是有責任心且實際的，他們看重穩定和可靠。",
        "work": "工作中的 ESTJ 擅長管理和組織，追求目標導向和成就。",
        "pros_cons": "優點：堅持原則，有領導力；缺點：過於控制，忽略他人感受。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ISFJ": {
        "trait": "守護者，關心他人並注重責任。",
        "love": "愛情中的 ISFJ 是深情且關懷的，會把另一半放在心中最重要的位置。",
        "work": "工作中的 ISFJ 重視穩定性和團隊合作，善於處理細節和照顧他人。",
        "pros_cons": "優點：忠誠，有責任心；缺點：過於自我犧牲，容易忽略自身需要。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ESFJ": {
        "trait": "提供者，樂於助人並追求和諧。",
        "love": "愛情中的 ESFJ 是溫暖且體貼的，會在關係中付出很多。",
        "work": "工作中的 ESFJ 喜歡幫助他人，適合服務型或人際關係密切的工作。",
        "pros_cons": "優點：熱情，善於溝通；缺點：過於依賴他人看法，容易忽視自己的需要。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ISTP": {
        "trait": "工匠，喜歡動手操作和解決問題。",
        "love": "愛情中的 ISTP 是理性且獨立的，對於情感表達較為內斂。",
        "work": "工作中的 ISTP 喜歡解決問題，擅長實務和技術。",
        "pros_cons": "優點：冷靜，實際；缺點：情感疏遠，難以表達自己。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ESTP": {
        "trait": "冒險家，喜歡挑戰和感官刺激。",
        "love": "愛情中的 ESTP 直接且熱情，喜歡冒險和新鮮感。",
        "work": "工作中的 ESTP 具有行動力，喜歡即時解決問題，並且充滿競爭心。",
        "pros_cons": "優點：果斷，適應力強；缺點：衝動，缺乏規劃。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "INTP": {
        "trait": "思想家，充滿好奇心並專注於理論。",
        "love": "愛情中的 INTP 是理性且稍顯冷漠的，往往將愛情視為理性探索。",
        "work": "工作中的 INTP 喜歡挑戰性的任務，並能在獨立的環境中表現出色。",
        "pros_cons": "優點：邏輯思維強，創新；缺點：情感表達冷漠，容易忽略他人感受。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    },
    "ENTJ": {
        "trait": "指揮官，具有強烈的領導力和決策能力。",
        "love": "愛情中的 ENTJ 是主導且有組織感，會在關係中付出很多。",
        "work": "工作中的 ENTJ 天生領袖，擅長帶領團隊並且對達成目標有強烈的決心。",
        "pros_cons": "優點：果斷，領導力強；缺點：過於控制，對細節缺乏耐心。",
        "image_url": "https://cdn-www.cw.com.tw/article/202406/article-667b8765d63ad9.19226580.jpg"
    }
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

    try:
        # 嘗試發送訊息
        line_bot_api.reply_message(reply_token, TextSendMessage(text=response_message))
    except Exception as e:
        # 如果發送訊息時出現錯誤，打印錯誤訊息
        print(f"Error sending message: {e}")

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
        try:
            # 嘗試發送模板消息
            line_bot_api.reply_message(reply_token, TemplateSendMessage(alt_text=f"更多關於{mbti_type}", template=buttons_template))
        except Exception as e:
            # 如果發送訊息時出現錯誤，打印錯誤訊息
            print(f"Error sending template message: {e}")
