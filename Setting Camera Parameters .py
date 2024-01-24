import cv2
import datetime
cap=cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'mp4v')

fps=20
framesize=(50,10)
output_file='output.mp4'
video=cv2.VideoWriter(output_file,fourcc,fps,framesize)
while(cap.isOpened()):
    ret,frame=cap.read()
    if ret:
     print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
     print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

     video.write(frame)
     cv2.imshow('video',frame)

     if cv2.waitKey(1) == ord('q'):
        break
    else:
       break

cap.release()
cv2.destroyAllWindows()
