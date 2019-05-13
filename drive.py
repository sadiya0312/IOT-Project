import os
import voiceRec
import led
import motor
import time
import turn
import ultra
import matplotlib
import server
import Adafruit_PCA9685
import picamera
from picamera.array import PiRGBArray
from io import BytesIO
import speech
#import pyautogui
import subprocess
#pwm = Adafruit_PCA9685.PCA9685()    #Ultrasonic Control

dis_dir = []
distance_stay  = 0.4
distance_range = 2
led_status = 0

left_R = 15
left_G = 16
left_B = 18

right_R = 19
right_G = 21
right_B = 22

spd_ad     = 1          #Speed Adjustment
pwm0       = 0          #Camera direction 
pwm1       = 1          #Ultrasonic direction
status     = 1          #Motor rotation
forward    = 1          #Motor forward
backward   = 0          #Motor backward

left_spd   = 100         #Speed of the car
right_spd  = 100         #Speed of the car
left       = 100         #Motor Left
right      = 100         #Motor Right

spd_ad_1 = 1
spd_ad_2 = 1
spd_ad_u = 1

#Status of the car
auto_status   = 0
ap_status     = 0
turn_status   = 0

opencv_mode   = 0
findline_mode = 0
speech_mode   = 0
auto_mode     = 0
pwm = Adafruit_PCA9685.PCA9685()
pwm.set_pwm_freq(60)
data = ''

dis_data = 0
dis_scan = 1
#######
ultra.setup()
theta = []
rad = []
start = 0



def turnLeft():
    
    turn.middle()
    time.sleep(0.5)
    motor.setup()
    turn.left()
    motor.motor_right(1,0,100)
    time.sleep(3.5)
    
    motor.destroy()


def turnRight():

    turn.middle()
    time.sleep(.5)
    motor.setup()
    turn.right()
    motor.motor_right(1,0,100)
    time.sleep(3.5)

    motor.destroy()

def forward(feet):

    wait = feet/1.8

    if feet >= 8:
        wait -= 1.2
    elif (feet <= 7) & (feet >= 4):
        wait -= feet*.1

    turn.middle()
    time.sleep(0.1)
    motor.setup()
    motor.motor_right(1,0,100)
    time.sleep(wait)

    motor.destroy()

def backward(feet):

    wait = feet/1.8

    if feet >= 8:
        wait -= 1.2
    elif (feet <= 7) & (feet >= 4):
        wait -= feet*.04

    turn.middle()
    time.sleep(0.1)
    motor.setup()
    motor.motor_right(1,1,100)
    time.sleep(wait)

    motor.destroy()

def flip(turns, arc):

    fullTurn = 4
    wait = fullTurn / arc

    turn.middle()
    motor.setup()
    for i in range(turns):

        if i % 2 == 0:
            turn.left()
            motor.motor_right(1,0,100)
            time.sleep(wait-.25)
        else:
            turn.right()
            motor.motor_right(1,1,100)
            time.sleep(wait+.25)

    motor.destroy()

def recognize(): # num = 1,3,9

    led.setup()

    turn.ahead()
    led.green()
    time.sleep(.5)

    pwm.set_pwm(0,0,180)
    time.sleep(.5)
    led.both_off()
    led.red()

    camera = picamera.PiCamera()
    camera.resolution = (640,480)
    camera.start_preview()
    time.sleep(2)

    camera.capture('/home/pi/Desktop/testimg.jpg')
    time.sleep(1)
    camera.stop_preview()
    copy_file = subprocess.Popen(["scp", "/home/pi/Desktop/testimg.jpg", "sadiyaahmad@hopper.slu.edu:~/workspace/IOT/"])
    copy_wait = os.waitpid(copy_file.pid, 0)
   
#    os.system("scp /home/pi/Desktop/testimg.jpg sadiyaahmad@hopper.slu.edu:~/testimage.jpg")
    #/workspace/IOT/testImg.jpg")
    #pyautogui.press('enter')
   

    time.sleep(.5)
    led.both_off()

    time.sleep(.5)

    turn.ahead()

def forward_sonar():
    hold = []
    motor.setup()
    turn.ahead()
    time.sleep(0.25)
    turn.middle()
    time.sleep(0.25)
    while all(i > 2 for i in hold[:-7:-1]):
        hold.append(ultra.checkdist())
        print(ultra.checkdist())
        motor.motor_right(1, 0, 100)
        time.sleep(0.5)
    motor.destroy()

def voiceRecognition():
    voice = voiceRec.voice()
    voice.main("/home/pi/Desktop/Adeept_PiCar-B/server/test.csv")

def pan():
    for i in range(100):
        pwm.set_pwm(1,0,180+(i*25))
        time.sleep(0.5)
#recognize()
#backward(3)
#forward(7)
#turnLeft()
#turn.middle()
#motor.motor_right(1,0,100)
#time.sleep(2)
#turnRight()
#flip(5,2)
while True:
    print(' 1. Forward [distance] \n 2. Forward [sonar] \n 3. Backward \n 4. Turn Left \n 5. Turn Right \n 6. Turn Around \n 7. Recoqnize \n 8. Voice Recognition')
    directions = int(input('\nSelect an action [1-6]: '))
    if directions == 1:
         dist = int(input('Enter distance in feet you want to travel forwards: '))
         forward(dist)
    elif directions == 2:
         forward_sonar()
    elif directions == 3:
         dist = int(input('Enter distance in feet you want to travel backwards: '))
         backward(dist)
    elif directions == 4:
         turnLeft()
    elif directions == 5:
         turnRight()
    elif directions == 6:
         flip(5,2)
    elif directions == 7:
         recognize()
    elif directions == 8:
         voiceRecognition()
    elif directions == 9:
         pan()
