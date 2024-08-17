
from openai import OpenAI
import os


app = Flask(__name__)
client = OpenAI(api_key=os.environ.get("GPT4OMINI_API_KEY"))

@app.route('/api/chat', methods=['GET'])
def chat():
    data = request.json
    messages = data.get('messages', [])

    try:
        # Create a completion using the OpenAI API
        completion = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=messages
        )
            
        # the response
        return jsonify({
            'response': completion.choices[0].message['content']
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
