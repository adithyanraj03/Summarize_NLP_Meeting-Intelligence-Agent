import soundcard as sc
import soundfile as sf
import tkinter as tk
import time,sys
import threading
import subprocess

OUTPUT_FILE_NAME_1 = "out.wav"
OUTPUT_FILE_NAME_2 = "out2.wav"
SAMPLE_RATE = 48000

# Create global variables to control recording state for both recordings
recording_1 = False
recording_2 = False
recorded_data_1 = []
recorded_data_2 = []
recording_thread_1 = None
recording_thread_2 = None

# Function to start or stop recording for both recordings
def toggle_recording():
    global recording_1, recording_2, recorded_data_1, recorded_data_2, recording_thread_1, recording_thread_2

    if not recording_1 or not recording_2:
        recorded_data_1.clear()
        recorded_data_2.clear()

        def record_audio_1():
            with sc.get_microphone(id=str(sc.default_speaker().name), include_loopback=True).recorder(samplerate=SAMPLE_RATE) as mic_1:
                while recording_1:
                    data_1 = mic_1.record(numframes=SAMPLE_RATE)
                    recorded_data_1.extend(data_1[:, 0])

        def record_audio_2():
            with sc.default_microphone().recorder(samplerate=SAMPLE_RATE) as mic_2:
                while recording_2:
                    data_2 = mic_2.record(numframes=SAMPLE_RATE)
                    recorded_data_2.extend(data_2[:, 0])

        recording_thread_1 = threading.Thread(target=record_audio_1)
        recording_thread_2 = threading.Thread(target=record_audio_2)

        recording_thread_1.start()
        recording_thread_2.start()

        recording_1 = True
        recording_2 = True

        start_stop_button.config(text="Stop Recording")

    else:
        recording_1 = False
        recording_2 = False

        start_stop_button.config(text="Start Recording")

        if recording_thread_1 and recording_thread_2:
            recording_thread_1.join()
            recording_thread_2.join()

# Function to save recorded data for both recordings and run a subprocess
def save_recorded_data():
    global recording_1, recording_2, recorded_data_1, recorded_data_2

    recording_1 = False
    recording_2 = False

    start_stop_button.config(text="Start Recording")

    if recorded_data_1:
        sf.write(file=OUTPUT_FILE_NAME_1, data=recorded_data_1, samplerate=SAMPLE_RATE)
        recorded_data_1.clear()

    if recorded_data_2:
        sf.write(file=OUTPUT_FILE_NAME_2, data=recorded_data_2, samplerate=SAMPLE_RATE)
        recorded_data_2.clear()

    root.quit()

def on_closing():
    if recording_1 or recording_2:
        toggle_recording()
    save_recorded_data()

# Create a GUI window
root = tk.Tk()
root.title("Audio Recorder")

root.protocol("WM_DELETE_WINDOW", on_closing)

# "Start/Stop" button
start_stop_button = tk.Button(root, text="Start Recording", command=toggle_recording)
start_stop_button.pack()

save_button = tk.Button(root, text="Save Recording and Continue", command=save_recorded_data)
save_button.pack()

root.mainloop()
print("[IDENTIFIER] combineaudio.py")
sys.stdout.flush()
time.sleep(1)
subprocess.run(["python", "combineaudio.py"])