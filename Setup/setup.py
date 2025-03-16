import subprocess
import sys
import time

def run_installation_command(command):
    try:
        process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
        output = ""
        while True:
            line = process.stdout.readline()
            if not line:
                break
            output += line
            sys.stdout.write(line)
            sys.stdout.flush()
        process.wait()
        return process.returncode, output
    except Exception as e:
        return 1, str(e)

def main():
    installation_commands = [
        "pip install pandas",
        "pip install future",
        "pip install sounddevice",
        "pip install PyAudio",
        "pip install pydub",
        "pip install soundcard",
        "pip install soundfile",
        "pip install ffmpeg-python",
        "winget install ffmpeg",
        "pip install openpyxl",
        "winget install --id Git.Git -e --source winget",
        "pip install git+https://github.com/openai/whisper.git",
        "pip install openai==0.28",
        "pip install Pillow~=10.0.0"
        "pip install PyQt5~=5.15.10"
    ]

    # Start loading animation subprocess
    loading_process = subprocess.Popen(["python", "setupload.py"])

    for command in installation_commands:
        print(f"\nRunning command: {command}")

        # Run the installation command
        return_code, output = run_installation_command(command)

        if return_code == 0:
            print(f"Command successful: {command}")
            print(output)
        else:
            print(f"Error running command: {command}")
            print(output)

    # End loading animation subprocess
    loading_process.terminate()
    loading_process.wait()

    print("All commands executed.")

if __name__ == "__main__":
    main()
