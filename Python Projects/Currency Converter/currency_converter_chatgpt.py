import requests


def get_currency_input(prompt):
    while True:
        currency = input(prompt)
        if currency.strip():
            return currency.upper()


def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter the amount: "))
            if amount <= 0:
                print("The amount must be greater than 0")
            else:
                return amount
        except ValueError:
            print("The amount must be a numeric value!")


def fetch_conversion_rate(from_currency, to_currency, amount):
    url = f"https://api.apilayer.com/fixer/convert?to={
        to_currency}&from={from_currency}&amount={amount}"
    headers = {"apikey": "Gd3W8z4zWpt5kR09Ro9FKRKlj8mQFLkh"}
    response = requests.get(url, headers=headers)
    return response


def main():
    from_currency = get_currency_input("Enter an initial currency: ")
    to_currency = get_currency_input("Enter a target currency: ")
    amount = get_valid_amount()

    response = fetch_conversion_rate(from_currency, to_currency, amount)

    if response.status_code != 200:
        print("Sorry, there was a problem. Please try again later.")
    else:
        result = response.json()
        print(f"{amount} {from_currency} = {result['result']} {to_currency}")


if __name__ == "__main__":
    main()
