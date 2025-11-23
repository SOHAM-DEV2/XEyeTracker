import cv2
import mediapipe as mp
import pyautogui
# Initialize camera
camera = cv2.VideoCapture(0)
# Mediapipe FaceMesh
face_mesh = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w, screen_h = pyautogui.size()
# smooth lists used to improve speed of cursor movements
smooth_x = []
smooth_y = []
smooth_limit = 5 # number of points to average
# HEAD NOD THRESHOLDS
previous_head_y = None
nod_threshold = 0.015  # adjustable threshold
while True:
    success, frame = camera.read()
    frame = cv2.flip(frame, 1) # used to correct image mirroring
    if success == False:
        break
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)

    frame_h, frame_w, _ = frame.shape

    if output.multi_face_landmarks:
        face = output.multi_face_landmarks[0]
        landmarks = face.landmark

        # -------------------------------------
        # IRIS LANDMARKS (474–478) FOR MOUSE
        # -------------------------------------
        for idx, lm in enumerate(landmarks[474:478]):
            x = int(lm.x * frame_w)
            y = int(lm.y * frame_h)

            cv2.circle(frame, (x, y), 3, (0, 255, 255), -1)

            if idx == 1:  # Use this point for cursor
                # Add to smoothing list
                smooth_x.append(x)
                smooth_y.append(y)

                # Ensure list max size
                if len(smooth_x) > smooth_limit:
                    smooth_x.pop(0)
                    smooth_y.pop(0)

                # Compute average
                avg_x = sum(smooth_x) / len(smooth_x)
                avg_y = sum(smooth_y) / len(smooth_y)

                screen_x = screen_w / frame_w * avg_x
                screen_y = screen_h / frame_h * avg_y

                pyautogui.moveTo(screen_x, screen_y, duration=0.01)

        # -------------------------------------
        # BLINK CLICK (left eye)
        # -------------------------------------
        left_eye = [landmarks[145], landmarks[159]]
        if (left_eye[0].y - left_eye[1].y) < 0.004:
            pyautogui.click()
            pyautogui.sleep(1)
            print("CLICK")

        # -------------------------------------
        # HEAD NOD SCROLLING
        # landmark 1 = near forehead / upper head
        # -------------------------------------
        head_y = landmarks[1].y

        if previous_head_y is not None:
            diff = head_y - previous_head_y

            # Nod down → scroll down
            if diff > nod_threshold:
                pyautogui.scroll(-300)
                print("SCROLL DOWN")

            # Nod up → scroll up
            elif diff < -nod_threshold:
                pyautogui.scroll(300)
                print("SCROLL UP")

        previous_head_y = head_y

    cv2.imshow("EyeTracking Control", frame)

    if cv2.waitKey(1) & 0xFF == 27:
        break

camera.release()
cv2.destroyAllWindows()
