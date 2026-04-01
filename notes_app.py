from db_config import get_connection
from datetime import datetime

# Connect DB
conn = get_connection()
cursor = conn.cursor()

# ---------- CREATE NOTE ----------
def add_note():
    try:
        title = input("Enter title: ")
        content = input("Enter content: ")

        query = "INSERT INTO notes (title, content, created_at) VALUES (%s, %s, %s)"
        cursor.execute(query, (title, content, datetime.now()))
        conn.commit()

        print("✅ Note Added!\n")

    except Exception as e:
        print("❌ Error:", e)


# ---------- VIEW NOTES ----------
def view_notes():
    try:
        cursor.execute("SELECT * FROM notes_view ORDER BY title ASC")
        data = cursor.fetchall()

        print("\n📒 Notes:")
        for row in data:
            print(f"ID: {row[0]} | Title: {row[1]} | Date: {row[2]}")
        print()

    except Exception as e:
        print("❌ Error:", e)


# ---------- SEARCH ----------
def search_note():
    title = input("Enter title: ")

    cursor.execute("SELECT * FROM notes WHERE title LIKE %s", ('%' + title + '%',))
    data = cursor.fetchall()

    print("\n🔍 Results:")
    for row in data:
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()


# ---------- UPDATE ----------
def update_note():
    note_id = input("Enter ID: ")

    new_title = input("New title: ")
    new_content = input("New content: ")

    cursor.execute(
        "UPDATE notes SET title=%s, content=%s WHERE note_id=%s",
        (new_title, new_content, note_id)
    )
    conn.commit()

    print("✏️ Updated!\n")


# ---------- DELETE ----------
def delete_note():
    note_id = input("Enter ID: ")

    cursor.execute("DELETE FROM notes WHERE note_id=%s", (note_id,))
    conn.commit()

    print("🗑️ Deleted!\n")


# ---------- MENU ----------
def menu():
    while True:
        print("\n====== NOTES APP ======")
        print("1. Add")
        print("2. View")
        print("3. Search")
        print("4. Update")
        print("5. Delete")
        print("6. Exit")

        ch = input("Choice: ")

        if ch == '1':
            add_note()
        elif ch == '2':
            view_notes()
        elif ch == '3':
            search_note()
        elif ch == '4':
            update_note()
        elif ch == '5':
            delete_note()
        elif ch == '6':
            print("👋 Bye!")
            break
        else:
            print("❌ Invalid!")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    menu()