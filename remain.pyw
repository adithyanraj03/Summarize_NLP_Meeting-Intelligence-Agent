import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QTextEdit, QDesktopWidget
from PyQt5.QtCore import QProcess, QTextCodec
from PyQt5.QtGui import QColor, QTextCharFormat, QFont


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Process Monitor")
        self.setGeometry(0, 0, 640, 400)  # Initial geometry without a position

        screen = QDesktopWidget().screenGeometry()
        window_size = self.geometry()
        self.move((screen.width() - window_size.width()) // 2, (screen.height() - window_size.height()) // 2)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.start_button = QPushButton("Start Application", self)
        self.start_button.clicked.connect(self.start_subprocess)
        self.layout.addWidget(self.start_button)

        self.subprocess = QProcess()
        self.subprocess.setProcessChannelMode(QProcess.MergedChannels)
        self.subprocess.setReadChannel(QProcess.StandardOutput)

        self.output_widget = QTextEdit(self)
        self.layout.addWidget(self.output_widget)

        self.subprocesses = {
            "remail_entry.py": "Loading ...",
            "remail.py": "Senting Mails ...",
        }

        self.current_subprocess = None

    def start_subprocess(self):
        self.start_button.hide()  # Hide the button after clicking it
        command = ["python", "remail_entry.py"]
        self.subprocess.start(" ".join(command))
        self.subprocess.readyReadStandardOutput.connect(self.handle_output)
        self.subprocess.finished.connect(self.handle_finish)

    def handle_output(self):
        codec = QTextCodec.codecForName("UTF-8")
        data = codec.toUnicode(self.subprocess.readAll())
        lines = data.split("\n")

        for line in lines:
            if "[IDENTIFIER]" in line:
                self.current_subprocess = line.split("[IDENTIFIER] ")[1].strip()
            else:
                subprocess_name = self.subprocesses.get(self.current_subprocess)
                if subprocess_name:
                    output_text = f"[{subprocess_name} ]: {line}"
                    if "Loading ..." in output_text:
                        dark_green = QColor(50, 200, 50)  # RGB values for green
                        self.print_output(output_text, color=dark_green, bold=True)
                    else:
                        dark_red = QColor(255, 0, 0)  # RGB values for dark red
                        self.print_output(output_text, color=dark_red, bold=True)

    def handle_finish(self):
        print("Subprocess finished.")

    def print_output(self, text, color=None, bold=False):
        cursor = self.output_widget.textCursor()
        cursor.movePosition(cursor.End)

        # Set text format
        formats = QTextCharFormat()
        if color:
            formats.setForeground(color)
        if bold:
            formats.setFontWeight(QFont.Bold)

        cursor.insertText(text + '\n', formats)  # Apply format directly to the inserted text
        cursor.movePosition(cursor.End)  # Move cursor to the end after inserting text
        self.output_widget.setTextCursor(cursor)

    def closeEvent(self, event):
        if self.subprocess.state() == QProcess.Running:
            self.subprocess.terminate()
            self.subprocess.waitForFinished()
        event.accept()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
