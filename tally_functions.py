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
    
"""
Opens the entered firm name
"""
def open_firm(name):
    pg.press("f1")
    time.sleep(1)
    pg.write(name)
    time.sleep(2)
    pg.press("down")
    time.sleep(2)
    pg.press("enter")
    time.sleep(1)

"""
Opens Purchase makes tally to recive data
"""
def open_purchase():
    pg.press("v")
    time.sleep(2)
    pg.press("f9")
    pg.press("enter")
    time.sleep(1)