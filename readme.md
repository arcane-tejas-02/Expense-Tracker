# 💰 CLI Expense Tracker

> A clean, beginner-friendly command-line expense tracker built in Python to help you easily manage, track, and analyze your daily finances.

![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## 🚀 About the Project

This project was inspired by the [roadmap.sh Expense Tracker Project](https://roadmap.sh/projects/expense-tracker). It is designed to practice core programming concepts like file I/O, error handling, data manipulation, and structured command-line interfaces (CLI). 

All your expense records are stored locally in a `json` file, meaning your financial data persists safely between sessions without needing an external database.

---

## ✨ Key Features

* **➕ Expense Management:** Add, update, and delete expenses effortlessly with built-in unique ID tracking.
* **👀 Comprehensive Views:** View all recorded expenses in a neatly formatted, readable table layout.
* **🏷️ Smart Filtering & Summaries:** Filter expenses by specific categories or generate monthly breakdowns.
* **📊 Category Analytics:** Automatically calculate and sort your total spending per category.
* **🛡️ Robust Validation:** Bulletproof input validation for amounts, dates, and menu selections to prevent crashes.
* **💾 Local Data Persistence:** Automated saving and loading utilizing a local JSON file.

---

## 🛠️ Technologies Used

* **Python 3.10+** (Utilizing modern features like `match/case` statements)
* **JSON Module:** For reading and writing local persistent storage
* **Datetime Module:** For precise date parsing and monthly summaries

---

## 📁 Project Structure

```text
expense-tracker/
│
├── expense_tracker.py   # Main application logic and CLI interface
├── expenses.json        # Local JSON database (auto-generated on first run)
└── README.md            # Project documentation