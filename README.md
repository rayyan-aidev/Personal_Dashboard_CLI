# 🧑‍💻 Personal Dashboard CLI

A modular, beginner-friendly **Command-Line Interface (CLI) Dashboard** that helps users manage their daily tasks, goals, notes, and more — all in one place! Secure login, streak tracking, and multiple productivity tools are included.

---

## 🚀 Features

- 🔐 **Secure Login System**  
  - Hashed passwords using `hashlib`  
  - One-time password display only (no plain text storage)  
  - Forgot password support  
  - Random or custom username/password options

- 📅 **Streak Tracker**  
  - Motivates daily usage  
  - Tracks login streaks with reset mechanism

- 📝 **Notes App**  
  - Create, view, and manage notes

- ✅ **To-do App**  
  - Track tasks and mark them complete

- 🎯 **Goal Tracker**  
  - Set and track your short- or long-term goals

- 🕒 **Clock and Timer Utility**  
  - Timer and clock functions for focus or timing activities

- 🧮 **Simple Calculator**  
  - Perform basic arithmetic operations

- 👤 **User Profile Manager**  
  - View and update basic user profile information

---

## 🗂️ Project Structure
Personal_Dashboard_CLI/
│
├── main.py # Main CLI entry point
├── login_system.py # Secure login and user management
├── user_profile.json # Stores login streak and user info
├── login_details.json # Stores hashed login credentials
├── notes_app.py # Notes manager module
├── todo_app.py # To-do list module
├── goal_tracker.py # Goal setting and tracking module
├── timer.py # Clock and timer features
├── Simple_Calculator_upd.py # Calculator functions
├── User_Profile.py # User profile display/editing
└── README.md # Project documentation

---

## 🛠️ Technologies Used

- **Python 3.13.5**
- Built-in modules:
  - `json`, `os`, `hashlib`, `datetime`, `time`, `random`
- File-based data persistence (no external database)

---

## 🧑‍🏫 How It Works

1. **Run** `main.py`  
2. **Login or Sign Up** using `login_system`  
3. The app checks your login streak and welcomes you  
4. Choose a feature from the menu:
    - Clock & Timer
    - Notes
    - Calculator
    - To-do App
    - Goal Tracker
    - User Profile

---

## 🧪 Security Features

- **Hashed passwords only** (SHA-256 using `hashlib`)
- **One-time password visibility**
- No storage of plain passwords
- Secure JSON-based login system
- Password reset via identity verification

---

## 📌 Requirements

- Python 3.7 or above
- No external libraries required

---

## 🧰 Setup Instructions

```bash
git clone https://github.com/rayyan-aidev/personal-dashboard-cli.git
cd personal-dashboard-cli
python main.py

---

## 📄 License
This project is licensed under the MIT License. See LICENSE for details.

---

## 🙌 Credits
Developed by Rayyan Aqeel

---

## 🌟 Show Your Support
If you like this project:
-⭐ Star the repo
-🐛 Report bugs
-✅ Suggest features
-🔗 Share it!

