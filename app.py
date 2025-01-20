
from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
import os
import openai

# Load environment variables from .env
load_dotenv()

# Initialize Flask app
app = Flask(__name__)

# Use the API key from the .env file
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate_image():
    # Get user input from the frontend
    user_input = request.form['description']

    try:
        # Generate the image using OpenAI's API
        response = openai.Image.create(
            prompt=user_input,
            n=1,
            size="512x512"
        )
        image_url = response['data'][0]['url']
        return jsonify({'status': 'success', 'image_url': image_url})
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)})

if __name__ == "__main__":
    app.run(debug=True)
