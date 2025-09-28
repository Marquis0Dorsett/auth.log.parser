# auth.log.parser
A Python script that parses Linux authentication logs (auth.log.txt) to extract failed and accepted SSH login attempts. It uses regular expressions to identify login events, captures usernames, IP addresses, and timestamps, and organizes failed login attempts by source IP. 
🔐 auth.log.parser
📌 Project Overview
This Python script parses Linux authentication logs (auth.log.txt) to extract and organize SSH login attempts. It identifies both failed and accepted logins, extracts key details like timestamp, username, and IP address, and aggregates failed attempts by source IP. Designed for cybersecurity students and SOC analysts to practice log analysis and incident detection.

🧠 Learning Objectives
Practice regular expression parsing for log analysis

Understand SSH authentication patterns in Linux

Build foundational skills for SOC workflows and threat detection

📂 Files Included
File Name	Description
auth.log.parser.py	Main Python script for parsing and analyzing auth.log
auth.log.txt	Sample log file for testing and demonstration
README.md	Project overview, setup instructions, and usage notes
🚀 How to Run
Make sure auth.log.txt is in the same directory as the script.

Run the script using Python:

bash
python auth.log.parser.py
The output will display failed login attempts grouped by IP address.

🛠️ Requirements
Python 3.x

No external libraries required (uses re, collections, and os)

📎 Notes
If auth.log is missing, the script will prompt you to check the file location.

You can replace the sample log with a real auth.log from a Linux system for deeper analysis.

🧑‍💻 Author
Marquis Dorsett Aspiring SOC Analyst | CompTIA Security+ Certified University of Tennessee, Knoxville Cybersecurity Bootcamp Graduate and Current University of Phoenix AS Student
