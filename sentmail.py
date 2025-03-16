import subprocess
import sys
import time
import tkinter as tk
import threading
import pandas as pd

# Flag to track whether save.py has been executed
save_process_executed = False


def save_terminal_output(command, output_file):
    try:
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        stdout, stderr = process.communicate()

        with open(output_file, 'w') as file:
            file.write(stdout)

    except FileNotFoundError:
        print("File not found or command not executable.")
    except Exception as e:
        print(f"An error occurred: {e}")


def close_output_window(output_window, previous_window, root):
    global save_process_executed
    output_window.destroy()
    previous_window.destroy()
    root.quit()  # End the program and close the main window


def process_email_addresses(output_filename, excel_filename):
    df = pd.read_excel(excel_filename)
    email_addresses = df['Email Address'].tolist()

    modified_emails = ["Email sent to " + email for email in email_addresses]

    with open(output_filename, 'w') as file:
        file.write('\n'.join(modified_emails))


def run_command_and_display_output(root, output_window, previous_window):
    print("[IDENTIFIER] mail3.py")
    sys.stdout.flush()
    time.sleep(1)
    display_command = ["python", "mail3.py"]
    output_filename = 'outputmail.txt'
    excel_filename = 'user_data.xlsx'

    save_terminal_output(display_command, output_filename)
    process_email_addresses(output_filename, excel_filename)

    output_window = tk.Toplevel(root)
    output_window.title("Output")
    output_text = tk.Text(output_window, height=20, width=80)
    output_text.pack()

    with open(output_filename, 'r') as file:
        modified_output = file.read()

    output_text.insert(tk.END, modified_output)

    save_close_button = tk.Button(output_window, text="Close",
                                  command=lambda: close_output_window(output_window, previous_window, root))
    save_close_button.pack()


def run_parallel_process():
    print("[IDENTIFIER] loadingauto.py")
    sys.stdout.flush()
    time.sleep(1)
    parallel_command = ["python", "loadingauto.py"]
    subprocess.Popen(parallel_command)


def run_save_process():
    print("[IDENTIFIER] save.py")
    sys.stdout.flush()
    time.sleep(1)
    save_command = ["python", "save.py"]
    subprocess.run(save_command)
    print("*Exit application to End Program*")



root = tk.Tk()
root.withdraw()

output_window = None  # Initialize output_window
previous_window = tk.Toplevel(root)
previous_window.withdraw()  # Hide initially, will be shown when AI Response is displayed

parallel_thread = threading.Thread(target=run_parallel_process)
parallel_thread.start()

root.after(100, lambda: run_command_and_display_output(root, output_window, previous_window))
root.after(200, run_save_process)  # Schedule the save process after a certain delay


root.mainloop()
