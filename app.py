from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import Event, MessageEvent, TextMessage, PostbackEvent
from mbti import handle_postback  # Import handle_postback from mbti.py

app = Flask(__name__)

# LINE BOT API Initialization
line_bot_api = LineBotApi('ixIjKiibYZdUn4W9ZZAPS5lgAt4JAsxW/nLrnmJWfCu5Vh19nerq/nooyzzsDL0SMr/DwBq+vGhKPWA+p/yzPINc9DvoRJ4f1qWxY2eb+ujWfFPbqx+6Ra0/Jbjh0zg18fqC/Mlak61+EXFkcUECgQdB04t89/1O/w1cDnyilFU=')  # Replace with your actual Channel Access Token
handler = WebhookHandler('3e49258295882026968a5788967a12f1')  # Replace with your actual Channel Secret

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
    print(f"Received postback: {event.postback.data}")  # Log postback data for debugging
    handle_postback(event, line_bot_api)  # Call the handle_postback function

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
