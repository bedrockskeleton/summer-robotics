
speed = 75
reverse = 50

motors.start(-speed, speed)
while True:
    if ultrasonic.distance <= .1:
        motors.run_for_seconds(0.5, reverse, -reverse)
        motors.run_for_seconds(1, reverse, reverse)
    else:
        pass
