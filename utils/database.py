import sqlite3

DATABASE = "database/knowledge.db"

def create_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        filename TEXT,
        content TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_document(filename, content):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO documents (filename, content) VALUES (?, ?)",
        (filename, content)
    )

    conn.commit()
    conn.close()


def search_documents(keyword):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT filename, content FROM documents WHERE content LIKE ?",
        ('%' + keyword + '%',)
    )

    results = cursor.fetchall()

    conn.close()

    return results