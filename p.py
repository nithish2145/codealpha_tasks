stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 2750,
    "MSFT": 330,
    "AMZN": 130
}

portfolio = {}
total_investment = 0

print("Enter your stock portfolio (type 'done' to finish):")

while True:
    stock = input("Enter stock symbol: ").upper()
    if stock == "DONE":
        break
    if stock not in stock_prices:
        print("Stock not in database. Try again.")
        continue
    try:
        quantity = int(input(f"Enter quantity for {stock}: "))
        portfolio[stock] = quantity
    except ValueError:
        print("Invalid quantity. Please enter a number.")

print("\nYour Portfolio Summary:")

for stock, qty in portfolio.items():
    price = stock_prices[stock]
    value = price * qty
    total_investment += value
    print(f"{stock}: {qty} shares x ${price} = ${value}")

print(f"\nTotal Investment Value: ${total_investment}")

save = input("\nDo you want to save this to a file? (yes/no): ").lower()
if save == "yes":
    filename = input("Enter filename (with .txt or .csv): ")
    with open(filename, 'w') as f:
        f.write("Stock,Quantity,Price,Value\n")
        for stock, qty in portfolio.items():
            price = stock_prices[stock]
            value = price * qty
            f.write(f"{stock},{qty},{price},{value}\n")
        f.write(f"\nTotal Investment Value: ${total_investment}")
    print(f"Portfolio saved to {filename}")
