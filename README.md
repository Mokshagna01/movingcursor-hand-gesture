# Hand Gesture Cursor Control

## Overview

This project demonstrates a simple **hand gesture based mouse cursor control system** using a webcam.
The program tracks the **index finger of a hand** using computer vision and moves the mouse cursor on the screen accordingly.

It uses real-time hand tracking to convert **hand movements into cursor movements**, enabling touch-free computer interaction.

## Features

* Real-time hand detection using a webcam
* Cursor movement using index finger position
* Smooth cursor motion
* Simple and lightweight implementation

## Technologies Used

* Python
* OpenCV
* MediaPipe
* PyAutoGUI

## How It Works

1. The webcam captures live video.
2. MediaPipe detects the hand landmarks.
3. The program identifies the **index finger tip position**.
4. The finger position is mapped to screen coordinates.
5. The mouse cursor moves according to the finger movement.

## Installation

Install the required libraries:

pip install opencv-python mediapipe pyautogui

## Run the Program

Run the script using:

python movingcursor.py

## Controls

* Move your **index finger** to control the mouse cursor.
* Press **Q** to close the webcam and exit the program.

## Future Improvements

* Add gesture based mouse click
* Add scrolling gesture
* Add drag and drop gesture
* Improve gesture recognition accuracy

## Author

Mokshagna
