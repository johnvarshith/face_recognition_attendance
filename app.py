from flask import Flask, render_template, jsonify, Response
import face_recognition
import pickle
import sqlite3
import cv2

app = Flask(__name__)

# Load known face encodings
with open('encodings.pkl', 'rb') as f:
    known_encodings = pickle.load(f)

# Track attendance for the current session
attended = set()

def generate_frames():
    video_capture = cv2.VideoCapture(0)
    while True:
        ret, frame = video_capture.read()
        if not ret:
            break

        # Detect faces in the frame
        face_locations = face_recognition.face_locations(frame)
        face_encodings = face_recognition.face_encodings(frame, face_locations)

        for (top, right, bottom, left), encoding in zip(face_locations, face_encodings):
            # Compare the detected face encoding with the known encodings
            matches = face_recognition.compare_faces(list(known_encodings.values()), encoding)
            name = "Unknown"

            if True in matches:
                first_match_index = matches.index(True)
                name = list(known_encodings.keys())[first_match_index]

            # Mark attendance if a recognized person is detected and hasn't already attended
            if name != "Unknown" and name not in attended:
                # Insert into the attendance database
                conn = sqlite3.connect('attendance.db')
                cursor = conn.cursor()
                cursor.execute("INSERT INTO attendance (name) VALUES (?)", (name,))
                conn.commit()
                conn.close()

                # Mark this person as attended in this session
                attended.add(name)

            # Draw a box around the face and label it
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Encode the frame as a JPEG for streaming
        _, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()

        # Yield the frame as part of the video stream
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    video_capture.release()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/attendance_data')
def attendance_data():
    # Fetch attendance records from the database
    conn = sqlite3.connect('attendance.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM attendance")
    rows = cursor.fetchall()
    conn.close()

    # Convert database rows to a JSON-friendly format
    attendance_list = [{'id': row[0], 'name': row[1], 'timestamp': row[2]} for row in rows]
    return jsonify(attendance_list)

if __name__ == "__main__":
    app.run(debug=True)
