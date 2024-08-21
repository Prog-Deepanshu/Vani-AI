# Vani AI - Text-to-Speech (TTS) Converter

Vani AI is a powerful and easy-to-use text-to-speech (TTS) application that leverages Google Text-to-Speech (gTTS) to convert written text into spoken words. This project is perfect for developers, educators, and anyone interested in exploring speech synthesis technology.

## Features

- Converts text into high-quality speech using Google TTS.
- Supports multiple languages and accents.
- Simple and intuitive interface.
- Lightweight and efficient, ideal for both personal and professional use.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.x installed on your system.
- Required Python libraries installed (detailed in the `requirements.txt` file).

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/vani-ai.git
    ```

2. Navigate to the project directory:

    ```bash
    cd vani-ai
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

### Usage

1. Run the application:

    ```bash
    python vani_ai.py
    ```

2. Enter the text you want to convert to speech.
3. Choose your desired language and accent (optional).
4. Listen to the generated speech or save it as an audio file.

### Example

```python
from gtts import gTTS
import os

text = "Hello, welcome to Vani AI. This is a text-to-speech conversion example."
language = 'en'

speech = gTTS(text=text, lang=language, slow=False)
speech.save("output.mp3")

os.system("start output.mp3")
