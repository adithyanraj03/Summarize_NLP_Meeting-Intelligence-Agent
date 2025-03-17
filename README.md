# Summarize_NLP: Meeting Intelligence Agent

A powerful AI-driven application that captures, transcribes, summarizes, and distributes meeting content to participants automatically.

![image](https://github.com/user-attachments/assets/e2d3c887-874f-4555-8f57-8b8a0ed27db4)

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
![Project Data Flow](https://github.com/user-attachments/assets/1c17f156-e8ff-41ba-9b51-28cb165763fd)

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
![image](https://github.com/user-attachments/assets/c64784c6-f3fe-484b-975e-77cccabcd3ae)

1. Double-click the executable file to launch the Process Manager
2. Click "Start Application" to initialize the system

![Process Monitor](https://github.com/user-attachments/assets/2a1beed0-6f53-49df-9f88-d18504833afe)

3. The main interface will appear with the ANJ logo - click on it to proceed


![AI Meeting Recorder](https://github.com/user-attachments/assets/e2d3c887-874f-4555-8f57-8b8a0ed27db4)

### Recording a Meeting

1. When the recording window appears, click "Start Recording" to begin capturing audio

![Recording Controls](https://github.com/user-attachments/assets/ea83018e-a2e2-460f-a411-44d5a4a9e557)

2. Conduct your meeting as normal

3. When the meeting concludes, click "Save Recording and Continue"

4. The system will begin processing the audio automatically

![image](https://github.com/user-attachments/assets/5bd61882-3694-4c34-ae94-90bb83dfd9f4)



### Distributing Meeting Content

1. After processing, enter or confirm the meeting title
2. Specify the number of recipients
3. Enter email addresses for all participants
4. Click "Collect Entries" to proceed

![image](https://github.com/user-attachments/assets/48d2a1af-39bb-415d-b014-afa22dffa836)
![User Data Entry](https://github.com/user-attachments/assets/e276f1ce-a01a-47e0-bd7c-5123bbda83dd)
![Entries Entered](https://github.com/user-attachments/assets/1921b47c-455d-42c9-9ca3-4e86d242dee3)

5. The system will generate summaries, format emails, and send them automatically

![image](https://github.com/user-attachments/assets/9328e4b3-99ce-4b18-b0f4-ec976d3c6ef4)

![image](https://github.com/user-attachments/assets/14daab82-2506-4d0a-87ba-3c20c9fc555c)


![image](https://github.com/user-attachments/assets/8b2a0821-aa87-48cd-857a-660854d70ce2)

![image](https://github.com/user-attachments/assets/b12ac937-99a1-48e4-9cd9-41b383adfc37)

### Resending to Additional Recipients

To send meeting summaries to recipients who weren't included initially:

1. Locate and run the "AI_Re-sent_Mails.exe" utility in the root folder

![Email Confirmation](https://github.com/user-attachments/assets/0da1ca36-909a-4978-b713-1d41875a983c)

![Email Sample](https://github.com/user-attachments/assets/01974b67-48aa-4437-b8d1-167b7e02ba4d)


3. Follow the prompts to select a previous meeting and specify new recipients
4. The system will resend the already-generated content to these new addresses


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

For full license details, see the [LICENSE](https://github.com/adithyanraj03/Summarize_NLP_Meeting-Intelligence-Agent/blob/main/LICENSE) file 

## 👨‍💻 Contributors

- Adithya N Raj
- Giridhar Prakash
- Madhav A Nair
- Madhav Sunil
