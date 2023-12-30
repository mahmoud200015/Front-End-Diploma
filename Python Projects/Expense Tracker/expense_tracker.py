import tkinter as tk
from tkinter import ttk
import requests
import math

def add_expense():
    amount = entry_amount.get()
    currency = combobox_currency.get()
    category = combobox_category.get()
    date = entry_date.get()
    payment_method = combobox_payment.get()

    expense_data.append([amount, currency, category, date, payment_method])

    # Clear entry fields after adding expense
    entry_amount.delete(0, tk.END)
    entry_date.delete(0, tk.END)

    update_table()

def convert_to_usd(amount, currency):
    if currency == 'USD':
        return float(amount)
    else:
        conversion_url = f"https://api.exchangerate-api.com/v4/latest/USD"
        response = requests.get(conversion_url)
        if response.status_code == 200:
            exchange_rates = response.json()['rates']
            usd_amount = float(amount) / float(exchange_rates[currency])
            return usd_amount
        else:
            return float(amount)  # Return original amount if currency conversion fails

def update_table():
    # Clear the existing table content
    for i in treeview.get_children():
        treeview.delete(i)

    total_expense_usd = 0.0  # Initialize total expense in USD

    # Update the table with stored expense data and convert amounts to USD
    for expense in expense_data:
        amount, currency, category, date, payment_method = expense
        usd_amount = convert_to_usd(amount, currency)
        treeview.insert('', tk.END, values=[amount, currency, category, date, payment_method])
        total_expense_usd += usd_amount

    label_total.config(text=f"Total Expense (USD): ${round(total_expense_usd, 2)}")

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

# treeview.heading('#0', text='ID')
treeview.heading('Amount', text='Amount')
treeview.heading('Currency', text='Currency')
treeview.heading('Category', text='Category')
treeview.heading('Date', text='Date')
treeview.heading('Payment Method', text='Payment Method')

treeview.grid(row=6, column=0, columnspan=2)


# Configure styles for the rows of expenses of user and heading of Treeview
style = ttk.Style()
style.configure("Treeview", font=('Arial', 10, 'bold'), background='silver', fieldbackground='silver',foreground='black', relief='groove')
style.configure("Treeview.Heading", font=('Arial', 10, 'bold'), background='lightgreen',foreground='black', relief='flat')

# Center text in all columns
treeview.column('#0', width=0)
treeview.column('Amount', width=100, anchor='center')
treeview.column('Currency', width=100, anchor='center')
treeview.column('Category', width=200, anchor='center')
treeview.column('Date', width=200, anchor='center')
treeview.column('Payment Method', width=200, anchor='center')

# Label to display total expense in USD
label_total = tk.Label(root, text='Total Expense (USD): $0.00', background= 'yellow', font=('Helvetica', 15, 'bold'))
label_total.grid(row=7, column=0, columnspan=2)

root.mainloop()
