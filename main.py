from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(3)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)

# Used the screenshot_script.py to get my regions: (550,125,650,575) 
# used https://imagecolorpicker.com/en to get rgb values of (74,74,86)

while keyboard.is_pressed('q') == False: 
    iml = pyautogui.screenshot(region=(550,125,650,575))
    width, height = iml.size
    for x in range(0,width,115):
        for y in range(0,height,115):
            r,g,b = iml.getpixel((x,y))
            if b == 86:
                click(x+550,y+125)
                time.sleep(0.05)
                break
            
