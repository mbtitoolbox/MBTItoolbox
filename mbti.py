from linebot.models import TextSendMessage
from linebot import LineBotApi

# LINE BOT 配置 (再次在這個檔案中初始化)
line_bot_api = LineBotApi('YOUR_CHANNEL_ACCESS_TOKEN')  # 替換為您的 Channel Access Token

# 儲存16種MBTI類型及其回覆內容
mbti_data = {
    "INFP": "INFP 是個好人，富有同情心和理想主義。",
    "ENTP": "ENTP 是富有創造力且善於辯論的人。",
    "INTP": "INTP 是邏輯性強的思想家，喜歡探索未知。",
    "INFJ": "INFJ 是充滿理想主義的深思熟慮者。",
    "ENFP": "ENFP 是充滿活力的創造者，富有直覺和探索精神。",
    "INTJ": "INTJ 是策略家，喜歡追求目標並計劃未來。",
    "ISFP": "ISFP 是藝術家，熱愛自由且注重感官享受。",
    "ESTP": "ESTP 是冒險者，喜歡挑戰現狀並活在當下。",
    "ESFP": "ESFP 是表演者，喜歡社交並尋求樂趣。",
    "ISTP": "ISTP 是技術專家，喜歡動手解決問題。",
    "ISFJ": "ISFJ 是守護者，重視責任和他人的需求。",
    "ESTJ": "ESTJ 是領導者，重視秩序和結構。",
    "ESFJ": "ESFJ 是支援者，喜歡幫助他人並促進和諧。",
    "ISTJ": "ISTJ 是負責任的執行者，重視傳統和規則。",
    "ENFJ": "ENFJ 是導師，關心他人並鼓勵他們成長。",
}

# 處理 Line 消息
def handle_mbtimessages(event):
    user_message = event.message.text
    reply_token = event.reply_token

    if user_message in mbti_data:
        # 回覆MBTI類型的詳細資訊
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text=mbti_data[user_message])
        )
    else:
        # 如果輸入無效，回覆提示
        line_bot_api.reply_message(
            reply_token,
            TextSendMessage(text="「請輸入您的MBTI類型」")
        )
