# =====================================
# NOTES APP (FLASK + SQLITE - NO ERRORS)
# =====================================

from flask import Flask, request, redirect
import sqlite3
from datetime import datetime

app = Flask(__name__)

# ---------------- DATABASE SETUP ---------------- #
conn = sqlite3.connect("notes.db", check_same_thread=False)
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS notes (
    note_id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    content TEXT,
    created_at TEXT
)
""")

# Create view (hide content)
cursor.execute("""
CREATE VIEW IF NOT EXISTS notes_view AS
SELECT note_id, title, created_at FROM notes
""")

conn.commit()


# ---------------- HOME PAGE ---------------- #
@app.route('/')
def home():
    return """
    <h1>📒 Notes App</h1>
    <a href='/add'>➕ Add Note</a><br><br>
    <a href='/view'>📄 View Notes</a><br>
    """


# ---------------- ADD NOTE ---------------- #
@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']

        cursor.execute(
            "INSERT INTO notes (title, content, created_at) VALUES (?, ?, ?)",
            (title, content, datetime.now())
        )
        conn.commit()

        return "✅ Note Added! <br><a href='/'>Back</a>"

    return """
    <h2>Add Note</h2>
    <form method='post'>
        Title: <input name='title'><br><br>
        Content: <input name='content'><br><br>
        <button type='submit'>Add</button>
    </form>
    """


# ---------------- VIEW NOTES ---------------- #
@app.route('/view')
def view():
    cursor.execute("SELECT * FROM notes_view ORDER BY title ASC")
    data = cursor.fetchall()

    output = "<h2>📄 Notes</h2><table border=1>"
    output += "<tr><th>ID</th><th>Title</th><th>Date</th></tr>"

    for row in data:
        output += f"<tr><td>{row[0]}</td><td>{row[1]}</td><td>{row[2]}</td></tr>"

    output += "</table><br><br><a href='/'>Back</a>"
    return output


# ---------------- RUN SERVER ---------------- #
if __name__ == "__main__":
    app.run(debug=True)