import sqlite3

# Establish a connection to SQLite (replace with your SQLite database file path)
conn = sqlite3.connect('attendance.db')  # SQLite file-based database

# Create a cursor object to interact with the database
cursor = conn.cursor()

# SQL query to create the attendance table if it doesn't already exist
cursor.execute('''
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY AUTOINCREMENT,  -- Auto-incrementing primary key
        name TEXT,                             -- Column for name
        timestamp DATETIME DEFAULT CURRENT_TIMESTAMP  -- Automatically sets current timestamp
    )
''')

# Commit changes to the database
conn.commit()

# Close the connection
conn.close()
