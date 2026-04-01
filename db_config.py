# Database connection file

import mysql.connector

def get_connection():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Mac@123",  # 🔁 CHANGE THIS
            database="notes_db"
        )
        return conn
    except Exception as e:
        print("❌ Connection Error:", e)
        exit()