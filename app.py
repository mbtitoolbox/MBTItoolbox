from flask import Flask, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from mbti import handle_mbtimessages  # Import the MBTI message handler

app = Flask(__name__)

# LINE BOT Configuration
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # Replace with your Channel Access Token
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # Replace with your Channel Secret

@app.route("/")
def home():
    return "Hello, this is the LINE Bot server!"

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers.get('X-Line-Signature')
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        return "Invalid signature", 400
    except Exception as e:
        print(f"Error: {e}")
        return "Internal server error", 500

    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    user_message = event.message.text
    reply_token = event.reply_token

    # Call the MBTI message handler function
    handle_mbtimessages(user_message, reply_token, line_bot_api)

if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0')
