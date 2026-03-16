import cv2
import mediapipe as mp
import math

# Mediapipe hands setup
mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# Distance between two landmarks
def distance(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

# Check which fingers are up
def fingers_up(hand):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Detect Left / Right Hand
    if hand.landmark[17].x > hand.landmark[5].x:
        handed = "Right Hand"
    else:
        handed = "Left Hand"

    # Thumb rule depends on left/right
    if handed == "Right Hand":
        fingers.append(1 if hand.landmark[4].x < hand.landmark[3].x else 0)
    else:
        fingers.append(1 if hand.landmark[4].x > hand.landmark[3].x else 0)

    # Other fingers
    for id in range(1, 5):
        fingers.append(1 if hand.landmark[tip_ids[id]].y < hand.landmark[tip_ids[id]-2].y else 0)

    return fingers, handed

# Detect gesture based on fingers up
def detect_gesture(fingers, hand):
    # fingers structure = [thumb, index, middle, ring, pinky]

    # ==== PRIORITY 1: ADVANCED GESTURES ====

    # 👍 Thumbs Up (LIKE)
    if fingers == [1, 0, 0, 0, 0]:
        return "LIKE MODE 👍"

    # ✌ Peace
    if fingers == [0, 1, 1, 0, 0]:
        return "PEACE MODE ✌"

    # 👌 OK Sign (thumb + index touching)
    dist_ok = distance(hand.landmark[4], hand.landmark[8])
    if dist_ok < 0.035:   # small threshold
        return "OK MODE 👌"

    # 🤙 Call Me (thumb + pinky only)
    if fingers == [1, 0, 0, 0, 1]:
        return "CALL ME MODE 🤙"

    # ==== PRIORITY 2: NUMBERS ====
    total = sum(fingers)

    if total == 0:
        return "0 (FIST) ✊"
    if total == 1:
        return "1"
    if total == 2:
        return "2"
    if total == 3:
        return "3"
    if total == 4:
        return "4"
    if total == 5:
        return "5 (OPEN HAND ✋)"

    # ==== PRIORITY 3: BASIC GESTURES ====
    return "UNKNOWN"

# Start webcam
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            fingers, handed = fingers_up(handLms)
            gesture = detect_gesture(fingers, handLms)

            cv2.putText(frame, handed, (20, 60),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 0), 2)

            cv2.putText(frame, gesture, (20, 120),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Level 3 - Hand Gesture + Number + Advanced Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
