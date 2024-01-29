# Learn to Debate chat tool 2023 ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white)

## Author: VS
### MSc Information Technology Project 
### Birkbeck College, University of London

<img width="436" alt="COVER" src="https://github.com/wikuskina/pythonProject7/assets/50303995/35bc507a-a837-4222-a4d2-47b3da92c961">

#### Description of the APP
The application is a chat that provides a space for users to talk to each other. It was created with the purpose of being used while learning debating skills and critical thinking. It can be used for other educational purposes, where it is beneficial to have a conversation in writing. 

#### CHAT features
- The chat lets users talk to each other.
- It saves communication in a newly created text file.
- Text file is saved in the same location the script is running from.
- User can add feedback at the end, which is also written into the text file.
- Chat conversations are tested against the list of "words.txt" and prompts messages if words are matching.
- "Words.txt" contain words that bring negative tone to the conversation, including swear words. 

#### VERSIONS of the program
Program has two versions: Local and Internet, and both can be run either via Python scripts or via executable files (.exe extention). Exe files used to be located in the 
Executable files subfolder, they were however removed as are no longer applicable.

**Difference between local and Internet** connection programs:
- Local version should successfully run between devices on the same network. The local version asks user to input the IP address of the device on which the server is running.
- A separate program (supplied) can be run to find out the IP address.
- Internet version is designed to connect to the server running on author's device.
 
#### PREPARE BEFORE running the program
**To run Python scripts:**
- Install Python.
- Instal libraries via Windows command prompt: pip install customtkinter  --- Customtkinter, pip install pillow   --- Pillow
- All other libraries should be built-in.

#### HOW TO run the program - LOCAL connection
Python script can be run directly by clicking on it, via command line or Python IDE, such as PyCharms.
- Chat-Server.py is run first.
- Get-your-host.py is run second (to find out the local IP) on the same machine as server.
- Chat-Client-Local.py is run third - can be run on the same or different machine as the server. Will need the IP address from the Get-your-host.py

#### HOW TO run the program - INTERNET connection
Python script can be run directly by clicking on it, via command line or Python IDE, such as PyCharms.
- Chat-Server.py is run first, if testing done with the server running on device other than author's. Otherwise, it can be attempted to run the Client script and hopefully it will connect to the server already running on author's device. Same applies for the .exe files.
- Chat-Client-Internet.py is run next.

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

#### NO files should be removed and they should be kept together, as this may affect performance of the program.
