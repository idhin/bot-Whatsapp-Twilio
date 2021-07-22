import dialogflow_v2 as dialogflow
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "hale-sequence-319816-c5c21beb823a.json"

dialogflow_session_client = dialogflow.SessionsClient()
PROJECT_ID = "hale-sequence-319816"


def detect_intent_from_text(text, session_id, language_code='en'):
    session = dialogflow_session_client.session_path(PROJECT_ID, session_id)
    text_input = dialogflow.types.TextInput(
        text=text, language_code=language_code)
    query_input = dialogflow.types.QueryInput(text=text_input)
    response = dialogflow_session_client.detect_intent(
        session=session, query_input=query_input)
    return response.query_result


def fetch_reply(query, session_id):
    response = detect_intent_from_text("order firli", 12314)
    return response.fulfillment_text
