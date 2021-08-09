from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import csv
import pandas as pd


from utils import fetch_reply

app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/sms", methods=['POST', 'GET'])
def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    phone_no = request.form.get('From')

    data = [msg, phone_no]

    with open('output.xlsx', 'a', encoding='UTF8', newline='\n') as d:
        df_marks = pd.DataFrame({'Pesan': [msg],
                                 'No HP': [phone_no], })

        writer = pd.ExcelWriter('output.xlsx')
        # write dataframe to excel
        df_marks.to_excel(writer)
        # save the excel
        writer.save()

    reply = fetch_reply(msg, phone_no)

    # Create reply
    resp = MessagingResponse()
    resp.message(reply)

    return str(resp)


if __name__ == "__main__":
    app.run(debug=True)
