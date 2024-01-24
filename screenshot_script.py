import pyautogui
import time

time.sleep(3)
iml = pyautogui.screenshot(region=(550,125,650,575))
iml.save(r"C:\Users\balle\Desktop\Coding\python\python_screen_reader\pic.png")
