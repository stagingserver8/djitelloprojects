import cv2
import numpy as np
from djitellopy import tello
import time

me = tello.Tello()
me.connect()
print(me.get_battery())

me.streamon()
me.takeoff()

me.send_rc_control(0,0, 4, 0)
time.sleep(2.2)

#PID controller

w, h = 360, 240
fbRange = [6200, 6800]
pid = [0.4, 0.4, 0]
pError = 0

def findFace(img):
    faceCascade = cv2.CascadeClassifier("face.xml")
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(imgGray, 1.2, 8)

    #Create a list of all the faces

    myFaceListC = [] #cx, cy - where is our face detected
    myFaceListArea = []  #our face area

    #Whever it detects a face it will return a value

    for (x,y, w,h) in faces:
        #draw a rectangle
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        cx = x+w // 2
        cy= y+h // 2
        area = w * h
        cv2.circle(img, (cx,cy),5,(0,255,0), cv2.FILLED)
        myFaceListC.append([cx,cy])
        myFaceListArea.append(area)
    if len(myFaceListArea) != 0:
         i = myFaceListArea.index(max(myFaceListArea))
         return img, [myFaceListC[i], myFaceListArea[i]]
    else:
         return img, [[0,0],0]

def trackFace( info, w, pid, pError):
    area = info[1]
    x,y = info[0]
    fb = 0
    #PID, errors
    error = x - w//2
    speed = pid[0]*error + pid[1]*(error-pError)
    #new speed for yaw
    speed = int(np.clip(speed,-100,100))

    #condition to stay stationary. Green zone, drone will not move
    if area > fbRange[0] and area <  fbRange[1]:
        fb=0
    #too close, go backwards!
    elif area > fbRange[1]:
        fb=-20
    #too small? Go forward!
    elif area < fbRange[0] and area !=0:
        fb=20
    #if we dont detect anything , we should stop


    if x==0:
        speed = 0
        error = 0

    #print(speed, fb)

    me.send_rc_control(0, fb, 0, speed)
    return error
    #Viola-Jones object detection framework. File is on OpecCV


#cap = cv2.VideoCapture(0)

#Standard code for running webcam with open CV
while True:
    #_, img= cap.read()
    img = me.get_frame_read().frame
    img = cv2.resize(img, (w,h))
    img, info = findFace(img)
    pError = trackFace( info, w, pid, pError)
    #print("Center", info[0], "Area", info[1])
    cv2.imshow("Output", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
    #when we press q button it stops




