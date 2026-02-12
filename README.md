# Meeting Action Items Tracker

## Overview
This is a Flask-based web application that allows users to:
- Paste a meeting transcript
- Automatically extract action items
- Edit, add, delete, and complete tasks
- View last 5 processed transcripts
- Filter tasks (All / Open / Completed)
- Check backend and database health via /status endpoint

---

## Features

- Transcript processing
- Automatic task extraction (basic rule-based)
- Task management (Add / Complete / Delete)
- Filter tasks by status
- Last 5 transcript history
- Status page: /status

---

## Tech Stack

- Python
- Flask
- SQLite
- HTML

---

## How to Run

1. Clone the repository
2. Create virtual environment:
   python -m venv venv

3. Activate virtual environment:
   venv\Scripts\activate

4. Install dependencies:
   pip install -r requirements.txt

5. Run the app:
   python app.py

6. Open in browser:
   http://127.0.0.1:5000

---

## Status Endpoint

Visit:
http://127.0.0.1:5000/status

This checks:
- Backend health
- Database connection

---

## Notes

- No API keys are stored in the code.
- Uses a local SQLite database.
- Basic rule-based extraction for demo purposes.