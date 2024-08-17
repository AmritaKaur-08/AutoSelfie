import cv2
import datetime
# Initialize the camera capture and cascade classifiers
cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_smile.xml')

while True:
    # Capture the frame
    _, frame = cap.read()
    
    # Copy the original frame correctly
    original_frame = frame.copy()
    
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    for (x, y, w, h) in faces:
        # Draw rectangle around the face
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 2)
        
        # Define the region of interest (ROI) for the face
        face_roi = frame[y:y+h, x:x+w]
        gray_roi = gray[y:y+h, x:x+w]
        
        # Detect smiles within the face ROI
        smiles = smile_cascade.detectMultiScale(gray_roi, 1.3, 25)
        
        for (x1, y1, w1, h1) in smiles:
            # Draw rectangle around the smile
            cv2.rectangle(face_roi, (x1, y1), (x1+w1, y1+h1), (0, 0, 255), 2)
            time_stamp=datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')
            file_name=f'selfie-{time_stamp}.png'
            # Save the original frame without rectangles
            cv2.imwrite(file_name, original_frame)
    
    # Display the frame with rectangles
    cv2.imshow('cam star', frame)
    
    # Break the loop if 'q' is pressed
    if cv2.waitKey(10) == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
