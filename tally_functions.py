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
    while pg.locateOnScreen('images/first_open.png') == None:
        time.sleep(0.1)
    
"""
Opens the entered firm name
"""
def open_firm(name):
    pg.press("f1")
    time.sleep(0.5)
    pg.write(name)
    time.sleep(0.5)
    pg.press("down")
    pg.press("enter")
    time.sleep(1)
    while pg.locateOnScreen('images/open_check.png') == None:
        time.sleep(0.2)

"""
Opens Purchase makes tally to recive data
"""
def open_purchase():
    if pg.locateOnScreen('images\purchase.png') == None:
        pg.press("v")
        time.sleep(2)
        pg.press("f9")
        pg.press("enter")
        while pg.locateOnScreen('images/purchase.png') != None:
            time.sleep(0.1)
    
def put_head(name, date, invoice_no):
    pg.press("f2")
    pg.write(date)
    pg.press("enter")
    pg.write(invoice_no)
    pg.press("enter")
    pg.press("enter")
    pg.write(name)
    pg.press("down")
    for i in range(17):
        pg.press("enter")
        
def put_data(data):
    for data1 in data:
        part = str(data1[0])
        quantity = str(data1[1])
        price = str(data1[2])
        disc = str(data1[3])
        pg.write(part)
        pg.press("down")
        pg.press("down")
        pg.press("enter")
        pg.write(price)
        pg.press("enter")
        pg.write(disc)
        pg.press("enter")
    for i in range(6):
        pg.press("enter")
        print("done")
    time.sleep(2)
    
def put_closing():
    pg.write("cgs")
    pg.press("down")
    for i in range(3):
        pg.press("enter")
    pg.write("sgs")
    pg.press("down")
    for i in range(30):
        pg.press("enter")