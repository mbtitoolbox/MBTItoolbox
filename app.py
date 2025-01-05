from flask import Flask, request, jsonify
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, PostbackEvent, PostbackAction, TextSendMessage, ButtonsTemplate, MessageAction

import mbti  # 导入自定义的mbti数据和函数

app = Flask(__name__)

line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3e49258295882026968a5788967a12f1')

# 用户初始输入的MBTI类型
user_mbti = None

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    
    # 处理消息事件
    handler.handle(body, signature)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    global user_mbti
    
    user_message = event.message.text.strip().upper()  # 获取用户消息并标准化为大写
    
    # 用户输入MBTI类型
    if user_mbti is None:
        if user_message in mbti.MBTI_TYPES:  # 检查用户输入的是否为有效的MBTI类型
            user_mbti = user_message
            mbti_info = mbti.get_basic_info(user_mbti)  # 获取MBTI基本信息
            buttons = ButtonsTemplate(
                title="想了解更多？", text=mbti_info, actions=[
                    PostbackAction(label="想了解更多關於" + user_mbti, data="more_info_" + user_mbti),
                    PostbackAction(label="想了解其他MBTI類型", data="other_mbti")
                ]
            )
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入您想了解的MBTI"))
            line_bot_api.reply_message(event.reply_token, buttons)
        else:
            line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入有效的MBTI類型，例如：ENFP"))
    
    # 用户选择选项
    elif "more_info_" in user_message:
        mbti_info_details = mbti.get_more_info(user_mbti)  # 获取详细信息
        buttons = ButtonsTemplate(
            title="更多信息", text=mbti_info_details, actions=[
                MessageAction(label="愛情", text="愛情"),
                MessageAction(label="工作", text="工作"),
                MessageAction(label="優缺點", text="優缺點")
            ]
        )
        line_bot_api.reply_message(event.reply_token, buttons)
    
    # 用户选择“想了解其他MBTI类型”
    elif user_message == "想了解其他MBTI類型":
        user_mbti = None
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入您想了解的MBTI"))

@handler.add(PostbackEvent)
def handle_postback(event):
    # 处理postback选项
    data = event.postback.data
    
    if "more_info_" in data:  # 用户点击更多信息
        mbti_info_details = mbti.get_more_info(user_mbti)  # 获取更多MBTI信息
        buttons = ButtonsTemplate(
            title="更多信息", text=mbti_info_details, actions=[
                MessageAction(label="愛情", text="愛情"),
                MessageAction(label="工作", text="工作"),
                MessageAction(label="優缺點", text="優缺點")
            ]
        )
        line_bot_api.reply_message(event.reply_token, buttons)

    elif data == "other_mbti":  # 用户想了解其他MBTI类型
        user_mbti = None
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text="請輸入您想了解的MBTI"))

if __name__ == "__main__":
    app.run(debug=True)
