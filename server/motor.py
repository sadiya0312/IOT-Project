#!/usr/bin/python3
# File name   : motor.py
# Description : Control Motors 
# Website     : www.adeept.com
# E-mail      : support@adeept.com
# Author      : William
# Date        : 2018/10/12

import RPi.GPIO as GPIO
import time
# motor_EN_A: Pin7  |  motor_EN_B: Pin11
# motor_A:  Pin8,Pin10    |  motor_B: Pin13,Pin12

Motor_B_EN    = 11


Motor_B_Pin1  = 13
Motor_B_Pin2  = 12

Dir_forward   = 0
Dir_backward  = 1

pwm_B = 0

def setup():#Motor initialization
    global pwm_B
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(Motor_B_EN, GPIO.OUT)
    GPIO.setup(Motor_B_Pin1, GPIO.OUT)
    GPIO.setup(Motor_B_Pin2, GPIO.OUT)
    try:
        pwm_B = GPIO.PWM(Motor_B_EN, 1000)
    except:
        pass

def motorStop():#Motor stops
    GPIO.output(Motor_B_Pin1, GPIO.LOW)
    GPIO.output(Motor_B_Pin2, GPIO.LOW)
    GPIO.output(Motor_B_EN, GPIO.LOW)

def motor_right(status, direction, speed):#Motor 2 positive and negative rotation
    global  pwm_B
    if status == 0: # stop
        motorStop()
    else:
        if direction == Dir_forward:
            GPIO.output(Motor_B_Pin1, GPIO.HIGH)
            GPIO.output(Motor_B_Pin2, GPIO.LOW)
            pwm_B.start(100)
            pwm_B.ChangeDutyCycle(speed)
        elif direction == Dir_backward:
            GPIO.output(Motor_B_Pin1, GPIO.LOW)
            GPIO.output(Motor_B_Pin2, GPIO.HIGH)
            pwm_B.start(0)
            pwm_B.ChangeDutyCycle(speed)



def destroy():
    motorStop()
    GPIO.cleanup()             # Release resource


try:
    pass
except KeyboardInterrupt:
    destroy()


