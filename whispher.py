import whisper
import subprocess
from pydub import AudioSegment
import concurrent.futures
import time
import sys

# import pip
# pip.main(["install", "ffmpeg"])

def run_parallel_command(command):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(subprocess.run, command)
        result = future.result()


sys.stdout.flush()
time.sleep(1)
parallel_command = ["python", "loadingauto.py"]
print("[IDENTIFIER] loadingauto.py")
sys.stdout.flush()
time.sleep(1)
run_parallel_command(parallel_command)
print("[IDENTIFIER] capture.py")
sys.stdout.flush()
time.sleep(1)
subprocess.run(["python", "capture.py"])

print("[IDENTIFIER] loadingauto.py")
sys.stdout.flush()
time.sleep(1)
parallel_command = ["python", "loadingauto.py"]
run_parallel_command(parallel_command)

model = whisper.load_model("base")
# Load the long audio file
long_audio_file = "combine_out.wav"
print("[IDENTIFIER] whishper.py")
sys.stdout.flush()
time.sleep(1)
# Split the audio file into segments
segment_duration = 30 * 1000  # Length of each segment in milliseconds
audio = AudioSegment.from_mp3(long_audio_file)
audio_segments = [audio[i:i + segment_duration] for i in range(0, len(audio), segment_duration)]

recognized_texts = []


def run_parallel_command(command):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        future = executor.submit(subprocess.run, command)
        result = future.result()


def process_segment(segment):
    segment.export("temp_segment.wav", format="wav")

    audio_segment = whisper.load_audio("temp_segment.wav")
    audio_segment = whisper.pad_or_trim(audio_segment)

    # Make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio_segment).to(model.device)

    # Detect the spoken language
    _, probs = model.detect_language(mel)
    detected_language = max(probs, key=probs.get)
    print(f"Detected language: {detected_language}")
    sys.stdout.flush()
    time.sleep(1)

    # Decode the audio
    options = whisper.DecodingOptions(fp16=False)
    result = whisper.decode(model, mel, options)
    return result.text


# Process each segment
for i, segment in enumerate(audio_segments):
    recognized_text = process_segment(segment)
    recognized_texts.append(recognized_text)

    # Save the recognized text for each segment to a separate file
    with open(f"master_text_segment_{i}.txt", "w", encoding="utf-8") as master_text_file:
        master_text_file.write(recognized_text)

# Combine all recognized texts into a single text file
with open("combined_text.txt", "w", encoding="utf-8") as combined_file:
    combined_file.write("\n".join(recognized_texts))

# subprocess.run(["python", "summarize.py"])
# subprocess.run(["python", "summarize2.py"])
print("[IDENTIFIER] summarizeai.py")
sys.stdout.flush()
time.sleep(1)
subprocess.run(["python", "summarizeai.py"])
print("Summary , Meeting Minutes and Tile Generated ")
print("[IDENTIFIER] load_display_subbpro.py")
sys.stdout.flush()
time.sleep(1)
subprocess.run(["python", "load_display_subbpro.py"])

# subprocess.run(["python", "summarize3.py"])  # using GPT-2 model
