from djitellopy import tello
import cv2



# Connect to Tello
me = tello.Tello()
me.connect()
print(me.get_battery())


#VIDEO:

me.streamon()

while True:
    img = me.get_frame_read().frame #individual image that comes from the drone
    img = cv2.resize(img,(360,240)) #smaller format, faster processing (default 1280x720)
    cv2.imshow("Image",img) #to create a window and display the result
    cv2.waitKey(1) #1ms delay