# 定义一个字典，包含所有16种MBTI类型
MBTI_TYPES = [
    'ISTP', 'ISFP', 'ESTP', 'ENFP', 'INFP', 'ENFJ', 'INFJ', 'ESTJ', 'ISTJ', 
    'ENTP', 'INTP', 'ESFP', 'ISFJ', 'INTJ', 'ESFJ', 'ENTJ'
]

# 每种MBTI类型的基本信息（如性格特点）
BASIC_INFO = {
    "ENFP": "ENFP是一个充满活力且富有创造力的人，通常热爱冒险和挑战。",
    "INFP": "INFP是理想主义者，常常在内心追求更高的目标。",
    "ESTP": "ESTP是一个行动派，喜欢探索世界的多样性。",
    "ISTP": "ISTP是实践者，通常理性冷静，喜爱解决实际问题。",
    "ISFP": "ISFP是感性且充满艺术气息的人，追求内心的宁静。",
    "ENFJ": "ENFJ是天生的领袖，善于理解他人的需求并提供帮助。",
    "INFJ": "INFJ通常是理想主义者，注重他人的情感，擅长理解复杂的情境。",
    "ESTJ": "ESTJ是务实且有组织的人，喜欢保持秩序并遵循传统。",
    "ISTJ": "ISTJ是非常细致和有责任感的人，喜欢在稳定的环境中工作。",
    "ENTP": "ENTP是创新者和辩论者，善于提出新颖的想法并挑战现有的框架。",
    "INTP": "INTP通常是逻辑型和深思熟虑的思想家，喜爱独立思考。",
    "ESFP": "ESFP是社交达人，喜爱与人交往并享受生活的每一刻。",
    "ISFJ": "ISFJ是体贴和忠诚的人，擅长关心他人的需求。",
    "INTJ": "INTJ是战略家和规划者，注重未来和自我完善。",
    "ESFJ": "ESFJ是热情而关心他人的人，喜爱组织社交活动。",
    "ENTJ": "ENTJ是自信且果敢的领导者，善于组织和决策。"
}

# 每种MBTI类型的更多详细信息（如爱情、工作、优缺点等）
MORE_INFO = {
    "ENFP": {
        "爱情": "ENFP在爱情中非常浪漫，渴望激情与自由。",
        "工作": "ENFP在工作中充满创造力，喜欢探索新领域。",
        "优缺点": "优点：有创造力、善于沟通；缺点：容易分心、缺乏耐心。",
    },
    "INFP": {
        "爱情": "INFP在爱情中忠诚且理想化，渴望找到心灵契合的人。",
        "工作": "INFP在工作中追求意义，通常更倾向于艺术或社会服务领域。",
        "优缺点": "优点：有同理心、深思熟虑；缺点：过于理想化、过度内省。",
    },
    "ESTP": {
        "爱情": "ESTP在爱情中充满热情，喜欢挑战和冒险。",
        "工作": "ESTP在工作中行动迅速，善于处理紧急情况。",
        "优缺点": "优点：果断、应变能力强；缺点：冲动、缺乏耐性。",
    },
    # 更多类型的数据
}

# 获取某个MBTI类型的基本信息
def get_basic_info(mbti_type):
    """
    根据MBTI类型返回基本信息
    :param mbti_type: MBTI类型（例如ENFP）
    :return: 该类型的基本信息
    """
    return BASIC_INFO.get(mbti_type, "未找到该类型的基本信息")

# 获取某个MBTI类型的更多详细信息（包括爱情、工作、优缺点等）
def get_more_info(mbti_type):
    """
    根据MBTI类型返回更多的详细信息
    :param mbti_type: MBTI类型（例如ENFP）
    :return: 该类型的更多信息（爱情、工作、优缺点）
    """
    more_info = MORE_INFO.get(mbti_type, {})
    if not more_info:
        return "未找到该类型的详细信息"

    info = ""
    for key, value in more_info.items():
        info += f"{key}：{value}\n"
    return info

