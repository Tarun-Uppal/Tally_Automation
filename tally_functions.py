import pyautogui as pg
import time

"""
Opens Tally and initializes it
"""
def open_tally():
    pg.press("win")
    time.sleep(1)
    pg.write("Tally")
    time.sleep(1)
    pg.press("enter")
    time.sleep(3)