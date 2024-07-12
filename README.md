# Ai-based-welcome-system
Libraries Used:

cv2 (OpenCV): For image and video capture and processing.
pyttsx3: For text-to-speech conversion.
Functionality:

Captures an image from the camera.
Converts the image to grayscale.
Uses a pre-trained Haar Cascade classifier to detect faces.
Draws rectangles around detected faces.
Uses text-to-speech to indicate the number of faces detected.
Based on this, here's a suitable README file content for your project:

Face Detection with Audio Feedback
This project demonstrates a simple face detection application using OpenCV and text-to-speech feedback using pyttsx3.

Features
Captures real-time video from the webcam.
Detects faces in the video stream.
Provides audio feedback on the number of faces detected.
Installation
To run this project, you'll need to have Python installed along with the required libraries. Follow the instructions below to set up your environment:

Clone the repository:

bash
Copy code
git clone https://github.com/yourusername/face-detection.git
cd face-detection
Install required libraries:

bash
Copy code
pip install opencv-python pyttsx3
Usage
Run the script to start the face detection:

bash
Copy code
python face_detect.py
The application will open your webcam, detect faces in real-time, and provide audio feedback on the number of faces detected.

Code Overview
face_detect.py: The main script that captures video from the webcam, detects faces, and provides audio feedback.
Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

License
This project is licensed under the MIT License. See the LICENSE file for details.
