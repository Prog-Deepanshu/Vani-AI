import logging
from flask import Flask, request, render_template, url_for
import gtts
import os
import time

app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)


@app.route('/')
def index():
    return render_template('index.html')

def text_to_speech(text):
    try:
        timestamp = int(time.time())
        output_filename = f'static/output_{timestamp}.mp3'
        tts = gtts.gTTS(text=text, lang='en')
        tts.save(output_filename)
        return output_filename
    except Exception as e:
        app.logger.error(f'Error in text_to_speech: {e}')
        raise

@app.route('/convert', methods=['POST'])
def convert():
    try:
        text = request.form['text']
        audio_file = text_to_speech(text)
        return url_for('static', filename=audio_file)
    except Exception as e:
        app.logger.error(f'Error in convert route: {e}')
        return 'Error processing request', 500

if __name__ == '__main__':
    app.run(debug=True)
