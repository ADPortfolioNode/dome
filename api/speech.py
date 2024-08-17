from pathlib import Path
import openai

speech_file_path = Path(__file__).parent / "speech.mp3"

response.stream_to_file(speech_file_path)

@app.route('/api/speech', methods=['POST'])
def speech():
    MODEL = "gpt-3.5-turbo"
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "Knock knock."},
            {"role": "assistant", "content": "Who's there?"},
            {"role": "user", "content": "Orange."},
    ],
    temperature=0,
),response = openai.audio.speech.create(
  model="tts-1",
  voice="alloy",
  input=""The quick brown fox jumped over the lazy dog.""
)
    return(json.dumps(json.loads(response.model_dump_json()), indent=4))