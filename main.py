# Imports all required tally functions
import tally_functions as tf
def main():
    tf.open_tally()
    activated = tf.is_activated()
    if activated:
        tf.open_firm("Uppa")
        tf.open_purchase()
        print("Purchase OPEN")
        name = "SUND"
        date = "20-9-2023"
        invoice_no = "SMUM1234"
        part = ["WPA",1, 1200, 10]
        data = [part, part]
        tf.put_head(name, date, invoice_no)
        tf.put_data(data)
        # tf.put_closing()

main()