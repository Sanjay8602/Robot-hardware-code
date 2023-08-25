from gpiozero import Servo, Motor
import time

# Initialize servo and motor instances
shoulder_horizontal_servo = Servo(18)  # GPIO pin for horizontal shoulder
shoulder_vertical_servo = Servo(12)    # GPIO pin for vertical shoulder 
elbow_motor = Motor(forward=22, backward=23)  # GPIO pins for elbow BO motor
wrist_servo = Servo(19)                # GPIO pin for wrist servo motor
thumb_servo = Servo(26)                # GPIO pin for thumb servo motor

def move_to_angle(servo, angle, min_pulse=-1, max_pulse=1):
    # Convert angle to servo value range
    angle_range = max_pulse - min_pulse
    servo_value = (angle - min_pulse) / angle_range
    servo.value = servo_value

try:
    # Shoulder movements
    move_to_angle(shoulder_horizontal_servo, 90, -1, 1)  # Adjust angles and servo range
    move_to_angle(shoulder_vertical_servo, 45, -1, 1)
    time.sleep(1)
    move_to_angle(shoulder_horizontal_servo, -90, -1, 1)
    move_to_angle(shoulder_vertical_servo, -45, -1, 1)
    time.sleep(1)
    move_to_angle(shoulder_horizontal_servo, 0, -1, 1)
    move_to_angle(shoulder_vertical_servo, 0, -1, 1)

    # Elbow movement (BO motor)
    elbow_motor.forward()  # Adjustable
    time.sleep(1)
    elbow_motor.backward()
    time.sleep(1)
    elbow_motor.stop()

    # Wrist rotation
    move_to_angle(wrist_servo, 180)  # Adjustable
    time.sleep(1)
    move_to_angle(wrist_servo, 0)
    time.sleep(1)

    # Thumb movement
    move_to_angle(thumb_servo, 45, -1, 1)  # Adjustable
    time.sleep(1)
    move_to_angle(thumb_servo, -45, -1, 1)
    time.sleep(1)
    move_to_angle(thumb_servo, 0, -1, 1)

finally:
    # Detach servos and stop motor
    shoulder_horizontal_servo.detach()
    shoulder_vertical_servo.detach()
    wrist_servo.detach()
    thumb_servo.detach()
    elbow_motor.stop()
