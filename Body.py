# 1. Create a Twilio Account
#    Go to Twilio's website.
#    Sign up and verify your account.
#    Get a Twilio phone number with WhatsApp capabilities. 

# 2. Set Up Python Environment
#    Create a virtual environment:

# 3. Get Twilio Credentials
#    After logging into Twilio, get your Account SID, Auth Token, and WhatsApp-enabled phone number
#    from the Twilio console.

# 4. Build the Flask Application

# 5. Connect Twilio with Flask
#    Twilio needs a publicly accessible URL to send messages to your Flask app. Use a tool like ngrok to expose 
#    your local server to the internet:
#    Take note of the ngrok URL (e.g., https://abc123.ngrok.io).

# 6. Configure Twilio Webhook
#    Go to your Twilio Console -> Messaging -> WhatsApp.
#    Set the Webhook URL to your ngrok URL followed by /whatsapp (e.g., https://abc123.ngrok.io/whatsapp).

# 7. Test Your Chatbot
#    Send a WhatsApp message to your Twilio number (which you set up during the account creation).
#    You should receive responses based on the logic defined in the Flask app.

from flask import Flask, request
from googlesearch import search
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/", methods=["POST"])
def bot():
    user_msg = request.values.get('Body', '').lower()
    response = MessagingResponse()
    q = user_msg + " espn.com"  
    result = [url for url in search(q, num_results=3)]
    msg = response.message(f"--- Results for '{user_msg}' ---")
    for res in result:
        msg.body(res)  
    return str(response)

if __name__ == "__main__":
    app.run()