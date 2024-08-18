from pathlib import Path 
from flask import Flask, CORS
from openai import OpenAI
import os


app = Flask(__name__)
CORS(app)
client = OpenAI(api_key=os.environ.get("GPT4OMINI_API_KEY"))

@app.route('/api/audio', methods=['POST'])
def audio():
    data = response.getjson()
    speech_file_path = Path(__file__).parent / "speech.mp3"
    response = client.audio.speech.create(
      model="tts-1",
      voice="alloy",
      input=data
    )

    response.stream_to_file(speech_file_path)
# POST : https://api.openai.com/v1/audio/speech