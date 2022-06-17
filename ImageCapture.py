from djitellopy import tello
import keys as kp
from time import sleep
import cv2

kp.init()

me = tello.Tello()
me.connect()
#print(me.get.battery())

me.turn_motor_off()
me.send_expansion_command("mled sc")

def getKeyboardInput():
    lr, fb, ud, yv = 0,0,0,0
    speed = 50

    if kp.getKey("LEFT"): lr = -speed
    elif kp.getKey("RIGHT"): lr = speed

    if kp.getKey("UP"): fb = speed
    elif kp.getKey("DOWN"): fb = -speed

    if kp.getKey("w"): ud = speed
    elif kp.getKey("s"): ud = -speed

    if kp.getKey("a"): yv = speed
    elif kp.getKey("d"): yv = -speed

    if kp.getKey("l"): me.land()
    if kp.getKey("t"): me.takeoff()

    if kp.getKey("m"):
        print("throw me")
        me.initiate_throw_takeoff()

    if kp.getKey("f"):
        me.flip("f")

    if kp.getKey("b"):
        print(me.get_battery())
    if kp.getKey("z"): me.send_expansion_command("mled l r 1.1 __Happy Easter!!")

    return [lr, fb, ud, yv]

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)



