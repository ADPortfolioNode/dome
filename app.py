from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os

app = Flask(__name__)
CORS(app) 
# Initialize the OpenAI client with your API key
openai.api_key = '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' 

@app.route('/', methods=['GET'])
def index():
    welcome = 'Welcome to the AI Chat API. Use POST <a href="http://localhost:8000/api/chat">This link</a> to interact.'
    return welcome

@app.route('/api/chat', methods=['POST'])  # Only accept POST requests
def chat():
    if not request.is_json:  # Check if the request is JSON
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    data = request.json
    messages = data.get('messages', [])
    
    if not messages:  # Check if messages are provided
        return jsonify({'error': 'No messages provided'}), 400

    try:
        # Create a completion using the OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",  # Make sure this model is available
            messages=messages
        )

        # Return the response
        return jsonify({
            'response': completion.choices[0].message['content']
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/chat', methods=['GET'])  # Provide instructions for GET
def chat_instructions():
    return jsonify({'message': 'Use POST to /api/chat with JSON body containing messages.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)