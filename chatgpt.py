import openai
import os

def initialize_openai():
    openai.api_key = os.getenv("OPEN_API_KEY")

def get_chat_response(chat_log, user_message):
    chat_log.append({"role": "user", "content": user_message})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=chat_log
    )
    assistant_response = response["choices"][0]['message']['content']
    return chat_log, assistant_response

