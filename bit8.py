

#8 bit 
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
from time import sleep # Import the sleep function from the time module
 
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(11, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(12, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(13, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(15, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(16, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(18, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(22, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(29, GPIO.OUT, initial=GPIO.HIGH)
 
ditt = {1:11,2:12,3:13,4:15,5:16,6:18,7:22,8:29}
 
try:
    a = int(input("enter  : "))
    lst = [0,0,0,0,0,0,0,0]# Run forever
    b = 0
 
    while a!=0:
        lst[b] = a%2
        b = b+1
        a = a//2
 
    for i in range(1,9):
        if lst[i-1]==1:
            GPIO.output(ditt[i], GPIO.LOW)
 
 
except KeyboardInterrupt:
    GPIO.cleanup()