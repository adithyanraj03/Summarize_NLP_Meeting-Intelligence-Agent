# Summarize_NLP: Meeting Intelligence Agent

A powerful AI-driven application that captures, transcribes, summarizes, and distributes meeting content to participants automatically.

![AI Meeting Summarizer](https://github.com/adithyanraj03/Summarize/assets/39313793/065c3eff-e80f-4eea-979a-429dd2cf943d)

## 🚀 Overview

This intelligent application can be integrated with any online browser or application-based meeting to:
- Capture meeting audio
- Convert speech to text using advanced APIs
- Process and analyze the text with OpenAI
- Generate concise meeting summaries and detailed minutes 
- Automatically email the processed content to all participants

The system intelligently fetches participant emails from synced Excel files, Google Spreadsheets, or Google Forms, streamlining the entire workflow.

## 📑 Table of Contents

- [Features](#features)
- [System Architecture](#system-architecture)
- [Installation](#installation)
  - [Automatic Installation](#automatic-installation)
  - [Manual Installation](#manual-installation)
- [Usage Guide](#usage-guide)
  - [Starting the Application](#starting-the-application)
  - [Recording a Meeting](#recording-a-meeting)
  - [Distributing Meeting Content](#distributing-meeting-content)
  - [Resending to Additional Recipients](#resending-to-additional-recipients)
- [Technical Notes](#technical-notes)
- [License](#license)
- [Contributors](#contributors)

## ✨ Features

- **Intuitive GUI Interface**: Easy-to-use controls for recording and managing meetings
- **Speech-to-Text Conversion**: Accurate transcription of meeting audio
- **AI-Powered Summarization**: Intelligent content analysis using OpenAI
- **Automated Email Distribution**: Seamless delivery of meeting content
- **Participant Management**: Multiple methods to collect and manage recipient emails
- **Historical Access**: Ability to resend meeting summaries to new recipients
- **Cross-Platform Support**: Works with various meeting platforms

## 🏗️ System Architecture

![Project Data Flow](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/meeting-minutes-dataflow-enhanced.svg)

The application follows a three-stage pipeline:
1. **Audio Capture & Conversion**: API converts speech to text
2. **Text Processing**: Python with OpenAI transforms text into structured minutes and summaries
3. **Automated Distribution**: Email system delivers processed content to all participants

## 💻 Installation

### Automatic Installation

The easiest way to install is using the setup script:

```bash
python setup.py install
```

### Manual Installation

Alternatively, you can install dependencies manually:

```bash
pip install -r requirements.txt
```

**Important Note**: When using OpenAI functionality, you may see migration messages regarding API versions. You can:
- Run `openai migrate` to automatically upgrade your codebase
- Pin your installation to the old version: `pip install openai==0.28`

A detailed migration guide is available here: https://github.com/openai/openai-python/discussions/742

## 📝 Usage Guide

### Starting the Application

1. Double-click the executable file to launch the Process Manager
2. Click "Start Application" to initialize the system
3. The main interface will appear with the ANJ logo - click on it to proceed

![Process Monitor](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/process_monitor.png)

![AI Meeting Recorder](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/ai_meeting_recorder.png)

### Recording a Meeting

1. When the recording window appears, click "Start Recording" to begin capturing audio
2. Conduct your meeting as normal
3. When the meeting concludes, click "Save Recording and Continue"
4. The system will begin processing the audio automatically

![Recording Controls](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/recording_controls.png)

### Distributing Meeting Content

1. After processing, enter or confirm the meeting title
2. Specify the number of recipients
3. Enter email addresses for all participants
4. Click "Collect Entries" to proceed
5. The system will generate summaries, format emails, and send them automatically

![User Data Entry](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/user_data_entry.png)

![Entries Entered](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/entries_entered.png)

### Resending to Additional Recipients

To send meeting summaries to recipients who weren't included initially:

1. Locate and run the "AI_Re-sent_Mails.exe" utility in the root folder
2. Follow the prompts to select a previous meeting and specify new recipients
3. The system will resend the already-generated content to these new addresses

![Email Confirmation](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/email_confirmation.png)

![Email Sample](https://raw.githubusercontent.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/main/screenshots/email_sample.png)

## 🔧 Technical Notes

The application uses several advanced technologies:
- PyTorch for audio processing
- Language detection for multi-language support
- OpenAI API for intelligent summarization
- SMTP/Email libraries for distribution
- Tkinter for the graphical interface

On first run, the system will download necessary model files, which may take a few moments depending on your connection speed.

## 📄 License

This project is licensed under the GNU General Public License v3.0 (GPL-3). This means:

- The software is free to use and open source
- You can modify and distribute the software
- Commercial use requires licensing from the original authors

For full license details, see the LICENSE file in the repository.

## 👨‍💻 Contributors

- Adithya N Raj
- Giridhar Prakash
- Madhav A Nair
- Madhav Sunil
