import face_recognition
import pickle
import sqlite3
import cv2
import time

# Load known face encodings
with open('encodings.pkl', 'rb') as f:
    known_encodings = pickle.load(f)

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Track attendance within this session
attended = set()

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
            # Insert into attendance database
            conn = sqlite3.connect('attendance.db')
            cursor = conn.cursor()
            cursor.execute("INSERT INTO attendance (name) VALUES (?)", (name,))
            conn.commit()
            conn.close()

            # Mark this person as attended in this session
            attended.add(name)
            print(f"Marked attendance for: {name}")

        # Draw a box around the face and label it
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        cv2.putText(frame, name, (left, top - 10), cv2.FONT_HERSHEY_DUPLEX, 0.5, (255, 255, 255), 1)

    cv2.imshow("Face Recognition Attendance", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture and close windows
video_capture.release()
cv2.destroyAllWindows()
