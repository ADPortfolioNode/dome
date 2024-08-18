from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
import os
import speech from speech.speech

app = Flask(__name__)
CORS(app) 
# Initialize the OpenAI client with your API key
openai.api_key = '<DomeGPT4oMini>' 

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
    
@app.route('/api/speech', methods=['POST'])  # Only accept POST requests
def speech():
    if not request.is_json:  # Check if the request is JSON
        return jsonify({'error': 'Content-Type must be application/json'}), 415

    data = request.json
    messages = data.get('message', [])
    
    if not messages:  # Check if messages are provided
        return jsonify({'error': 'No messages provided'}), 400

    try:
        # Create a completion using the OpenAI API
       
        response = client.audio.speech.create(
        model="tts-1",
        voice="alloy",
        input="Hello world! This is a streaming test.",
    ) 
    return response.stream_to_file(speech_file_path)
        
@app.route('/api/chat', methods=['GET'])  # Provide instructions for GET
def chat_instructions():
    return jsonify({'message': '<h2>Use POST to /api/chat with JSON body containing messages.</h2>'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
