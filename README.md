Automated Burnt Cracker Detection System
Overview
This project uses a Basler camera and YOLOv8 model to detect burnt cracker sticks in real-time on a production line. The system continuously captures images from the camera, processes them with a pre-trained YOLO model to detect objects (i.e., burnt crackers), and displays the results on a video feed.

Requirements
Python 3.x

OpenCV: For video display and image processing.

pypylon: For interacting with Basler cameras.

Ultralytics YOLO: For object detection.

supervision: For video frame handling.

To install the required dependencies, you can use pip:

pip install opencv-python pypylon ultralytics supervision

How it Works
Camera Initialization:
The Basler camera is initialized and connected to the first available device.

Real-time Image Capture:
The camera captures frames continuously with minimal delay using the GrabStrategy_LatestImageOnly method.

Object Detection:
YOLOv8 (a pre-trained model) is used to detect burnt crackers in the frames. The coordinates of detected objects are extracted and displayed on the video feed.

Display and FPS Calculation:
Detected objects (burnt crackers) are highlighted with bounding boxes, and the frame rate (FPS) is calculated and displayed on the video feed for performance monitoring.

Real-time Output:
The processed frames are displayed in a window, and the program continues until the user presses the "Escape" key (ESC).

How to Run
Make sure you have all the dependencies installed.

Connect your Basler camera to the computer.

Place the pre-trained YOLOv8 model (forcuda.pt) in the specified directory (C:/Users/talha/forcuda.pt).

Run the Python script to start the real-time detection.

python detect_burnt_crackers.py

Key Points:
Camera Setup: Basler camera is used for high-speed image capture.

YOLOv8 Model: YOLO is a real-time object detection model, used to identify burnt crackers.

FPS Display: Displays the frame rate in real-time to assess the performance of the detection process.

Project Files
detect_burnt_crackers.py: The main script for real-time object detection.

forcuda.pt: The pre-trained YOLOv8 model file.

License
This project is open-source and can be used for educational or commercial purposes. Modify it to suit your production line needs.

Author
Talha Akbas

