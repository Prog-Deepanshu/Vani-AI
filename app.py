from flask import Flask, request, render_template
import gtts


app = Flask(__name__)

def text_to_speech(text):
    tts = gtts.gTTS(text=text, lang='en')  # Change 'en' to desired language
    tts.save("output.mp3")
   

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    text_to_speech(text)
    return "Text converted to speech"

if __name__ == '__main__':
    app.run(debug=True)
