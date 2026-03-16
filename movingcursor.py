import cv2
import mediapipe as mp
import pyautogui

# Screen size
screen_width, screen_height = pyautogui.size()

# Mediapipe hands setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# For smoothing cursor movement
prev_x, prev_y = 0, 0
smoothening = 5

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            # Index finger tip
            x_norm = handLms.landmark[8].x
            y_norm = handLms.landmark[8].y

            # Convert to screen coordinates
            screen_x = int(screen_width * x_norm)
            screen_y = int(screen_height * y_norm)

            # Smooth movement
            curr_x = prev_x + (screen_x - prev_x) / smoothening
            curr_y = prev_y + (screen_y - prev_y) / smoothening

            pyautogui.moveTo(curr_x, curr_y)
            prev_x, prev_y = curr_x, curr_y

    cv2.imshow("Hand Cursor Control", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
