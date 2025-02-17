import face_recognition
import cv2
import numpy as np
from os import listdir
import time

def FaceAuth():
    # Initialize video capture for the camera
    video_capture = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not video_capture.isOpened():
        print("Error: Cannot access the webcam.")
        return None

    known_face_encodings = []
    known_face_names = []

    # Load images from the "auth" folder
    try:
        for i in listdir("IMAGES\\auth\\"):
            image_path = f"IMAGES\\auth\\{i}"
            image = face_recognition.load_image_file(image_path)
            encodings = face_recognition.face_encodings(image)

            if len(encodings) == 0:
                print(f"Warning: No face found in image {i}. Skipping...")
                continue

            face_encoding = encodings[0]
            known_face_encodings.append(face_encoding)
            known_face_names.append(i.split(".")[0])

    except Exception as e:
        print(f"Error loading images: {e}")
        return None

    process_this_frame = True
    start_time = time.time()

    while True:
        # Check time limit (2 seconds)
        if time.time() - start_time > 2:
            print("Authentication timeout. No face recognized.")
            break

        ret, frame = video_capture.read()
        if not ret:
            print("Error reading frame from camera.")
            break

        # Resize frame for faster processing
        if process_this_frame:
            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
            rgb_small_frame = np.ascontiguousarray(small_frame[:, :, ::-1])

            # Detect and encode faces
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                name = "Unknown"

                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches and matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Handle recognition results
        for name in face_names:
            if name in known_face_names:
                print(f"Face recognized: {name}")
                video_capture.release()
                cv2.destroyAllWindows()
                return name

    video_capture.release()
    cv2.destroyAllWindows()
    return None

