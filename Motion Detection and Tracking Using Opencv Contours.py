import cv2

path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\people.mp4'
cap = cv2.VideoCapture(path)
video = cv2.VideoWriter
ret1, frame1 = cap.read()
ret2, frame2 = cap.read()

while cap.isOpened():
    # find the absolute difference between the 2 frames
    diff = cv2.absdiff(frame1, frame2)
    # to find the contours
    gray = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, binary = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)  # Use "_" to discard the threshold value
    dilated = cv2.dilate(binary, None, iterations=3)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        # save the coordinates of all the contours
        if cv2.contourArea(contour) < 3000:
            continue
        (x, y, z, t) = cv2.boundingRect(contour)
        cv2.rectangle(frame1, (x, y), (x + z, y + t), (0, 255, 0), 2)

    # cv2.drawContours(frame1, contours, -1, (0, 0, 255), 2)
    cv2.imshow("inter", frame1)
    frame1 = frame2
    ret, frame2 = cap.read()

    if cv2.waitKey(40) == 27:
        break

cv2.destroyAllWindows()
cap.release()  # Remove the extra colon at the end
