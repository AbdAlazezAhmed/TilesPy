import numpy as np
from grabscreen import grab_screen
from directkeys import Up , Down , PressKey , ReleaseKey , Move1 , Move2
import time
from getkeys import key_check
import cv2

def main () :
    while(True) :
        #Resize the game window to about less than quarter of the screen at 1920*1080 resolution
        screen = cv2.cvtColor(grab_screen(region=(0,0,800,800)),cv2.COLOR_RGB2GRAY)
        keys = key_check()

        while screen[778,250] < 130 or screen[778,250] > 200 :
            if screen[765,250] < 130 or screen[765,250] > 200 :
                Move1(307,778)
            screen = cv2.cvtColor(grab_screen(region=(0,0,800,800)),cv2.COLOR_RGB2GRAY)
            print(screen[778 , 250] )
            keys = key_check()
##            time.sleep(0.1)
            if 'X' in keys:
                break
        Move2(0,0)
        
        while screen[778 , 360]<130 or screen[778 , 360]>200  :
            if screen[765 , 360]<130 or screen[765 , 360]>200  :
                Move1(420 , 778)
            screen = cv2.cvtColor(grab_screen(region=(0,0,800,800)),cv2.COLOR_RGB2GRAY)
            print(screen[778 , 360] )
##        time.sleep(0.1)
            keys = key_check()
            if 'X' in keys:
                break
        Move2(0,0)    
        while screen [778 , 480]<130 or screen [778 , 480]>200 :
            if screen [765 , 480]<130 or screen [765 , 480]>200 :
                Move1(525 , 778)
##            time.sleep(0.1)
            screen = cv2.cvtColor(grab_screen(region=(0,0,800,800)),cv2.COLOR_RGB2GRAY)
            print(screen[778 , 480] )
            keys = key_check()
            if 'X' in keys:
                break
        Move2(0,0)    
        while screen[778 , 590]<130 or screen[778 , 590]>200:
            if screen[765 , 590]<130 or screen[765 , 590]>200:
                Move1(620 , 778)
##            time.sleep(0.1)
            screen = cv2.cvtColor(grab_screen(region=(0,0,800,800)),cv2.COLOR_RGB2GRAY)
            print(screen[778 , 600] )
            keys = key_check()
            if 'X' in keys:
                break
        Move2(0,0)
            
        
        if 'X' in keys:
            break
main()
