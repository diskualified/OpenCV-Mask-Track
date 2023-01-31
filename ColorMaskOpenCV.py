# import the opencv library
import cv2
import numpy as np

# define a video capture object
vid = cv2.VideoCapture(0)

while(True):
    ret, frame = vid.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    lower_orange = np.array([10, 180, 140])
    upper_orange = np.array([25, 255, 255])

    # Create a mask. Threshold the HSV image to get only orange colors
    mask = cv2.inRange(hsv, lower_orange, upper_orange)
    coords = cv2.findNonZero(mask)
    if coords is not None and len(coords) > 1:
        coord = coords[0]
        color = (255, 0, 0) # blue
        mask = cv2.circle(mask, (coord[0][0], coord[0][1]), 100, color, 2)
        frame = cv2.circle(frame, (coord[0][0], coord[0][1]), 100, color, 2)
    # cv2.imshow('mask', mask) # black and white mask option
    cv2.imshow('frame', frame)
    
    # press q to exit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
