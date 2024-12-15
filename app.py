from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your To-Do List App!"

@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body')
    print("Received an SMS:", incoming_msg)
    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Use dynamic PORT, default to 5000
    app.run(host="0.0.0.0", port=port)
