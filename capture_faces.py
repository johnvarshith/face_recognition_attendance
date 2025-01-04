import cv2
import face_recognition
import os
import uuid

def capture_faces():
    # Create directory to store face images if it doesn't exist
    if not os.path.exists('faces'):
        os.makedirs('faces')

    # Input validation for name
    name = input("Enter the name of the person: ")
    while not name.strip():
        name = input("Name cannot be empty. Enter the name of the person: ")

    folder_path = f'faces/{name}'
    os.makedirs(folder_path, exist_ok=True)

    # User-defined number of images
    num_images = int(input("Enter the number of images to capture: "))

    video_capture = cv2.VideoCapture(0)
    count = 0

    while count < num_images:  # Capture user-defined number of images
        ret, frame = video_capture.read()
        if not ret:
            print("Failed to capture image")
            break

        face_locations = face_recognition.face_locations(frame)
        if not face_locations:
            print("No face detected. Adjust your position and try again.")
            continue

        for (top, right, bottom, left) in face_locations:
            face_image = frame[top:bottom, left:right]
            unique_id = uuid.uuid4().hex
            cv2.imwrite(f"{folder_path}/{name}_{unique_id}.jpg", face_image)
            count += 1
            print(f"Captured {count}/{num_images} images.")

        cv2.imshow("Capturing Faces", frame)

        # Exit on pressing 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("Exiting the program...")
            break

    video_capture.release()
    cv2.destroyAllWindows()
    print(f"Captured {count} images for {name}.")

if __name__ == "__main__":
    capture_faces()