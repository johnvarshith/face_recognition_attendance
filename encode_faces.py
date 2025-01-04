import face_recognition
import os
import pickle

def encode_faces():
    encodings = {}
    for folder in os.listdir('faces'):
        for image_file in os.listdir(f'faces/{folder}'):
            image_path = f'faces/{folder}/{image_file}'
            print(f"Processing: {image_path}")  # Debug info
            image = face_recognition.load_image_file(image_path)
            face_locations = face_recognition.face_locations(image)  # Detect face locations
            if len(face_locations) == 0:
                print(f"No face detected in {image_path}")
                continue
            try:
                encoding = face_recognition.face_encodings(image)[0]
                encodings[folder] = encoding
            except IndexError:
                print(f"Failed to encode {image_path}")
    with open('encodings.pkl', 'wb') as f:
        pickle.dump(encodings, f)

if __name__ == "__main__":
    encode_faces()
