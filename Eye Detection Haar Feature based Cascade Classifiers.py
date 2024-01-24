import cv2
# Load the pre-trained Haar Cascade classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade=cv2.CascadeClassifier(cv2.data.haarcascades+'haarcascade_eye_tree_eyeglasses.xml')
# Open a connection to the webcam (0 is usually the default webcam)
cap = cv2.VideoCapture(0)
# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()
# Define the codec and create a VideoWriter object for saving the output (optional)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640, 480))  # Change resolution if needed
while True:
    # Read a frame from the webcam
    ret, frameface = cap.read()
    # Break the loop if the video stream ends
    if not ret:
        print("Error: Failed to capture frame.")
        break
    # Convert the frame to grayscale for face detection
    grayface = cv2.cvtColor(frameface, cv2.COLOR_BGR2GRAY)
    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(grayface, scaleFactor=1.5, minNeighbors=5)
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        #cv2.rectangle(frameface, (x, y), (x+w, y+h), (0, 255, 0), 3)
        grayeye=grayface[y:y+h,x:x+w]
        frameeye=frameface[y:y+h,x:x+h]
        eyes=eye_cascade.detectMultiScale(grayeye,scaleFactor=1.4,minNeighbors=4)
        for(ex,ey,ew,eh) in eyes:
            cv2.rectangle(frameeye,(ex,ey),(ex+ew,ey+eh),(255,0,0),3)
    # Display the frame
    cv2.imshow('Face Detection', frameface)
    # Write the frame to the output video file (optional)
    out.write(frameface)
    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
# Release the video capture and writer objects
cap.release()
out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
