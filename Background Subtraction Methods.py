import cv2 as cv

path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject.mp4'
cap = cv.VideoCapture(path)

# Create a BackgroundSubtractorMOG2 object
bg_subtractor = cv.createBackgroundSubtractorMOG2()
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output19.avi', fourcc, 20.0, (640, 480))  # Change resolution if needed
while cap.isOpened():
    # Find the absolute difference between the two frames
    ret, frame = cap.read()
    if frame is None:
        break

    # Apply the background subtractor
    fg_mask = bg_subtractor.apply(frame)

    cv.imshow("Original Frame", frame)
    cv.imshow("Foreground Mask", fg_mask)
    out.write(fg_mask)
    if cv.waitKey(30) & 0xFF == 27:  # Press 'Esc' to exit
        break

cap.release()
cv.destroyAllWindows()
