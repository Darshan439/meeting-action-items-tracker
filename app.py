from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# Create database and table
def init_db():
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    # Transcripts table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS transcripts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    # Tasks table linked to transcript
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            transcript_id INTEGER,
            title TEXT NOT NULL,
            assignee TEXT,
            due_date TEXT,
            status TEXT DEFAULT 'Pending',
            FOREIGN KEY (transcript_id) REFERENCES transcripts(id)
        )
    """)

    conn.commit()
    conn.close()

init_db()

@app.route("/")
def index():
    status_filter = request.args.get("status")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    if status_filter:
        cursor.execute(
            "SELECT id, title, assignee, due_date, status FROM tasks WHERE status=?",
            (status_filter,)
        )
    else:
        cursor.execute(
            "SELECT id, title, assignee, due_date, status FROM tasks"
        )

    tasks = cursor.fetchall()
    conn.close()

    return render_template("index.html", tasks=tasks)

@app.route("/process_transcript", methods=["POST"])
def process_transcript():
    transcript = request.form["transcript"]

    if not transcript.strip():
        return redirect("/")

    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO transcripts (content) VALUES (?)",
        (transcript,)
    )
    transcript_id = cursor.lastrowid

    lines = transcript.split("\n")

    for line in lines:
        if "will" in line.lower():
            title = line.strip()
            assignee = "Unknown"
            due_date = "Not specified"

            cursor.execute(
                """
                INSERT INTO tasks (transcript_id, title, assignee, due_date)
                VALUES (?, ?, ?, ?)
                """,
                (transcript_id, title, assignee, due_date)
            )

    conn.commit()
    conn.close()

    return redirect("/")

@app.route("/complete/<int:id>")
def complete_task(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("UPDATE tasks SET status='Completed' WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")

@app.route("/delete/<int:id>")
def delete_task(id):
    conn = sqlite3.connect("database.db")
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tasks WHERE id=?", (id,))
    conn.commit()
    conn.close()
    return redirect("/")
@app.route("/status")
def status():
    db_status = "OK"
    try:
        conn = sqlite3.connect("database.db")
        conn.close()
    except:
        db_status = "Error"

    return {
        "backend": "OK",
        "database": db_status,
        "llm": "Not Connected (basic rule-based version)"
    }

if __name__ == "__main__":
    app.run(debug=True)
