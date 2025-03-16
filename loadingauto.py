import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QProgressBar
from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtGui import QFont  # Add this import for QFont

import time

def start_loading():
    progress_bar.setValue(0)
    progress_bar.setMinimum(0)
    progress_bar.setMaximum(100)
    progress_bar.setFormat("Loading...")

    for i in range(101):
        time.sleep(0.01)
        progress_bar.setValue(i)
        app.processEvents()  # Process events to update the window

    progress_bar.setFormat("Loading Complete!")

    QTimer.singleShot(2000, root.close)

app = QApplication(sys.argv)
root = QMainWindow()
root.setWindowTitle("PyQt Loading Animation")

loading_label = QLabel(root)
loading_label.setFont(QFont("Arial", 12))  # Set font using QFont object
loading_label.setText("")
loading_label.setAlignment(Qt.AlignCenter)
loading_label.setGeometry(50, 50, 300, 50)
root.setCentralWidget(loading_label)

progress_bar = QProgressBar(root)
progress_bar.setOrientation(Qt.Horizontal)
progress_bar.setGeometry(50, 100, 300, 20)
root.setCentralWidget(progress_bar)

root.show()

QTimer.singleShot(100, start_loading)

sys.exit(app.exec_())
