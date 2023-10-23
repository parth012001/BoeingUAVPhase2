from pymavlink import mavutil
import serial
import time

ser = serial.serial('dev/serial0', 115200, timeout = 1.0)

the_connection = mavutil.mavlink_connection('dev/serial0', 115200)

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

#https://www.ardusub.com/developers/pymavlink.html#send-rc-joystick
#https://www.ardusub.com/developers/pymavlink.html#send-manual-control

# Send a positive x value, negative y, negative z,
# positive rotation and no button.
# https://mavlink.io/en/messages/common.html#MANUAL_CONTROL
# Warning: Because of some legacy workaround, z will work between [0-1000]
# where 0 is full reverse, 500 is no output and 1000 is full throttle.
# x,y and r will be between [-1000 and 1000].
the_connection.mav.manual_control_send(
    the_connection.target_system,
    500,
    -500,
    250,
    500,
    0)

# To active button 0 (first button), 3 (fourth button) and 7 (eighth button)
# It's possible to check and configure this buttons in the Joystick menu of QGC
buttons = 1 + 1 << 3 + 1 << 7
the_connection.mav.manual_control_send(
    the_connection.target_system,
    0,
    0,
    500, # 500 means neutral throttle
    0,
    buttons)

#I need to get motors to work first
#Then map motors to a "remote control" channel. This is what they would do if we had a remote control
#Then those mapped buttons can be simulated with the above commands
#Then I need to get the right values for each motor speed and such

#This may be easier done by not using them as motors but instead as servos, which seem to let you have more control. 
#See https://mavlink.io/en/messages/common.html#MAV_CMD_DO_SET_SERVO
#This would take more work with software and getting exact pwm values for what I want, but is more similar to what I have done.
#Command syntax for that is:
the_connection.mav.command_long_encode(
        the_connection.target_system, 
        the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0,
        9, 1500, 0, 0, 0, 0, 0
    )

def MoveLeft():

def MoveRight():

def MoveUp():

def MoveDown():

def HoverInPlace():

def MoveForward():
