import pygame
#Detecting key press

#function init
def init():
    pygame.init()
    win = pygame.display.set_mode((400,400))

# fucntion, if called, tells us if the key has been pressed or not.

def getKey(keyName):
    ans = False
    for eve in pygame.event.get(): pass
    keyInput = pygame.key.get_pressed()
    myKey = getattr(pygame, 'K_{}'.format(keyName)) #Setting format K_LEFT if left button is pressed
    if keyInput[myKey]:
        ans = True
    pygame.display.update()
    return ans

def main():
    if getKey("LEFT"):
        print("Left key pressed")
    if getKey("RIGHT"):
        print("Right key pressed")


if __name__ == '__main__': #if I am running this as a main file, do this, otherwise do not do it
    init()
    while True:
        main();

#Get the key press





