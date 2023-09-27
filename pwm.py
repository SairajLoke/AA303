#pwm

import RPi.GPIO as GPIO
from time import sleep
 
ledpin1 = 11				# PWM pin connected to LED
ledpin2 = 12
ledpin3 = 13
GPIO.setwarnings(False)			#disable warnings
GPIO.setmode(GPIO.BOARD)		#set pin numbering system
GPIO.setup(ledpin1,GPIO.OUT)
GPIO.setup(ledpin2,GPIO.OUT)
GPIO.setup(ledpin3,GPIO.OUT)
 
pi_pwm1 = GPIO.PWM(ledpin1,1000)
pi_pwm1.start(100)#create PWM instance with frequency
#pi_pwm2 = GPIO.PWM(ledpin2,1000)
#pi_pwm2.start(100)
#pi_pwm3 = GPIO.PWM(ledpin3,1000)
#pi_pwm3.start(100)				#start PWM of required Duty Cycle 
try:
    while True:
        for duty in range(100,-1,-1):
            pi_pwm1.ChangeDutyCycle(duty) #provide duty cycle in the range 0-100
            sleep(0.01)
        sleep(0.5)
 
        for duty in range(0,101,1):
            pi_pwm1.ChangeDutyCycle(duty)
            sleep(0.01)
        sleep(0.5)
 
except KeyboardInterrupt:
    GPIO.cleanup()