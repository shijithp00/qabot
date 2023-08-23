import openai
from flask import Flask, jsonify, request, render_template
import os

keys = os.getenv('OPENAI_KEY')
api_key = keys

app = Flask(__name__)
openai.api_key = api_key

# Function to generate chatbot response
def generate_chat_response(user_input):
    prompt = user_input
    # Create a chat completion request using OpenAI's GPT-3.5 Turbo model
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are an AI assistant."},
            {"role": "user", "content": prompt}
        ]
    )
    # Extract the generated chat response from the API response
    chat_response = response['choices'][0]['message']['content'].strip()
    return chat_response

# Route for handling chat requests
@app.route("/chat", methods=["POST"])
def chat():
    # Get the user input from the request
    user_input = request.json["user_input"]  
    # Generate chatbot response using the user input
    chat_response = generate_chat_response(user_input)
    response_data = {"response": chat_response}
    return jsonify(response_data)


@app.route("/")
@app.route("/index.html")
def index():
    # Render the index.html template
    return render_template("index.html")  

if __name__ == "__main__":
    app.run(host='0.0.0.0') 
