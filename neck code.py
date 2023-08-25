from gpiozero import Servo
import time

# Initialize servo instances
vertical_servo = Servo(18)  # GPIO pin for vertical 
horizontal_servo = Servo(12)  # GPIO pin for horizontal 

try:
    while True:
        # Move neck up and down
        vertical_servo.value = -1  # Adjustable values
        time.sleep(1)
        vertical_servo.value = 1
        time.sleep(1)

        # Move neck left and right
        horizontal_servo.value = -1  # Adjustable values
        time.sleep(1)
        horizontal_servo.value = 1
        time.sleep(1)

finally:
    # Stop servos and cleanup
    vertical_servo.detach()
    horizontal_servo.detach()
