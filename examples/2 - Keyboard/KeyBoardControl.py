import KeyPressModule as KP

from djitellopy import tello
from time import sleep

import threading #for the battery status in paralel


KP.init()

# Connect to Tello
me = tello.Tello()
me.connect()
print(me.get_battery())


# A function to periodically check and print the battery status every 5s
def print_battery_status(interval=5):
    last_battery_check_time = time()
    while True:
        current_time = time()
        if current_time - last_battery_check_time >= interval:
            battery = me.get_battery()
            print(f"Battery Status: {battery}%")
            last_battery_check_time = current_time
        sleep(1)


#Check if the key is pressed and act upon it
def getKeyboardInput():
    lr, fb, ud, yv = 0, 0 ,0, 0, #leftright #forwardbackwards #updown #yaw
    speed = 30

    if KP.getKey("LEFT"): lr = - speed
    elif KP.getKey("RIGHT"): lr = speed

    if KP.getKey("UP"): fb = - speed
    elif KP.getKey("DOWN"): fb = speed

    if KP.getKey("w"): ud = - speed
    elif KP.getKey("s"): ud = speed

    if KP.getKey("a"): yv = -speed
    elif KP.getKey("d"): yv = speed

    if KP.getKey("q"): me.land()
    if KP.getKey("e"): me.takeoff()

    return[lr, fb, ud, yv]

# The code:

# Start a separate thread to print the battery status
battery_thread = threading.Thread(target=print_battery_status)
battery_thread.daemon = True
battery_thread.start()

while True:
    vals = getKeyboardInput()
    me.send_rc_control(vals[0], vals[1], vals[2], vals[3])
    sleep(0.05)


    #me.send_rc_control(0,0,0,0)
    #print(KP.getKey("s"))