from pitop.pma import UltrasonicSensor
from signal import pause

ultrasonic_sensor = UltrasonicSensor("D3", threshold_distance=0.1)

ultrasonic_sensor.when_in_range = lambda: print('in range')
ultrasonic_sensor.when_out_of_range = lambda: print('out of range')

#Pause execution whie we wait for events
pause()

    
