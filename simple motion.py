from gpiozero import MotionSensor

from time import sleep

 

# Initialize motion sensor using GPIO 4

pir = MotionSensor(4)

 

# Continuously check for motion and print message

while True:

    if pir.motion_detected:

        print("Continuous Motion detected!")

        break  # Exit the loop once motion is detected

    sleep(0.5)  # Check for motion every 0.5 seconds

 

# Wait for motion and print message

pir.wait_for_motion()

print("Waited Motion detected!")
