from pitop.camera import Camera
from pitop.pma import UltrasonicSensor
from time import time, sleep
from further_link import send_image
from signal import pause
import RPi.GPIO as GPIO

# Initialize camera
camera = Camera()

# Initialize ultrasonic sensor
ultrasonic_sensor = UltrasonicSensor("D0", threshold_distance=0.3)

# Initialize GPIO for solenoid lock and button
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT)  # Solenoid lock
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)  # Button at port D3

# Variable to keep track of previous state of ultrasonic sensor
previous_state = False

# Function to engage the solenoid lock
def engage_lock():
    GPIO.output(18, GPIO.HIGH)
    sleep(1)
    GPIO.output(18, GPIO.LOW)

# Function to start recording video
def start_recording():
    video_path = '/home/pi/Documents/Final Project/video.avi'
    camera.start_video_capture(video_path)
    record_duration = 10  # seconds

    start_time = time()
    while time() - start_time < record_duration:
        # Continue recording or perform other tasks during the recording duration
        # Optionally, you can add some processing logic here
        sleep(0.1)

    camera.stop_video_capture()
    send_image(video_path)

# Callback function for ultrasonic sensor
def ultrasonic_callback(in_range):
    global previous_state

    if in_range and not previous_state:  # Object detected in range, engage lock
        engage_lock()
    elif not in_range and previous_state:  # Object detected out of range
        pass  # You can add any additional action here if needed
    previous_state = in_range

# Callback function for button press
def button_callback(channel):
    engage_lock()

# Set callback functions for ultrasonic sensor and button press
ultrasonic_sensor.when_in_range = start_recording
ultrasonic_sensor.when_out_of_range = ultrasonic_callback
GPIO.add_event_detect(3, GPIO.FALLING, callback=button_callback, bouncetime=300)

# Pause execution while we wait for events
pause()
