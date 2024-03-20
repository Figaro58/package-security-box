from pitop.camera import Camera

from pitop.pma import UltrasonicSensor

from time import time, sleep

from further_link import send_image

from signal import pause

 

# Initialize camera

camera = Camera()

 

# Initialize ultrasonic sensor with the callback function using a lambda function

ultrasonic_sensor = UltrasonicSensor("D0", threshold_distance=0.3)

ultrasonic_sensor.when_in_range = lambda: start_recording()

 

# Define the recording function inline using a lambda function

start_recording = lambda: (

    camera.start_video_capture('/home/pi/Documents/Final Project/video.avi'),

    sleep(10),  # Record for 10 seconds

    camera.stop_video_capture(),

    send_image('/home/pi/Documents/Final Project/video.avi')

)

 

# Pause execution while we wait for events

pause()
