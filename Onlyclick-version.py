# Import OpenCV library for video capture and image processing
import cv2
import mediapipe as mp
import pyautogui

# Initialize camera (0 = default webcam)
camera = cv2.VideoCapture(0)

# Initialize Mediapipe Face Mesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)

screen_w, screen_h = pyautogui.size()

# Previous smoothed cursor positions
smooth_x, smooth_y = 0, 0

while True:
    # Read a frame from the camera
    success, frame = camera.read()
    frame = cv2.flip(frame, 1)
    if not success:
        print("Failed to read camera")
        break

    # Convert BGR→RGB for Mediapipe processing
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    # Safeguard: check if landmarks detected
    if output.multi_face_landmarks:
        face = output.multi_face_landmarks[0]
        landmarks = face.landmark

        # Get frame dimensions (height, width)
        frame_h, frame_w, _ = frame.shape

        # Eye landmark points (iris)
        for id1, landmark in enumerate(landmarks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (255, 0, 0), cv2.FILLED)

            if id1 == 1:  # Use the specific landmark for gaze point
                target_x = (screen_w / frame_w) * x
                target_y = (screen_h / frame_h) * y


                smooth_x = smooth_x + (target_x - smooth_x) * 0.20
                smooth_y = smooth_y + (target_y - smooth_y) * 0.20

                pyautogui.moveTo(smooth_x, smooth_y)

        # Blink detection
        left_eye = [landmarks[145], landmarks[159]]
        for landmark in left_eye:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h)
            cv2.circle(frame, (x, y), 2, (255, 0, 0), cv2.FILLED)

        # Blink to click
        if (left_eye[0].y - left_eye[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
            print("click")

        # Display the frame with landmarks
    cv2.imshow('EyeTracking', frame)

    # Exit when ESC (27) is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release camera properly
camera.release()
cv2.destroyAllWindows()
