from pymavlink import mavutil
import time

the_connection = mavutil.mavlink_connection('/dev/ttyTHS1', 115200)

the_connection.wait_heartbeat()
print("Heartbeat from system (system %u component %u)" % (the_connection.target_system, the_connection.target_component))

#first arm, requires arming checks to pass. Use mission planner to set up arm/disarm checks.
the_connection.mav.command_long_send(the_connection.target.system, the_connection.target_component, 
                                    mavutil.mavlink.MAV_CMD_COMPONENT_ARM_DISARM, 0, 1, 0, 0, 0, 0, 0, 0)

#tells you if the drone got the previous message.
print(the_connection.recv_match(type='COMMAND_ACK', blocking= True))

#Takeoff. Move to 10m. Use current lat and long.
the_connection.mav.command_long_send(the_connection.target.system, the_connection.target_component, 
                                    mavutil.mavlink.MAV_CMD_NAV_TAKEOFF 0, 0, 0, 0, 0, 0, 0, 10)

#tells you if the drone got the previous message.
print(the_connection.recv_match(type='COMMAND_ACK', blocking= True))