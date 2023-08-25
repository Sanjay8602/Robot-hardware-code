from gpiozero import Servo, Motor
import time

# Initialize servo and motor instances for the left hand
left_shoulder_horizontal_servo = Servo(17)   # GPIO pin for horizontal shoulder
left_shoulder_vertical_servo = Servo(13)     # GPIO pin for vertical shoulder 
left_elbow_motor = Motor(forward=27, backward=24)  # GPIO pins for elbow BO motor
left_wrist_servo = Servo(16)                 # GPIO pin for wrist servo motor
left_thumb_servo = Servo(20)                 # GPIO pin for thumb servo motor

def move_to_angle(servo, angle, min_pulse=-1, max_pulse=1):
    # Convert angle to servo value range
    angle_range = max_pulse - min_pulse
    servo_value = (angle - min_pulse) / angle_range
    servo.value = servo_value

try:
    # Left hand movements
    move_to_angle(left_shoulder_horizontal_servo, 90, -1, 1)  # Adjust angles and servo range
    move_to_angle(left_shoulder_vertical_servo, 45, -1, 1)
    time.sleep(1)
    move_to_angle(left_shoulder_horizontal_servo, -90, -1, 1)
    move_to_angle(left_shoulder_vertical_servo, -45, -1, 1)
    time.sleep(1)
    move_to_angle(left_shoulder_horizontal_servo, 0, -1, 1)
    move_to_angle(left_shoulder_vertical_servo, 0, -1, 1)

    # Left hand elbow movement (BO motor)
    left_elbow_motor.forward()  # Adjustable
    time.sleep(1)
    left_elbow_motor.backward()
    time.sleep(1)
    left_elbow_motor.stop()

    # Left hand wrist rotation
    move_to_angle(left_wrist_servo, 180)  # Adjustable
    time.sleep(1)
    move_to_angle(left_wrist_servo, 0)
    time.sleep(1)

    # Left hand thumb movement
    move_to_angle(left_thumb_servo, 45, -1, 1)  # Adjustable
    time.sleep(1)
    move_to_angle(left_thumb_servo, -45, -1, 1)
    time.sleep(1)
    move_to_angle(left_thumb_servo, 0, -1, 1)

finally:
    # Detach servos and stop motor
    left_shoulder_horizontal_servo.detach()
    left_shoulder_vertical_servo.detach()
    left_wrist_servo.detach()
    left_thumb_servo.detach()
    left_elbow_motor.stop()
