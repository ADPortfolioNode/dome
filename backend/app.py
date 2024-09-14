# File location: app.py

from flask import Flask, request, jsonify
from flask_cors import CORS
from openai import OpenAI
import os
import json
import numpy as np
from dotenv import load_dotenv
import faiss
from typing import List, Dict
from fetchdee import FetchDee 

load_dotenv()

IMAGES_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'images')

app = Flask(__name__, static_folder=IMAGES_DIRECTORY, static_url_path='/images')
CORS(app)

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

@app.route('/api/models/retrieve', methods=['GET'])
def retrieve_model():
    model = request.args.get('model')
    if not model:
        return jsonify({"error": "Model parameter is required"}), 400
    with app.app_context():
        return jsonify(client.models.retrieve(model))

@app.route('/api/completions', methods=['POST'])
def create_completion():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.completions.create(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/chat/completions', methods=['POST'])
def create_chat_completion():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.chat.completions.create(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/edits', methods=['POST'])
def create_edit():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.edits.create(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/images/generations', methods=['POST'])
def create_image():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.images.generate(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/images/edits', methods=['POST'])
def edit_image():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.images.edit(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/images/variations', methods=['POST'])
def create_image_variation():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.images.create_variation(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/embeddings', methods=['POST'])
def create_embedding_route():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.embeddings.create(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/audio/transcriptions', methods=['POST'])
def create_audio_transcription():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        with app.app_context():
            return jsonify(client.audio.transcriptions.create(**data))
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

@app.route('/api/completions/<filename>', methods=['GET'])
def get_completion(filename):
    with app.app_context():
        return jsonify({"url": f"{API_URL}/completions/{filename}"})

@app.route('/api/edits/<filename>', methods=['GET'])
def get_edit(filename):
    with app.app_context():
        return jsonify({"url": f"{API_URL}/edits/{filename}"})

@app.route('/api/audio/transcriptions/<filename>', methods=['GET'])
def get_transcription(filename):
    with app.app_context():
        return jsonify({"url": f"{API_URL}/audio/transcriptions/{filename}"})

@app.route('/api/audio/translations/<filename>', methods=['GET'])
def get_translation(filename):
    with app.app_context():
        return jsonify({"url": f"{API_URL}/audio/translations/{filename}"})

@app.route('/api/fine-tunes/<filename>', methods=['GET'])
def get_fine_tune(filename):
    with app.app_context():
        return jsonify({"url": f"{API_URL}/fine-tunes/{filename}"})

@app.route('/api/concierge', methods=['POST'])
def chat_with_concierge():
    if not request.data:
        return jsonify({"error": "Empty request body"}), 400

    try:
        data = request.get_json()
        if data is None:
            raise json.JSONDecodeError("Expecting value", "", 0)
        message = data.get('message')
        if not message:
            return jsonify({"error": "Message is required"}), 400
        print('Sending message:', message)
        
        
        
        
        response = {"reply":message}
        return jsonify(response)
    except json.JSONDecodeError as e:
        error_message = f"Error decoding JSON from request: {str(e)}"
        print(error_message)
        print(f"Raw request data: {request.data}")
        return jsonify({"error": error_message}), 400
    except Exception as e:
        error_message = f"Unexpected error: {str(e)}"
        print(error_message)
        return jsonify({"error": error_message}), 500

if __name__ == '__main__':
    app.run(debug=True)