import cv2
import datetime

cap = cv2.VideoCapture(0)
output_file = 'output.avi'
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
cap.set(3,1200)
cap.set(4,480)
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
frame_size = (frame_width, frame_height)
video_writer = cv2.VideoWriter(output_file, fourcc, fps, frame_size)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        print(cap.get(3))
        print(cap.get(4))
        dataset=str(datetime.datetime.now())
        print(dataset)
        font=cv2.FONT_HERSHEY_SIMPLEX
        frame=cv2.putText(frame,dataset,(255,50),font,0.5,(255,0,0),2)
    
        cv2.imshow('video', frame)

        if cv2.waitKey(1) == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()

