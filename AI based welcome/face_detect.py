import cv2
import pyttsx3

# Function to capture an image from the camera and check for faces
def capture_image():
    # Initialize the camera
    cap = cv2.VideoCapture(0)
    
    # Check if the camera opened successfully
    if not cap.isOpened():
        print("Error: Could not open camera")
        return None
    
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    
    while True:
        # Capture a single frame
        ret, frame = cap.read()
        
        # Check if the frame was captured successfully
        if not ret:
            print("Error: Could not capture image")
            continue
        
        # Convert frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Detect faces in the frame
        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
        
        # Draw rectangle around the faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        
        # Display the resulting frame
        cv2.imshow('Captured Image', frame)
        
        # If faces are detected, convert text to speech and play it
        if len(faces) > 0:
            text_to_speech("Welcome")
        
        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the camera and close all OpenCV windows
    cap.release()
    cv2.destroyAllWindows()

# Function to convert text to speech and play it
def text_to_speech(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    # Set properties (optional)
    engine.setProperty('rate', 150)    # Speed of speech
    engine.setProperty('volume', 1)    # Volume (0.0 to 1.0)
    
    # Convert text to speech
    engine.say(text)
    
    # Play the speech
    engine.runAndWait()

# Main function
def main():
    # Capture an image and check for faces
    capture_image()

# Run the main function
if __name__ == "__main__":
    main()
