# Face Recognition Attendance System

This project implements a **Face Recognition Attendance System** using **Flask**, **OpenCV**, and the **face_recognition** library. The system uses a pre-trained model for recognizing faces in real-time and stores attendance records in a SQLite database with timestamps.

---

## Features

- 🎥 **Real-time Face Recognition**: Captures video feeds from a camera and identifies faces.
- 🗄️ **Database Integration**: Stores attendance data with timestamps in a SQLite database.
- 📁 **Face Encoding**: Processes images and generates face encodings for recognition.
- 🔄 **Dynamic Updates**: Easily update or add new faces for recognition.

---

## Folder Structure

```plaintext
face_recognition_attendance/
├── app.py                  # Flask app for the attendance system
├── capture_face.py         # Script to capture new faces and save images
├── check_encoding.py       # Verify stored encodings in encodings.pkl
├── create_attendance_table.py # Script to initialize the SQLite attendance table
├── create_database.py      # Script to initialize the database
├── encode_face.py          # Generate and save face encodings
├── encodings.pkl           # File containing face encodings
├── faces/
│   └── john/                 
│   ├── messi/
│   │   ├── messi1.jpg
│   │   └── messi2.jpg
├── recognition.py          # Main script for real-time face recognition
├── requirements.txt        # Python dependencies
├── static/                 # Static files for the Flask app
├── templates/              # HTML templates for the Flask app
├── test_database.py        # Script to test database functionality
├── update_encoding.py      # Update existing face encodings
├── attendance.db           # SQLite database file
```

---

## Prerequisites

- 🐍 Python 3.8 or later
- 🌐 Flask
- 🖼️ face_recognition
- 📹 OpenCV
- 🗄️ SQLite
- 🐍 Conda Environment

Install the required dependencies using:

```bash
pip install -r requirements.txt
```

---

## How to Run the Project

1. **Clone the Repository**

   ```bash
   git clone https://github.com/johnvarshith/face_recognition_attendance.git
   cd face_recognition_attendance
   ```

2. **Set Up the Conda Environment**
   Create and activate a Conda environment:

   ```bash
   conda create -n face_recognition python=3.8 -y
   conda activate face_recognition
   ```

   Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. **Set Up the Database**
   Run the script to create the SQLite database and attendance table:

   ```bash
   python create_database.py
   python create_attendance_table.py
   ```

4. **Add Faces**
   Place images of the individuals you want to recognize in the `faces/` directory, organized by folder names (e.g., `messi`, `john`).

5. **Generate Face Encodings**
   Run the following to generate encodings for the faces:

   ```bash
   python encode_face.py
   ```

6. **Run the Flask Application**
   Start the Flask app:

   ```bash
   python app.py
   ```

   Access the application at `http://127.0.0.1:5000` in your browser.

7. **Run Real-Time Recognition**
   Start the face recognition process:

   ```bash
   python recognition.py
   ```

---

## Files Explained

- **`app.py`**: Flask web application that acts as the interface for the attendance system.
- **`capture_face.py`**: Captures images for a new individual and saves them in the `faces/` directory.
- **`check_encoding.py`**: Loads and verifies the `encodings.pkl` file.
- **`create_attendance_table.py`**: Creates the `attendance` table in the database.
- **`create_database.py`**: Initializes the SQLite database.
- **`encode_face.py`**: Processes images in the `faces/` directory and saves face encodings to `encodings.pkl`.
- **`recognition.py`**: Detects and recognizes faces in real-time and logs attendance to the database.
- **`update_encoding.py`**: Updates or regenerates encodings for specific individuals.
- **`encodings.pkl`**: Stores face encodings for all individuals.
- **`attendance.db`**: SQLite database to store attendance records.
- **`test_database.py`**: Tests the connection and functionality of the SQLite database.

---

## SQLite Database Schema

**Table Name**: `attendance`

- 🆔 `id`: Primary key (integer)
- 🧍 `name`: Name of the recognized individual (text)
- ⏰ `timestamp`: Time of attendance logging (datetime)

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests. Follow the guidelines below:

- Fork the repository.
- Create a feature branch: `git checkout -b feature-name`.
- Commit your changes: `git commit -m 'Add some feature'`.
- Push to the branch: `git push origin feature-name`.
- Submit a pull request.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Developer Profile

**Janjarapu Varshithkar**  
[LinkedIn Profile](https://www.linkedin.com/in/janjarapu-varshithkar-927020271)

---

## requirements.txt

```
Flask==2.3.2
face_recognition==1.3.0
opencv-python==4.8.0.76
opencv-contrib-python==4.8.0.76
numpy==1.24.3
pandas==2.0.2
SQLAlchemy==2.0.17
```

