from flask import Flask, request, render_template, send_from_directory, url_for
import gtts
import os
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def text_to_speech(text):
    timestamp = int(time.time())
    output_filename = f'output_{timestamp}.mp3'
    output_path = os.path.join('static', output_filename)
    tts = gtts.gTTS(text=text, lang='en')
    tts.save(output_path)
    return output_filename

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    audio_file = text_to_speech(text)
    return url_for('static', filename=audio_file)

if __name__ == '__main__':
    app.run(debug=True)
