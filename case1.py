"""def calculate_discount(purchase_amount, payment_method):
    if payment_method == 'cash':
        return purchase_amount * 0.1
    elif payment_method == 'card':
        return purchase_amount * 0.2
    else:
        return 0

def process_purchase():
    purchase_amount = float(input("Enter the purchase amount in taka: "))
    age = int(input("Enter the customer's age: "))
    gender = input("Enter the customer's gender (male/female): ")
    payment_method = input("Enter the payment method (cash/card): ")

    if purchase_amount < 1000 or age >= 50:
        print("Sorry, you are not eligible for the offer.")
        return

    discount = calculate_discount(purchase_amount, payment_method)

    if gender == 'male':
        free_item = 'cake'
    elif gender == 'female':
        free_item = 'chocolate'
    else:
        print("Invalid gender entered.")
        return

    payable_amount = purchase_amount - discount

    print("Congratulations!")
    print("You have qualified for a free", free_item)
    print("Your payable amount is:", payable_amount)

process_purchase()
"""
import tkinter as tk
from tkinter import messagebox

def calculate_discount(purchase_amount, payment_method):
    if payment_method == 'cash':
        return purchase_amount * 0.1
    elif payment_method == 'card':
        return purchase_amount * 0.2
    else:
        return 0

def process_purchase():
    purchase_amount = float(purchase_entry.get())
    age = int(age_entry.get())
    gender = gender_var.get()
    payment_method = payment_var.get()

    if purchase_amount < 1000 or age >= 50:
        messagebox.showinfo("Invalid", "Sorry, you are not eligible for the offer.")
        return

    discount = calculate_discount(purchase_amount, payment_method)

    if gender == 'Male':
        free_item = 'cake'
    elif gender == 'Female':
        free_item = 'chocolate'
    else:
        messagebox.showinfo("Invalid", "Invalid gender entered.")
        return

    payable_amount = purchase_amount - discount

    messagebox.showinfo("Congratulations", f"You have qualified for a free {free_item}. Your payable amount is: {payable_amount} taka.")

# Create the GUI window
window = tk.Tk()
window.title("Purchase Processing")
window.geometry("300x200")

# Create labels and entry fields
purchase_label = tk.Label(window, text="Purchase Amount (taka):")
purchase_label.pack()
purchase_entry = tk.Entry(window)
purchase_entry.pack()

age_label = tk.Label(window, text="Age:")
age_label.pack()
age_entry = tk.Entry(window)
age_entry.pack()

gender_label = tk.Label(window, text="Gender:")
gender_label.pack()
gender_var = tk.StringVar(window)
gender_var.set("Male")
gender_radiobutton1 = tk.Radiobutton(window, text="Male", variable=gender_var, value="Male")
gender_radiobutton1.pack()
gender_radiobutton2 = tk.Radiobutton(window, text="Female", variable=gender_var, value="Female")
gender_radiobutton2.pack()

payment_label = tk.Label(window, text="Payment Method:")
payment_label.pack()
payment_var = tk.StringVar(window)
payment_var.set("Cash")
payment_radiobutton1 = tk.Radiobutton(window, text="Cash", variable=payment_var, value="Cash")
payment_radiobutton1.pack()
payment_radiobutton2 = tk.Radiobutton(window, text="Card", variable=payment_var, value="Card")
payment_radiobutton2.pack()

process_button = tk.Button(window, text="Process", command=process_purchase)
process_button.pack()

# Start the GUI event loop
window.mainloop()
