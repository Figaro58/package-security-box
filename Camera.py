from pitop.camera import Camera
from time import time, sleep
from further_link import send_image


camera = Camera()

#Start recording video in the background
video_path = '/home/pi/Documents/Final Project/video.avi' 
camera.start_video_capture(video_path)

#Set the recording duration to 15 seconds
record_duration = 15 # seconds

# record for the specified duration
start_time = time()
while time() - start_time < record_duration:
    #the loop ensures that the recording continues until the spcified duration is reached
    sleep(0.1)

#Stop recording after 15 seconds
camera.stop_video_capture()

#Send the caputured video using the send_image function
send_image(video_path)

    
