import speech_recognition as sr

def convert_speech_to_text(audio_file):
    # Initialize recognizer
    recognizer = sr.Recognizer()

    # Load audio file
    with sr.AudioFile(audio_file) as source:
        # Record the audio
        audio_data = recognizer.record(source)

        # Convert audio to text
        try:
            text = recognizer.recognize_google(audio_data)
            return text
        except sr.UnknownValueError:
            print("Speech Recognition could not understand the audio")
        except sr.RequestError as e:
            print("Could not request results from Speech Recognition service; {0}".format(e))

# Example usage
audio_file = "your_audio_file.wav"  # Replace with the path to your audio file
text = convert_speech_to_text(audio_file)
if text:
    print("Text from audio:", text)
