import os
import pyttsx3
from pydub import AudioSegment

def text_to_mp3(text, output_mp3_path):
    engine = pyttsx3.init()
    wav_path = "output.wav"
    engine.save_to_file(text, wav_path)
    engine.runAndWait()

    audio = AudioSegment.from_wav(wav_path)
    audio.export(output_mp3_path, format="mp3")

def read_file_to_string(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()  # Read the entire file content as a string
        return content
    except FileNotFoundError:
        print(f"Error: The file at {file_path} was not found.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

if __name__ == "__main__":

    try:
        os.remove(f'{current_dir}/output.wav')
    except:
        pass

    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = f'{current_dir}/input.txt'  # Replace with your actual file path
    text = read_file_to_string(file_path)
    output_mp3_file = f"{current_dir}/output.mp3"
    text_to_mp3(text, output_mp3_file)
    print(f"Converted text to speech and saved to {output_mp3_file}.")
