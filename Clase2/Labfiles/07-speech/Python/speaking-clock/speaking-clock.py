from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound

def main():
    try:
        global speech_config

        # Get Configuration Settings
        load_dotenv()
        ai_key = os.getenv('SPEECH_KEY')
        ai_region = os.getenv('SPEECH_REGION')

        # Configure speech service
        # Configure speech service
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)
        print('Ready to use speech service in:', speech_config.region)

        # Get spoken input
        command = TranscribeCommand()
        if command.lower() == 'what time is it?':
            TellTime()

    except Exception as ex:
        print(ex)

def TranscribeCommand():
    command = ''

    # Configure speech recognition
    # Configure speech recognition
# Configure speech recognition
    # Configure speech recognition
    audio_config = speech_sdk.AudioConfig(use_default_microphone=True)
    speech_recognizer = speech_sdk.SpeechRecognizer(speech_config, audio_config)
    print('Speak now...')


    # Process speech input
    # Process speech input
    speech = speech_recognizer.recognize_once_async().get()
    if speech.reason == speech_sdk.ResultReason.RecognizedSpeech:
        command = speech.text
        print(command)
    else:
        print(speech.reason)
    if speech.reason == speech_sdk.ResultReason.Canceled:
        cancellation = speech.cancellation_details
        print(cancellation.reason)
        print(cancellation.error_details)

    # Return the command
    return command


def TellTime():
    now = datetime.now()
    response_text = 'Bienvenido chicos al curso de IA GENERATIVA, la respuesta de La hora es {}:{:02d}'.format(now.hour,now.minute)


    # Configure speech synthesis
    # Configure speech synthesis
    speech_config.speech_synthesis_voice_name = "es-VE-PaolaNeural"
    speech_synthesizer = speech_sdk.SpeechSynthesizer(speech_config)

    # Synthesize spoken output
# Synthesize spoken output
    speak = speech_synthesizer.speak_text_async(response_text).get()
    if speak.reason != speech_sdk.ResultReason.SynthesizingAudioCompleted:
        print(speak.reason)

    # Print the response
    print(response_text)


if __name__ == "__main__":
    main()