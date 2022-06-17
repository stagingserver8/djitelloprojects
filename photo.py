from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()

print(me.get.battery())
me.connect()
me.streamon()

while True:
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360,240))
    #Now create a window that will actually show this image. 'Image' is the name of the window, and it will desplay img in there
    cv2.imshow("Image", img)
    #Wait key needs to be added otherwise the frame will shut down before we can see it.
    cv2.waitKey(1)
