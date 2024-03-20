from gpiozero import MotionSensor

from time import sleep

 

# Initialize motion sensor using GPIO 4

pir = MotionSensor(4)

pir.wait_for_motion()
print ("Motion detected!")
