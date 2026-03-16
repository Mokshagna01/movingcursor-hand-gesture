import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)

def fingers_up(hand):
    tip_ids = [4, 8, 12, 16, 20]
    fingers = []

    # Thumb (special case)
    if hand.landmark[tip_ids[0]].x < hand.landmark[tip_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for id in range(1, 5):
        if hand.landmark[tip_ids[id]].y < hand.landmark[tip_ids[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


def detect_gesture(fingers):
    total = sum(fingers)

    # Gesture Rules
    if total == 0:
        return "FIST ✊"
    elif total == 5:
        return "OPEN PALM ✋"
    elif total == 1 and fingers[0] == 1:
        return "THUMBS UP 👍"
    elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 0 and fingers[4] == 0:
        return "PEACE ✌"
    elif fingers[1] == 1 and fingers[2] == 1 and fingers[3] == 1 and fingers[4] == 1:
        # For OK: index+thumb make a circle → thumb near index
        return "FOUR FINGERS"
    else:
        return "UNKNOWN"


cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    frame = cv2.flip(frame, 1)

    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb)

    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, handLms, mp_hands.HAND_CONNECTIONS)

            fingers = fingers_up(handLms)
            gesture = detect_gesture(fingers)

            cv2.putText(frame, gesture, (50, 80),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 3)

    cv2.imshow("Custom Gesture Detection - Level 2", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
