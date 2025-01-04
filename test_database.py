import sqlite3

def test_database():
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()
    print("Database connection successful!")
    print("Current records in attendance table:", rows)

if __name__ == "__main__":
    test_database()
