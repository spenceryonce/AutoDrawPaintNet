from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con
import math

#Top Left Corner of Paint.NET
#X:  901 Y:  279 RGB: (237, 218, 255)
tx = 901
ty = 279
x = 1300
y = 657
R = 36
distance = 50
mult = 3.14
offsetx = 0
offsety = 0

#colors
rx = 1824
ry = 338

bx = 1763
by = 273

gx = 1825
gy = 210

px = 1884
py = 268

def changeColor(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    time.sleep(0.005)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)

def drawInterior():
    global distance,mult
    while distance > 0 and keyboard.is_pressed('q') == False:
        pyautogui.drag(distance * mult, 0, duration=0.01)#right
        distance -= 2
        pyautogui.drag(0,distance* mult, duration=0.05)#down
        pyautogui.drag(-distance* mult, 0, duration=0.01)#left
        distance -= 2
        pyautogui.drag(0, -distance* mult, duration=0.01)#up


def loop():
    global distance,offsetx,offsety
    while offsetx < (156 * 4):
        if not distance > 0:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
            offsetx += 156
            win32api.SetCursorPos((tx+offsetx,ty+offsety))
            distance = 50
            drawInterior()
    offsetx = 0
    offsety = 156
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)
    win32api.SetCursorPos((tx,ty+offsety))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    print(ty-offsety)
    drawInterior()
    loop()
    
    
time.sleep(2)
changeColor(rx,ry)
win32api.SetCursorPos((tx,ty))
win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, tx, ty, 0, 0)

drawInterior()
loop()



    
