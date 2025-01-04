import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('attendance.db')
cursor = conn.cursor()

# Query to check the tables in the database
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print("Tables:", tables)

# Query to check the attendance records (should be empty for now)
cursor.execute("SELECT * FROM attendance;")
records = cursor.fetchall()
print("Attendance Records:", records)

# Close the connection
conn.close()
