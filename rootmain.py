import sys
import subprocess
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
from PyQt5.QtGui import QPixmap, QFont, QIcon
from PyQt5.QtCore import QTimer

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("AI Meeting Recorder")
        self.setGeometry(100, 100, 800, 600)

        # Background image
        self.background_label = QLabel(self)
        self.background_label.setGeometry(0, 0, 800, 600)
        pixmap = QPixmap("images/b3.jpg").scaled(800, 600)
        self.background_label.setPixmap(pixmap)

        # Heading label
        self.heading_label = QLabel("AI MEETING SUMMARIZER", self)
        font = QFont("Arial", 15)
        self.heading_label.setFont(font)
        self.heading_label.setStyleSheet("background-color: white;")
        self.heading_label.setGeometry(200, 100, 400, 50)

        # Start button
        self.start_button = QPushButton(self)
        self.start_button.setGeometry(300, 300, 200, 200)
        pixmap = QPixmap("images/3.png").scaled(200, 200)
        icon = QIcon(pixmap)
        self.start_button.setIcon(icon)
        self.start_button.setIconSize(pixmap.rect().size())
        self.start_button.clicked.connect(self.on_start_click)

        self.alpha = 0.0
        self.direction = 1  # Start with fade-in

        self.fade_timer = QTimer()
        self.fade_timer.timeout.connect(self.fade)
        self.fade_timer.start(100)

    def fade(self):
        # (Rest of the fade method remains the same)
        pass

    def on_start_click(self):
        self.close()
        subprocess.run(["python", "whispher.py"])

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
