import cv2
import numpy as np

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)

def click_event(event, x, y, flags, par):
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x, ' , ', y)
        font = cv2.FONT_HERSHEY_PLAIN
        text = f'Coordinates: ({x},{y})'

        # Create a blank image to display live coordinates
        live_coordinates_img = np.zeros((100, 300, 3), np.uint8)
        cv2.putText(live_coordinates_img, text, (10, 40), font, 1, (255, 255, 255), 2)

        # Display the live coordinates window
        cv2.imshow('Live Coordinates', live_coordinates_img)

        # Draw the coordinates on the original image
        cv2.putText(img, text, (x, y), font, 1, (255, 0, 0), 2)
        cv2.imshow('image', img)

# Load your image
path = r'C:\Users\T.M.S\OneDrive\Bureau\pythonProject\photo.jpg'
img = cv2.imread(path)

# Create a window for the image
cv2.imshow('image', img)

# Set mouse callback
cv2.setMouseCallback('image', click_event)

while True:
    key = cv2.waitKey(1) & 0xFF
    # Close the program when 'esc' key is pressed
    if key == 27:
        break

cv2.destroyAllWindows()
