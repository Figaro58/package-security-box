from pitop.camera import Camera

from gpiozero import MotionSensor

from time import time, sleep

from signal import pause

 

def start_recording():

    # Start recording video in the background

    video_path = '/home/pi/Documents/Final Project/video.avi'

    camera.start_video_capture(video_path)

   

    # Set the recording duration to 10 seconds

    record_duration = 10  # seconds

 

    # Record for the specified duration

    start_time = time()

    while time() - start_time < record_duration:

        # Continue recording or perform other tasks during the recording duration

        # Optionally, you can add some processing logic here

 

        # Sleep for a short duration to avoid high CPU usage during the loop

        sleep(0.1)

 

    # Stop recording after 10 seconds

    camera.stop_video_capture()

 

# Initialize camera

camera = Camera()

 

# Initialize motion sensor using GPIO 4

pir = MotionSensor(4)

pir.when_motion = start_recording

 

# Pause execution while we wait for events

pause()
