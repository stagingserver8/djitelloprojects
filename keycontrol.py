from djitellopy import tello
import keys as kp
from time import sleep
import cv2

kp.init()
me = tello.Tello()
me.connect()
#me.send_expansion_command("mled sc")

me.streamon()

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("d"): yv = speed
    elif kp.getKey("a"): yv = -speed

    if kp.getKey("l"): me.land()
    if kp.getKey("t"): me.takeoff()

    if kp.getKey("m"):
        print("throw me")
        me.initiate_throw_takeoff()

    if kp.getKey("f"):
        me.flip_forward()
        me.flip_forward()

    if kp.getKey("b"):
        print(me.get_battery())
    #if kp.getKey("z"): me.send_expansion_command("mled l r 1.1 __Happy Easter!!")

    return [lr, fb, ud, yv]


while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    img = me.get_frame_read().frame
    img = cv2.resize(img, (360, 240))
    # Now create a window that will actually show this image. 'Image' is the name of the window, and it will desplay img in there
    cv2.imshow("Image", img)
    cv2.waitKey(1)


