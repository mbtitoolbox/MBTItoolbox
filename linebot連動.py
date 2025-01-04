from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import LineBotApiError
from linebot.models import TextMessage, TextSendMessage

app = Flask(__name__)

# Initialize LineBotApi and WebhookHandler with your credentials
line_bot_api = LineBotApi('BIfHpJaliSaaRxAbVXTN+kLoGp40++TW3lv4yqCrjwqJBsVItmCcuoGo6JZr8o/QMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujueAxO/W3WwbmDXC0FTVPrRssFQYcgLb4/tEOyFTjc/AdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('3e49258295882026968a5788967a12f1')

@app.route("/callback", methods=['POST'])
def callback():
    # Get the request body as text
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        # Handle the incoming webhook event
        handler.handle(body, signature)
    except LineBotApiError as e:
        print("Error:", e)

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    # Echo the received message
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="請輸入您的MBTI類型")
    )

if __name__ == "__main__":
    app.run()
