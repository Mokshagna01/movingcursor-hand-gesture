# Hand Gesture Control System

A computer vision project that allows users to control the computer using **hand gestures**.
This project uses **Python, OpenCV, and MediaPipe** to detect hand landmarks through the webcam and perform different actions like controlling the mouse cursor.

---

## Features

* Move mouse cursor using hand gestures
* Detect finger positions using MediaPipe
* Real-time hand tracking
* Gesture-based interaction with the computer
* Webcam-based control system

---

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI
* NumPy

---

## Project Structure

```
hand-gesture-control
│
├── movingcursor.py
├── gesture_click.py
├── gesture_scroll.py
└── README.md
```

---

## How It Works

1. The webcam captures real-time video.
2. MediaPipe detects hand landmarks.
3. Finger positions are analyzed.
4. Specific gestures trigger actions like:

   * Moving the cursor
   * Clicking
   * Scrolling

---

## Installation

Clone the repository:

```
git clone https://github.com/Mokshagna01/movingcursor-hand-gesture.git
```

Go to the project folder:

```
cd movingcursor-hand-gesture
```

Install required libraries:

```
pip install opencv-python mediapipe pyautogui numpy
```

---

## Run the Project

Example:

```
python movingcursor.py
```

Make sure your **webcam is enabled**.

---

## Applications

* Touchless computer interaction
* Accessibility tools
* Gesture-based interfaces
* Computer vision learning project

---

## Future Improvements

* Add more gesture commands
* Improve gesture accuracy
* Add gesture training model
* Build a GUI interface

---

## Author

Mokshagna Rajulapati

AI & Machine Learning Enthusiast
Interested in Computer Vision, NLP, and Multilingual AI Systems.

---

## License

This project is open source and available for learning and research purposes.
