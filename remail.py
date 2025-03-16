import sys
import pandas as pd
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QPushButton, QVBoxLayout, QFileDialog, QHBoxLayout, QTextEdit
)
from datetime import datetime
import time

class EmailStatusWindow(QWidget):
    def __init__(self, status_text):
        super().__init__()

        self.setWindowTitle("Email Status")
        self.setGeometry(100, 100, 600, 400)

        layout = QVBoxLayout()

        status_label = QLabel(status_text)
        layout.addWidget(status_label)

        self.setLayout(layout)


class FileSelector(QWidget):
    def __init__(self):
        super().__init__()
        self.summary_file = ""
        self.minutes_file = ""
        self.title_file = ""
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        title_layout = QVBoxLayout()
        title_label = QLabel("Title File:")
        self.title_label = QLabel("No file selected")
        title_button = QPushButton("Select Title File")
        title_button.clicked.connect(self.select_title_file)

        title_layout.addWidget(title_label)
        title_layout.addWidget(self.title_label)
        title_layout.addWidget(title_button)

        summary_layout = QVBoxLayout()
        summary_label = QLabel("Summary File:")
        self.summary_label = QLabel("No file selected")
        summary_button = QPushButton("Select Summary File")
        summary_button.clicked.connect(self.select_summary_file)

        summary_layout.addWidget(summary_label)
        summary_layout.addWidget(self.summary_label)
        summary_layout.addWidget(summary_button)

        minutes_layout = QVBoxLayout()
        minutes_label = QLabel("Minutes File:")
        self.minutes_label = QLabel("No file selected")
        minutes_button = QPushButton("Select Minutes File")
        minutes_button.clicked.connect(self.select_minutes_file)

        minutes_layout.addWidget(minutes_label)
        minutes_layout.addWidget(self.minutes_label)
        minutes_layout.addWidget(minutes_button)

        save_continue_layout = QVBoxLayout()
        save_continue_button = QPushButton("Save and Continue")
        save_continue_button.clicked.connect(self.save_and_continue)

        save_continue_layout.addWidget(save_continue_button)

        layout.addLayout(title_layout)
        layout.addLayout(summary_layout)
        layout.addLayout(minutes_layout)
        layout.addLayout(save_continue_layout)

        self.setLayout(layout)
        self.setWindowTitle("File Selector")

    def select_title_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            self.title_file = file_names[0]
            self.title_label.setText(self.title_file)

    def select_summary_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            self.summary_file = file_names[0]
            self.summary_label.setText(self.summary_file)

    def select_minutes_file(self):
        file_dialog = QFileDialog()
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setNameFilter("Text files (*.txt)")
        if file_dialog.exec_():
            file_names = file_dialog.selectedFiles()
            self.minutes_file = file_names[0]
            self.minutes_label.setText(self.minutes_file)

    def save_and_continue(self):
        if self.title_file and self.summary_file and self.minutes_file:
            send_emails(self.title_file, self.summary_file, self.minutes_file)
            self.close()
        else:
            print("Please select all files.")


def send_emails(title_file, summary_file, minutes_file):
    current_date = datetime.now().strftime('%d-%m-%Y')
    sender_email = "abc@gmail.com"  # Enter your email
    sender_password = "wwwn aqlf gcxn uuuu"  # Enter your app password

    with open(title_file, "r") as email_content_file:
        email_subject = email_content_file.readline().strip()

    excel_file = "re_user_data.xlsx"
    df = pd.read_excel(excel_file)
    email_addresses = df["Email Address"].tolist()
    names = df["Name"].tolist()

    smtp_server = "smtp.gmail.com"
    smtp_port = 587

    for idx, recipient_email in enumerate(email_addresses):
        recipient_name = names[idx]

        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = email_subject

        email_text = f"Hi {recipient_name},\n\n"
        email_text += f"This is an Automated mail regarding the Contents of the Meeting '{email_subject}' you attended.\n"
        email_text += "The autogenerated meeting details and References are as follows:\n\n"

        text_files = [
            {"title": "Meeting Minutes", "path": minutes_file},
            {"title": "Summary", "path": summary_file},
        ]

        for file_data in text_files:
            if file_data["path"]:
                with open(file_data["path"], "r") as file:
                    email_text += f"--- {file_data['title']} ---\n{file.read()}\n\n"

        email_text += "\n" * 2
        email_text += f"Regards, Automated Tool 😀"

        msg.attach(MIMEText(email_text, "plain"))

        try:
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()
            sys.stdout.flush()
            time.sleep(1)
            print(f"Email sent to {recipient_email}")
            sys.stdout.flush()
            time.sleep(1)
        except Exception as e:
            sys.stdout.flush()
            time.sleep(1)
            print(f"Failed to send email to {recipient_email}: {str(e)}")
            sys.stdout.flush()
            time.sleep(1)

    status_text = f"Emails sent to {len(email_addresses)} recipients."
    status_window = EmailStatusWindow(status_text)
    status_window.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    file_selector = FileSelector()
    file_selector.show()
    sys.exit(app.exec_())
