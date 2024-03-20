from pitop.camera import Camera

from pitop.pma import UltrasonicSensor

from time import time, sleep

from further_link import send_image

from signal import pause

import smtplib

from email.mime.multipart import MIMEMultipart

from email.mime.text import MIMEText

from email.mime.base import MIMEBase

from email import encoders

 

# Email configuration

sender_email = 'iguelmae@gmail.com'

sender_password = 'Cutoffmyfilter45$'

receiver_email = 'iguelmae@gmail.com'

 

def send_email(subject, message, file_path):

    msg = MIMEMultipart()

    msg['From'] = sender_email

    msg['To'] = receiver_email

    msg['Subject'] = subject

 

    msg.attach(MIMEText(message, 'plain'))

 

    with open(file_path, 'rb') as attachment:

        part = MIMEBase('application', 'octet-stream')

        part.set_payload(attachment.read())

 

    encoders.encode_base64(part)

    part.add_header('Content-Disposition', f'attachment; filename= {file_path}')

 

    msg.attach(part)

 

    server = smtplib.SMTP('smtp.gmail.com', 587)

    server.starttls()

    server.login(sender_email, sender_password)

    text = msg.as_string()

    server.sendmail(sender_email, receiver_email, text)

    server.quit()

 

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

 

    # Send the captured video using the send_image function

    send_email("Video Alert", "An object has been detected. Video attached.", video_path)

 

# Initialize camera

camera = Camera()

 

# Initialize ultrasonic sensor

ultrasonic_sensor = UltrasonicSensor("D0", threshold_distance=0.3)

ultrasonic_sensor.when_in_range = start_recording

 

# Pause execution while we wait for events

pause()
