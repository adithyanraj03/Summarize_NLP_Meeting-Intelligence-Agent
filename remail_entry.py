import sys
import time
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QTextEdit
)
import pandas as pd
import subprocess
print("[IDENTIFIER] remail_entry.py")
sys.stdout.flush()
time.sleep(1)

class UserDataEntry(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("User Data Entry")
        self.setGeometry(100, 100, 800, 600)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.num_entries_label = QLabel("Enter number of entries:", self)
        self.layout.addWidget(self.num_entries_label)

        self.num_entries_entry = QLineEdit(self)
        self.layout.addWidget(self.num_entries_entry)

        self.collect_button = QPushButton("Collect Entries", self)
        self.collect_button.clicked.connect(self.collect_entries)
        self.layout.addWidget(self.collect_button)

    def save_to_excel(self, entries):
        data = {'Name': [], 'Email Address': []}
        for entry in entries:
            name = entry['Name'].text()
            email = entry['Email Address'].text()
            data['Name'].append(name)
            data['Email Address'].append(email)

        df = pd.DataFrame(data)
        df.to_excel('re_user_data.xlsx', index=False)
        print("Data saved to 're_user_data.xlsx'.")
        self.display_data(df)
        self.close()  # Close the window after saving and displaying data

    def display_data(self, dataframe):
        self.output_window = DisplayWindow(dataframe, self)
        self.output_window.show()

    def collect_entries(self):
        num_entries = int(self.num_entries_entry.text())

        self.num_entries_label.hide()
        self.num_entries_entry.hide()
        self.collect_button.hide()

        entries_layout = QVBoxLayout()
        entries_widget = QWidget()

        entries = []
        for i in range(num_entries):
            entry_layout = QHBoxLayout()

            name_label = QLabel(f"Name {i + 1}:", self)
            entry_layout.addWidget(name_label)

            name_entry = QLineEdit(self)
            entry_layout.addWidget(name_entry)

            email_label = QLabel(f"Email Address {i + 1}:", self)
            entry_layout.addWidget(email_label)

            email_entry = QLineEdit(self)
            entry_layout.addWidget(email_entry)

            entries_layout.addLayout(entry_layout)
            entries.append({'Name': name_entry, 'Email Address': email_entry})

        save_button = QPushButton("Save and Continue", self)
        save_button.clicked.connect(lambda: self.save_to_excel(entries))
        entries_layout.addWidget(save_button)

        self.layout.addWidget(entries_widget)
        entries_widget.setLayout(entries_layout)


class DisplayWindow(QMainWindow):
    def __init__(self, dataframe, parent=None):
        super().__init__()

        self.setWindowTitle("Entries Entered")
        self.setGeometry(100, 100, 800, 600)
        self.parent = parent

        self.output_text = QTextEdit(self)
        self.output_text.setPlainText(dataframe.to_string(index=False))
        self.output_text.setGeometry(0, 0, 800, 500)

        self.setCentralWidget(self.output_text)

        continue_button = QPushButton("Continue", self)
        continue_button.clicked.connect(self.close_windows)
        continue_button.setGeometry(300, 510, 200, 50)

        edit_button = QPushButton("Edit", self)
        edit_button.clicked.connect(self.edit_entries)
        edit_button.setGeometry(100, 510, 200, 50)

    def close_windows(self):
        self.close()  # Close the display window
        self.parent.close()  # Close the main window
        sys.stdout.flush()
        time.sleep(1)
        print("[IDENTIFIER] remail.py")
        sys.stdout.flush()
        time.sleep(1)
        subprocess.run(["python", "remail.py"])  # Run subprocess after window is closed
    def edit_entries(self):
        self.close()
        edit_window = UserDataEntry()
        edit_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = UserDataEntry()
    window.show()
    sys.exit(app.exec_())
