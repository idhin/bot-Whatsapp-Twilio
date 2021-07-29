from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import csv

from utils import fetch_reply

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    # f = open("tests.txt", "w")
    # f.write(phone_no + " pesannya : " + msg)
    # f.close()

    # header = ['nomor HP', 'pesan']
    data = [msg, phone_no]

    with open('hasil.csv', 'a', encoding='UTF8', newline='\n') as f:
        writer = csv.writer(f)

        # write the header
        # writer.writerow(header)

        # write the data
        writer.writerow(data)

    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
