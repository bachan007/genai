import pyttsx3

def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()

    # Set properties (optional)
    engine.setProperty('rate', 150)  # Speed of speech
    engine.setProperty('volume', 1)  # Volume level (0.0 to 1.0)

    # Convert the given text to speech
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()

# if __name__ == "__main__":
#     # Replace the text with your desired message
#     text_to_speech(speech_to_text())
