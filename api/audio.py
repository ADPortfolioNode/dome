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