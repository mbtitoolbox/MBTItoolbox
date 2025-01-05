from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import Event, MessageEvent, TextMessage, PostbackEvent
from mbti import handle_postback  # Import handle_postback from mbti.py

app = Flask(__name__)

# LINE BOT API Initialization
line_bot_api = LineBotApi('your_channel_access_token')
handler = WebhookHandler('your_channel_secret')

@app.route("/", methods=["GET"])
def index():
    return "Welcome to the LINE bot!"

@app.route("/callback", methods=["POST"])
def callback():
    signature = request.headers["X-Line-Signature"]
    body = request.get_data(as_text=True)
    
    try:
        # Validate the LINE webhook signature
        handler.handle(body, signature)

    except Exception as e:
        # Exception handling to show error message
        print(f"Error: {e}")
        abort(400)
    
    return "OK"

# Add a handler for postback events
@handler.add(PostbackEvent)
def handle_postback_event(event):
    handle_postback(event)  # Process the postback event using the imported function

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
