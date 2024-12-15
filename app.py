from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to your To-Do List App!"

@app.route('/sms', methods=['POST'])
def sms_reply():
    incoming_msg = request.form.get('Body')
    print("Received an SMS:", incoming_msg)  # This prints the incoming message in your terminal
    resp = MessagingResponse()
    resp.message(f"You said: {incoming_msg}")
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
