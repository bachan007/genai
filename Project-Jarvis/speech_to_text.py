import speech_recognition as sr

def speech_to_text():
    # Initialize the recognizer
    recognizer = sr.Recognizer()

    # Use the default microphone as the source
    with sr.Microphone() as source:
        print("Say something...")
        # Adjust for ambient noise
        recognizer.adjust_for_ambient_noise(source)
        # Listen for the audio and convert it to text
        audio = recognizer.listen(source)

    try:
        # Recognize the speech using Google Speech Recognition
        text = recognizer.recognize_google(audio)
        print(f"Text: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "Google Speech Recognition could not understand audio"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return e

