
import tally_functions as tf

FailSafeException=True
def main():
    tf.open_tally()

pg.press("f1")
time.sleep(1)
pg.write("uppal")
time.sleep(2)
pg.press("down")
time.sleep(2)
pg.press("enter")
time.sleep(1)
pg.press("v")
time.sleep(2)
pg.press("f9")
pg.press("enter")
time.sleep(1)

pg.press("f2")
pg.write("21-8-2023")
pg.press("enter")
pg.write("SMUM1234")
pg.press("enter")
pg.press("enter")
pg.write("Sund")
pg.press("down")
for i in range(17):
    pg.press("enter")
pg.write("WPA")
pg.press("down")
pg.press("down")
pg.press("enter")
pg.write("100")
for i in range(7):
    pg.press("enter")
print("done")
time.sleep(2)
pg.write("cgs")
pg.press("down")
for i in range(3):
    pg.press("enter")

pg.write("sgs")
pg.press("down")
for i in range(30):
    pg.press("enter")
    
main()