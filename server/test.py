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
turn.left()
ultra.setup()
theta = []
rad = []
start = 0
#for i in range(3):
    
    #motor.setup()
    #motor.motor_right(1, 0, 100)
    #time.sleep(10)
    #motor.destroy()
    #time.sleep(2)
    #for i in range(300, 550, 5):
    #    turn.turn_ang(i)
    #    time.sleep(.05)
    #    rad.append(ultra.checkdist())
    #    theta.append(i-250)
    #for i in range(550, 300, -5):
    #    turn.turn_ang(i)
    #    time.sleep(.05)
    #    rad.append(ultra.checkdist())
    #   theta.append(i-250)
    #start += 1
    
    #print(start)
### SONAR ###
# 250 LEFT MAX
# 550 RIGHT MAX
# 400 STRAIGHT
### CAMERA ###
#pwm.set_pwm(1, 0, 400)
#time.sleep(1)
# 240 UPWARDS MAX
# 400 DOWNWARDS MAX
# 320 MIDDLE

### CAMERA PICTURE ###
#camera = picamera.PiCamera()              #Camera initialization
#camera.resolution = (640, 480)
#camera.start_preview()
#time.sleep(10)
#camera.capture('/home/pi/Desktop/foo.jpg')

### CAMERA VIDEO FEED ###
#my_stream = BytesIO()
#camera = picamera.PiCamera()
#camera.start_preview()
#time.sleep(5)
#path = '/home/pi/Desktop/foo'
#for i in range(60):
#    turn.ultra_turn(250+(i*5))
#    new_path = path + str(i) + '.jpeg'
#    camera.capture(new_path)
#    time.sleep(0.2)
#camera.capture('/home/pi/Desktop/my_stream.jpeg')
speech.run()


            


    




    