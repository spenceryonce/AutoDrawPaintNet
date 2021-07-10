from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math

x = 1368
y = 657
R = 36

time.sleep(2)
win32api.SetCursorPos((x,y))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)

for i in range(360):
    # setting pace with a modulus 
    if i%3==0:
       pyautogui.moveTo(x+R*math.cos(math.radians(i)),y+R*math.sin(math.radians(i)))

win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
