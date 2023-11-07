#This code calibrates the ESC for servo 9. This requires the parameter for servo9_function to be set to 0.
#The code then sets the speed of the motor to 1/2 and then stops.
#Timings are significantly longer than required due to this code not being used in the final design.
#Contact Brett for questions.

from pymavlink import mavutil
import time

the_connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))
the_connection.mav.send(the_connection.mav.command_long_encode(
        the_connection.target_system, 
        the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
       1900, 0, 0, 0, 0, 0
    ))


time.sleep(7)
print("Hi 1")
the_connection.mav.send(the_connection.mav.command_long_encode(
        the_connection.target_system, 
        the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
       1100, 0, 0, 0, 0, 0
    ))


time.sleep(15)
print("Hi 2")
the_connection.mav.send(the_connection.mav.command_long_encode(
        the_connection.target_system, 
        the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
       1500, 0, 0, 0, 0, 0
    ))


time.sleep(2)
print("Hi 3")
the_connection.mav.send(the_connection.mav.command_long_encode(
        the_connection.target_system, 
        the_connection.target_component, 
        mavutil.mavlink.MAV_CMD_DO_SET_SERVO, 0, 9,
       1100, 0, 0, 0, 0, 0
    ))
print("Done")
