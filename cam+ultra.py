from pitop.camera import Camera
from pitop.pma import UltrasonicSensor
from time import time, sleep
from further_link import send_image
from signal import pause

def start_recording():
    # Start recording video in the background
    video_path = '/home/pi/Documents/Final Project/video.avi'
    camera.start_video_capture(video_path)
    
    # Set the recording duration to 15 seconds
    record_duration = 15  # seconds

    # Record for the specified duration
    start_time = time()
    while time() - start_time < record_duration:
        # Continue recording or perform other tasks during the recording duration
        # Optionally, you can add some processing logic here

        # Sleep for a short duration to avoid high CPU usage during the loop
        sleep(0.1)

    # Stop recording after 15 seconds
    camera.stop_video_capture()

    # Send the captured video using the send_image function
    send_image(video_path)

# Initialize camera
camera = Camera()

# Initialize ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor("D3", threshold_distance=0.1)
ultrasonic_sensor.when_out_of_range = start_recording

# Pause execution while we wait for events
pause()
