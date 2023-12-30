import tkinter as tk
from tkinter import ttk
import requests

def add_expense():
    amount = entry_amount.get()
    currency = combobox_currency.get()
    category = combobox_category.get()
    date = entry_date.get()
    payment_method = combobox_payment.get()

    expense_data.append([amount, currency, category, date, payment_method])

    # Clear entry fields after adding expense
    clear_entry_fields()

    update_table()

def clear_entry_fields():
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)

def convert_to_usd(amount, currency):
    if currency == 'USD':
        return float(amount)
    else:
        conversion_url = f"https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(conversion_url)
        if response.status_code == 200:
            exchange_rates = response.json()['rates']
            usd_amount = float(amount) / float(exchange_rates.get(currency, 1))  # Using .get() with default value
            return usd_amount
        else:
            return float(amount)

def update_table():
    clear_treeview()
    total_expense_usd = 0.0

    for expense in expense_data:
        amount, currency, category, date, payment_method = expense
        usd_amount = convert_to_usd(amount, currency)
        treeview.insert('', tk.END, values=[amount, currency, category, date, payment_method])
        total_expense_usd += usd_amount

    label_total.config(text=f"Total Expense (USD): ${round(total_expense_usd, 2)}")

def clear_treeview():
    for i in treeview.get_children():
        treeview.delete(i)

root = tk.Tk()
root.title("Expense Tracker")

expense_data = []

# Labels and Entry fields for expense details using grid layout
label_amount = tk.Label(root, text="Amount:")
label_amount.grid(row=0, column=0)
entry_amount = tk.Entry(root, width=23)
entry_amount.grid(row=0, column=1)

label_currency = tk.Label(root, text="Currency:")
label_currency.grid(row=1, column=0)
currency_options = ["USD", "EUR", "GBP", "JPY", "AED", "YER", "QAR", "PKR", "OMR", "NAD", "MOP", "LYD", "JOD", "IQD", "EGP"]  
combobox_currency = ttk.Combobox(root, values=currency_options)
combobox_currency.grid(row=1, column=1)

label_category = tk.Label(root, text="Category:")
label_category.grid(row=2, column=0)
category_options = ["Life Expenses", "Electricity", "Gas", "Rental", "Grocery", "Savings", "Education", "Charity"]
combobox_category = ttk.Combobox(root, values=category_options)
combobox_category.grid(row=2, column=1)

label_date = tk.Label(root, text="Date:")
label_date.grid(row=3, column=0)
entry_date = tk.Entry(root, width=23)
entry_date.grid(row=3, column=1)

label_payment = tk.Label(root, text="Payment Method:")
label_payment.grid(row=4, column=0)
payment_methods = ["Cash", "Credit Card", "Paypal"]
combobox_payment = ttk.Combobox(root, values=payment_methods)
combobox_payment.grid(row=4, column=1)

# Button to add an expense
button_add_expense = tk.Button(root, text="Add Expense", command=add_expense)
button_add_expense.grid(row=5, column=0, columnspan=2)

# Treeview for displaying expenses in a table
treeview = ttk.Treeview(root, columns=('Amount', 'Currency', 'Category', 'Date', 'Payment Method'))
treeview.grid(row=6, column=0, columnspan=2)

for column in ('Amount', 'Currency', 'Category', 'Date', 'Payment Method'):
    treeview.heading(column, text=column)

for column in ('Amount', 'Currency', 'Category', 'Date', 'Payment Method'):
    treeview.column(column, width=200, anchor='center')

label_total = tk.Label(root, text='Total Expense (USD): $0.00', background='yellow', font=('Helvetica', 15, 'bold'))
label_total.grid(row=7, column=0, columnspan=2)

root.mainloop()
