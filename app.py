from flask import Flask, render_template, request
import os
import openai
from dotenv import load_dotenv

app = Flask(__name__)

# Load environment variables from .env file
load_dotenv()

# Set up the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Initialize chat_log list
chat_log = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.form['user_input']
    
    if user_message.lower() == "quit":
        return "Chat session ended."
    else:
        chat_log.append({"role": "user", "content": user_message})
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=chat_log
        )

        assistant_response = response["choices"][0]['message']['content']

        chat_log.append({"role": "assistant", "content": assistant_response.strip("\n").strip()})

        return render_template('response.html', assistant_response=assistant_response.strip("\n").strip())

if __name__ == '__main__':
    app.run()
