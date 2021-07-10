from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math

time.sleep(2)

distance = 50
mult = 3.14

#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
#win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
#X: 1366 Y:  665 RGB: (207, 207, 207)

win32api.SetCursorPos((1368,657))

while distance > 0 and keyboard.is_pressed('q') == False:
    pyautogui.drag(distance * mult, 0, duration=0.1)#right
    distance -= 2
    pyautogui.drag(0,distance* mult, duration=0.1)#down
    pyautogui.drag(-distance* mult, 0, duration=0.1)#left
    distance -= 2
    pyautogui.drag(0, -distance* mult, duration=0.1)#up
    
    
