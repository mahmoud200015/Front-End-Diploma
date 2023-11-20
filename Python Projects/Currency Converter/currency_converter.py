import requests

from_currency = input("Enter an intial currency: ")
to_currency = input("Enter a target currency: ")

while True:
  try:
    amount = float(input("Enter the amount: "))
  except:
    print("The amount must be a numeric value!")
    continue

  if amount <= 0:
    print("The amount must be greater than 0")
    # continue
  else:
    break

url = ("https://api.apilayer.com/fixer/" + 
      f"convert?to={to_currency}&from={from_currency}&amount={amount}")

payload = {}
headers = {
    "apikey": "Gd3W8z4zWpt5kR09Ro9FKRKlj8mQFLkh"
}

response = requests.request("GET", url, headers=headers, data=payload)

status_code = response.status_code
if status_code != 200:
  print("Sorry, there was a problem. Please try again later.")

result = response.json()
print(f"{amount} {from_currency} = {result["result"]} {to_currency}")
