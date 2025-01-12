from TTS.api import TTS

def text_to_speech_coqui(text, output_file):
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC")
    tts.tts_to_file(text=text, file_path=output_file)
    print(f"Audio gespeichert: {output_file}")

text_to_speech_coqui("Dies ist ein Beispiel für Coqui TTS.", "output.wav")
