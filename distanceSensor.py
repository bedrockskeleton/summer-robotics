from gpiozero import DistanceSensor
ultrasonic = DistanceSensor(echo=17, trigger=4, threshold_distance=0.5)

while True:
    print(ultrasonic.distance)