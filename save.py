import os
import shutil
import datetime

def retrieve_and_combine_files(title_dir, summary_dir, minutes_dir, combined_text_dir):
    current_date = datetime.datetime.now().strftime('%d-%m-%Y')
    current_time = datetime.datetime.now().strftime("%H-%M-%S")

    # Define file names
    title_file = f"title_{current_date}.txt"
    summary_file = f"summary_{current_date}.txt"
    minutes_file = f"minutes_{current_date}.txt"
    combined_text_file = "combined_text.txt"

    # Retrieve data from title file
    title_data = ""
    title_path = os.path.join(title_dir, title_file)
    try:
        with open(title_path, 'r') as title_file:
            title_data = title_file.read()
    except FileNotFoundError:
        print(f"File '{title_path}' not found.")

    # Retrieve data from summary file
    summary_path = os.path.join(summary_dir, summary_file)
    try:
        with open(summary_path, 'r') as summary_file:
            summary_data = summary_file.read()
    except FileNotFoundError:
        print(f"File '{summary_path}' not found.")

    # Retrieve data from minutes file
    minutes_path = os.path.join(minutes_dir, minutes_file)
    try:
        with open(minutes_path, 'r') as minutes_file:
            minutes_data = minutes_file.read()
    except FileNotFoundError:
        print(f"File '{minutes_path}' not found.")

    # Rename files with addition to time in name
    os.rename(title_path, os.path.join(title_dir, f"title_{current_date}_{current_time}.txt"))
    os.rename(summary_path, os.path.join(summary_dir, f"summary_{current_date}_{current_time}.txt"))
    os.rename(minutes_path, os.path.join(minutes_dir, f"minutes_{current_date}_{current_time}.txt"))
    print("Data Saved!")
    # Copy and rename combined_text file to data/path directory
    combined_text_path = "combined_text.txt"
    if os.path.exists(combined_text_path):
        copy_path = os.path.join(combined_text_dir, f"combined_text_copy_{current_date}_{current_time}.txt")
        shutil.copyfile(combined_text_path, copy_path)

if __name__ == "__main__":
    title_directory = "data/"
    summary_directory = "data/"
    minutes_directory = "data/"
    combined_text_directory = "data/"

    retrieve_and_combine_files(title_directory, summary_directory, minutes_directory, combined_text_directory)

