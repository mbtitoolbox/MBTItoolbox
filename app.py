from linebot.models import MessageEvent, TextMessage, TextSendMessage, QuickReply, QuickReplyButton, MessageAction

# 2. 處理訊息事件
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text.strip()  # 使用者輸入的訊息

    # 3. 根據使用者輸入處理邏輯
    if user_message in BASIC_INFO:  # 如果是有效的 MBTI 類型
        # 取得基本信息
        basic_info = BASIC_INFO.get(user_message, "未找到該類型的基本信息")
        
        # 準備回覆訊息
        reply_text = f"你選擇的是 {user_message}！\n\n{basic_info}\n\n想了解更多關於 {user_message} 的資訊嗎？"
        
        # 準備快速回覆選項
        quick_reply = QuickReply(
            items=[
                QuickReplyButton(action=MessageAction(label="愛情", text=f"愛情 {user_message}")),
                QuickReplyButton(action=MessageAction(label="工作", text=f"工作 {user_message}")),
                QuickReplyButton(action=MessageAction(label="優缺點", text=f"優缺點 {user_message}"))
            ]
        )
        
        # 發送包含選項的訊息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text, quick_reply=quick_reply)
        )
    
    else:
        reply_text = "請輸入有效的 MBTI 類型！（例如：ENFP, INTJ, ISFJ）"
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=reply_text)
        )

# 處理用戶選擇的愛情、工作或優缺點訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_detail_selection(event):
    user_message = event.message.text.strip()

    if user_message.startswith("愛情") or user_message.startswith("工作") or user_message.startswith("優缺點"):
        mbti_type = user_message.split(" ")[1]  # 提取 MBTI 類型
        info_type = user_message.split(" ")[0]  # 提取選項：愛情、工作、優缺點
        
        # 獲取詳細信息
        detail_info = get_more_info(mbti_type, info_type)
        
        # 發送詳細信息
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=detail_info)
        )
