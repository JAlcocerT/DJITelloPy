from djitellopy import tello
from time import sleep



# Connect to Tello
me = tello.Tello()
me.connect()
print(me.get_battery())


# Movements Test
# me.takeoff()
# sleep(2)
#
# me.send_rc_control(0,50,0,0) #go forward at 50
# sleep(2)
#
# me.send_rc_control(25,0,0,0)
# sleep(1)
#
# me.send_rc_control(0,0,0,30)
# sleep(1)
#
#
# me.send_rc_control(0,0,0,0) #stop completely
# me.land() #then land