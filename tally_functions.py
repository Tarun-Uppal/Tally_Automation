import pyautogui as pg
import time

def is_activated():
    if pg.locateOnScreen('images/is_activated.png') == None:
        return None
    else:
        return True

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
        while pg.locateOnScreen('images/purchase.png') == None:
            pg.press("enter")
        pg.press("backspace")
    else:
        return

""" 
Puts in the invoice no, date, Party name and Purchase Ledger 
"""
def put_head(name, date, invoice_no):
    pg.press("f2")
    pg.write(date)
    pg.press("enter")
    pg.write(invoice_no)
    while (pg.locateOnScreen('images/party_name.png') == None):
        pg.press("enter")
    pg.write(name)
    pg.press("down")
    pg.press("enter")    
    while(pg.locateOnScreen('images/purchase.png') == None):
        pg.press("enter")
    pg.write("GST TAX")
    pg.press("down")
    pg.press("enter")
    while(pg.locateOnScreen('images/purchase.png') == None):
        pg.press("enter")
    
        
def put_data(data):
    for data1 in data:
        print(str(data1))
        part = str(data1[0])
        quantity = str(data1[1])
        price = str(data1[2])
        disc = str(data1[3])
        pg.write(part)
        pg.press("down")
        pg.press("enter")
        while(pg.locateOnScreen('images/purchase.png') == None):
            pg.press("enter")
        pg.write(quantity)
        pg.press("enter")
        while(pg.locateOnScreen('images/purchase.png') == None):
            pg.press("enter")
        pg.write(price)
        pg.press("enter")
        pg.press("enter")
        pg.write(disc)
        while(pg.locateOnScreen('images/new_product.png') == None):
            pg.press("enter")
        
    # Error before this 
    while(pg.locateOnScreen('images/end_of_list.png') == None):
        pg.press("enter")
        print("WOSSSSSSS")
    # time.sleep(2)
    pg.press("backspace")
    
    
def put_closing():
    pg.write("cgs")
    pg.press("down")
    while(pg.locateOnScreen('images/new_product.png') == None):
        pg.press("enter")
    pg.write("sgs")
    while(pg.locateOnScreen('images/new_product.png') == None):
        pg.press("enter")
    pg.write("round")
    while(pg.locateOnScreen('images/end_of_bill.png') == None):
        pg.press("enter")