import pyttsx3 
from pydub import AudioSegment 
 
def text_to_mp3(text, output_mp3_path): 
    engine = pyttsx3.init() 
    wav_path = "output.wav" 
    engine.save_to_file(text, wav_path) 
    engine.runAndWait() 
 
    audio = AudioSegment.from_wav(wav_path) 
    audio.export(output_mp3_path, format="mp3") 
 
if __name__ == "__main__": 
    text = "Hello, this is a test of the text to speech conversion." 
    output_mp3_file = "output.mp3" 
    text_to_mp3(text, output_mp3_file) 
    print(f"Converted text to speech and saved to {output_mp3_file}.") 
