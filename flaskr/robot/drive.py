import sys
from time import sleep
#import RPi.#GPIO as #GPIO
#GPIO.setmode(#GPIO.BOARD)
#mode=GPIO.getmode()

'''
GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)
'''

y = 0
x = 0
speed = 0
sleeptime= 1

#Pins used for motor controller
rightForward=35
rightBackward=37
leftForward=36
leftBackward=38

class basicMovement:
    def left_forward(x):
        #GPIO.output(leftForward, GPIO.HIGH)
        print("Moving Forward")
        sleep(x)
        #GPIO.output(leftBackward, GPIO.LOW)

    def left_reverse(x):
        #GPIO.output(leftForward, GPIO.HIGH)
        print("Moving Backward")
        sleep(x)
        #GPIO.output(leftBackward, GPIO.LOW)

    def right_forward(x):
        #GPIO.output(rightForward, GPIO.HIGH)
        #GPIO.output(rightBackward, GPIO.LOW)
        print("Moving Forward")
        sleep(x)
        #GPIO.output(rightForward, GPIO.LOW)

    def right_reverse(x):
        #GPIO.output(rightForward, GPIO.LOW)
        #GPIO.output(rightBackward, GPIO.HIGH)
        print("Moving Forward")
        sleep(x)
        #GPIO.output(leftForward, GPIO.LOW)

    def stop():
        print("Stoppppppping")
        #GPIO.output(leftForward, GPIO.LOW)
        #GPIO.output(leftBackward, GPIO.LOW)
        #GPIO.output(rightForward, GPIO.LOW)
        #GPIO.output(rightBackward, GPIO.LOW)

def forword():
    print("forword")
    print("Moving Forword")
    basicMovement.left_forward()
    basicMovement.right_forward()

def backword():
    print("Moving Backword")
    basicMovement.left_backword()
    basicMovement.right_backword()

def left():
    print("Moving Left")
    basicMovement.right_forward()
    basicMovement.right_backword()

def right():
    print("Moving Right")
    basicMovement.left_forward()
    basicMovement.left_backword()

def up():
    print("UP")
    #code goes here

def down():
    print("DOWN")
    #code goes here

def openclose():
    print("OPENING/CLOSING")
    #code goes here

def shoot():
    print("SHOOT")


#GPIO.cleanup()


'''

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftForward, GPIO.OUT)
GPIO.setup(leftBackward, GPIO.OUT)
GPIO.setup(rightForward, GPIO.OUT)
GPIO.setup(rightBackward, GPIO.OUT)

def left_forward(x):
   GPIO.output(leftForward, GPIO.HIGH)
   print("Moving Forward")
   sleep(x)
   GPIO.output(leftBackward, GPIO.LOW)

def left_reverse(x):
   GPIO.output(leftForward, GPIO.HIGH)
   print("Moving Backward")
   sleep(x)
   GPIO.output(leftBackward, GPIO.LOW)

def right_forward(x):
   GPIO.output(rightForward, GPIO.HIGH)
   GPIO.output(rightBackward, GPIO.LOW)
   print("Moving Forward")
   sleep(x)
   GPIO.output(rightForward, GPIO.LOW)

def right_reverse(x):
   GPIO.output(rightForward, GPIO.LOW)
   GPIO.output(rightBackward, GPIO.HIGH)
   print("Moving Forward")
   sleep(x)
   GPIO.output(leftForward, GPIO.LOW)


def stop():
   print("Stoppppppping")
   GPIO.output(leftForward, GPIO.LOW)
   GPIO.output(leftBackward, GPIO.LOW)
   GPIO.output(rightForward, GPIO.LOW)
   GPIO.output(rightBackward, GPIO.LOW)

GPIO.cleanup()

'''
