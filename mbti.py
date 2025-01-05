# 定義MBTI類型列表
MBTI_TYPES = [
    'ISTP', 'ISFP', 'ESTP', 'ENFP', 'INFP', 'ENFJ', 'INFJ', 'ESTJ', 'ISTJ',
    'ENTP', 'INTP', 'ESFP', 'ISFJ', 'INTJ', 'ESFJ', 'ENTJ'
]

# 每種MBTI類型的基本信息
BASIC_INFO = {
    "ENFP": "ENFP是一個充滿活力且富有創造力的人，通常熱愛冒險和挑戰。",
    "INFP": "INFP是理想主義者，常常在內心追求更高的目標。",
    "ESTP": "ESTP是一個行動派，喜歡探索世界的多樣性。",
    "ISTP": "ISTP是實踐者，通常理性冷靜，喜愛解決實際問題。",
    "ISFP": "ISFP是感性且充滿藝術氣息的人，追求內心的寧靜。",
    "ENFJ": "ENFJ是天生的領袖，善於理解他人的需求並提供幫助。",
    "INFJ": "INFJ通常是理想主義者，注重他人的情感，擅長理解複雜的情境。",
    "ESTJ": "ESTJ是務實且有組織的人，喜歡保持秩序並遵循傳統。",
    "ISTJ": "ISTJ是非常細緻和有責任感的人，喜歡在穩定的環境中工作。",
    "ENTP": "ENTP是創新者和辯論者，善於提出新穎的想法並挑戰現有的框架。",
    "INTP": "INTP通常是邏輯型和深思熟慮的思想家，喜愛獨立思考。",
    "ESFP": "ESFP是社交達人，喜愛與人交往並享受生活的每一刻。",
    "ISFJ": "ISFJ是體貼和忠誠的人，擅長關心他人的需求。",
    "INTJ": "INTJ是戰略家和規劃者，注重未來和自我完善。",
    "ESFJ": "ESFJ是熱情而關心他人的人，喜愛組織社交活動。",
    "ENTJ": "ENTJ是自信且果敢的領導者，善於組織和決策。"
}

# 每種MBTI類型的更多詳細信息
MORE_INFO = {
    "ENFP": {
        "愛情": "ENFP在愛情中非常浪漫，渴望激情與自由。",
        "工作": "ENFP在工作中充滿創造力，喜歡探索新領域。",
        "優缺點": "優點：有創造力、善於溝通；缺點：容易分心、缺乏耐性。",
    },
    "INFP": {
        "愛情": "INFP在愛情中忠誠且理想化，渴望找到心靈契合的人。",
        "工作": "INFP在工作中追求意義，通常更傾向於藝術或社會服務領域。",
        "優缺點": "優點：有同理心、深思熟慮；缺點：過於理想化、過度內省。",
    },
    "ESTP": {
        "愛情": "ESTP在愛情中充滿熱情，喜歡挑戰和冒險。",
        "工作": "ESTP在工作中行動迅速，善於處理緊急情況。",
        "優缺點": "優點：果斷、應變能力強；缺點：衝動、缺乏耐性。",
    },
    # 添加其餘 MBTI 類型的詳細信息...
}

def get_basic_info(mbti_type):
    """
    根據MBTI類型返回基本信息
    :param mbti_type: MBTI類型（例如ENFP）
    :return: 該類型的基本信息
    """
    return BASIC_INFO.get(mbti_type, "未找到該類型的基本信息")

def get_more_info(mbti_type, info_type):
    """
    根據MBTI類型返回更多的詳細信息（愛情、工作、優缺點）
    :param mbti_type: MBTI類型（例如ENFP）
    :param info_type: 使用者選擇的詳細信息類型（例如：愛情、工作、優缺點）
    :return: 該類型的相關信息
    """
    more_info = MORE_INFO.get(mbti_type, {})
    return more_info.get(info_type, f"未找到關於{info_type}的信息")

def main():
    """
    主程式：模擬用戶與系統的互動
    """
    while True:
        print("請輸入您想了解的MBTI類型（例如ENFP），或輸入'退出'結束：")
        mbti_type = input().strip().upper()
        if mbti_type == "退出":
            print("感謝使用MBTI查詢系統，再見！")
            break

        if mbti_type not in MBTI_TYPES:
            print("無效的MBTI類型，請重新輸入。")
            continue

        print(get_basic_info(mbti_type))
        print("\n是否想了解更多？請選擇（愛情、工作、優缺點），或輸入'返回'返回：")
        
        while True:
            info_type = input().strip()
            if info_type == "返回":
                break
            print(get_more_info(mbti_type, info_type))

if __name__ == "__main__":
    main()
