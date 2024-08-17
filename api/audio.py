
from openai import OpenAI
import os


app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("GPT4OMINI_API_KEY"))

@app.route('/api/audio', methods=['GET'])
def audio():
    data = request.json
    messages = data.get('messages', [])
    
    
    
    from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"
response = openai.with_streaming_response.method(
  model="tts-1",
  voice="alloy",
  input="Hey tami - what you doin over there???."
)
response.stream_to_file(speech_file_path) 

# POST : https://api.openai.com/v1/audio/speech