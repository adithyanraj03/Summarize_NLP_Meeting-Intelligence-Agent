import sys,time
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt  # Add this line to import Qt module
import subprocess

class DisplayLabel(QLabel):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setTextInteractionFlags(self.textInteractionFlags() | Qt.TextSelectableByMouse)  # Use Qt module

def enter_mails(window):
    window.close()  # Close the window when 'Enter Mails' button is clicked
    subprocess.run(["python", "mail_entry.py"])

def run_command_and_display_output():
    print("[IDENTIFIER] mail_entry.py")
    sys.stdout.flush()
    time.sleep(1)
    display_text = "Audio Summary Created Successfully.\n\nAudio Meeting Minutes Created Successfully."

    try:
        app = QApplication(sys.argv)
        window = QMainWindow()
        window.setWindowTitle("AI Response")
        window.setGeometry(100, 100, 970, 571)

        label = DisplayLabel(window)
        label.setGeometry(30, 10, 900, 300)
        font = QFont("Courier New", 13)
        label.setFont(font)
        label.setText(display_text)

        button = QPushButton("Enter Mails", window)
        button.resize(180, 50)
        button_font = QFont("Arial", 16)
        button.setFont(button_font)
        button.move(window.width() // 2 - button.width() // 2, 400)
        button.clicked.connect(lambda: enter_mails(window))

        window.show()
        sys.exit(app.exec_())

    except subprocess.CalledProcessError:
        print("Error executing the command.")

if __name__ == "__main__":
    run_command_and_display_output()
