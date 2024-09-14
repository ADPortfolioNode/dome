import os
from flask import Flask, Request, jsonify
from flask_cors import CORS
from pathlib import Path
import openai

# Initialize the OpenAI client with your API key from environment variables
openai.api_key = os.getenv('DomeGPT4oMini')

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    welcome = 'Welcome to the AI Chat API. Use POST <a href="/api/chat">This link</a> to interact.'
    return welcome

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    messages = data.get('messages', [])

    try:
        # Create a completion using the OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-4",
            messages=messages
        )
        response_text = completion.choices[0].message['content']
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
    return jsonify({'response': response_text})

@app.route('/api/speech', methods=['POST'])
def speech():
    data = Request.get_json()
    speech_file_path = Path(__file__).parent / "speech.opus"

    try:
        response = openai.Audio.create(
            model="tts-1",
            voice="alloy",
            input=data,
            output='Opus'
        )
        response.stream_to_file(speech_file_path)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

    return jsonify({'message': f'Speech saved to {speech_file_path}'})

@app.route('/api/chat', methods=['GET'])
def chat_instructions():
    message = 'Use POST to /api/chat with JSON body containing messages.'
    return jsonify({'message': message})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
