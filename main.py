from djitellopy import tello
from time import sleep
import cv2

me = tello.Tello()
me.connect()

me.takeoff()

#me.send_expansion_command("led br 1.1 255 0 0")
#me.send_expansion_command("mled l r 1.1 Love you Zhenya!")
#Starting the steam. Because it is a continous nr of frames we have to use a while loop.

sleep(4)
me.land()
