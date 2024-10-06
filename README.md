# Learn to Debate chat tool 2023 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)
### Author: Viktorija S

### Abstrat

Current political, economic, and social events, such as Covid-19 pandemic and war in Ukraine, remind us about how polarised the world is becoming. Many heated debates discussing current events are happening online, with people losing the skill (or never learning) how to discuss an issue in a mature and constructive way, so learning debating skills is essential to improve communication standards. 
The aim was to create a Learn To Debate chat tool (a chat tool), with simple functionality and ease of use. The application could potentially be used in educational environments as a helpful learning space for students, while they learn debating and critical thinking skills under supervision of their teachers.<br>

### Summary
<br>

### The code
This repository contains the app code and related files.<br> <br>
<img width="436" alt="COVER" src="https://github.com/wikuskina/pythonProject7/assets/50303995/35bc507a-a837-4222-a4d2-47b3da92c961"> <br>

<br>

- Chat is tested against the list of "words.txt" and prompts messages if words are matching.<br>
- "Words.txt" contains words that (for example) bring a negative tone to the conversation, including swear words. It can be amended and used with a different purpose. <br>
- The chat saves communication in a newly created text file.<br>
- The text file is saved in the same location the script is running from.<br>
- User can add feedback at the end, which is also written into the text file.<br><br>

Chat example <br><br>
<img width="384" alt="Picture1" src="https://github.com/wikuskina/Chat-App-Final-Project/assets/50303995/b7080faf-df66-426b-9380-13326248ce73">
<br> <br>
<img width="375" alt="Picture2" src="https://github.com/wikuskina/Chat-App-Final-Project/assets/50303995/5703f1b1-ac7f-4597-b71d-3db2dfcfd42d">
 <br> <br>
Text file of a saved chat <br> <br>
![Picture4](https://github.com/wikuskina/Chat-App-Final-Project/assets/50303995/a14fe42a-9386-4a9b-bc15-fd24fae285d4)  <br>

Program has two versions: Local and Internet.<br>
- Local version runs between devices on the same network. It asks user to input the IP address of the device on which the server is running.  <br>
- A separate script _Get Your Host_ can be run to find out the IP address. <br>
- Internet version is designed to connect to the server running on author's device (when running). <br>
 
#### HOW TO run the program 
- Chat-Server.py is run first.
- Chat-Client-Local.py is run second - can be run on the same or different machine as the server. Will need the IP address from the Get-your-host.py, if running the local version.

#### ALL files that are part of the project
- Chat-Server.py
- Get-your-host.py
- Chat-Client-Local.py
- Chat-Client-Internet.py
- Words.txt 
- deb.png
- debatetoolIcon.jpg
- Chat script.txt
- README.md

_NO files should be removed and should be kept in one location, as this may affect performance of the program._
