import csv

def stock_tracker():
    # Hardcoded dictionary of stock prices
    stock_prices = {
        'AAPL': 150.0,
        'GOOGL': 2800.0,
        'AMZN': 3400.0,
        'MSFT': 300.0,
        'TSLA': 700.0
    }
    
    print("Welcome to the Simple Stock Tracker!")
    print("Available stocks and their prices:")
    for stock, price in stock_prices.items():
        print(f"{stock}: ${price}")
    
    total_investment = 0.0
    investments = []
    
    while True:
        stock_name = input("\nEnter stock name (or type 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        
        if stock_name not in stock_prices:
            print("Stock not found. Please enter a valid stock symbol.")
            continue
        
        try:
            quantity = float(input(f"Enter quantity for {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative.")
                continue
        except ValueError:
            print("Please enter a valid number for quantity.")
            continue
        
        investment = stock_prices[stock_name] * quantity
        total_investment += investment
        investments.append((stock_name, quantity, investment))
        print(f"Added {quantity} shares of {stock_name} worth ${investment:.2f}")
    
    print(f"\nTotal investment: ${total_investment:.2f}")
    
    save = input("Do you want to save the result to a file? (yes/no): ").lower()
    if save == 'yes':
        file_type = input("Enter file type ('txt' or 'csv'): ").lower()
        if file_type == 'txt':
            with open('investment.txt', 'w') as file:
                file.write("Stock Tracker Report\n")
                file.write("====================\n")
                for stock, qty, invest in investments:
                    file.write(f"{stock}: {qty} shares worth ${invest:.2f}\n")
                file.write(f"\nTotal investment: ${total_investment:.2f}\n")
            print("Investment report saved as 'investment.txt'")
        
        elif file_type == 'csv':
            with open('investment.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Stock', 'Quantity', 'Investment'])
                for stock, qty, invest in investments:
                    writer.writerow([stock, qty, f"{invest:.2f}"])
                writer.writerow([])
                writer.writerow(['Total Investment', '', f"{total_investment:.2f}"])
            print("Investment report saved as 'investment.csv'")
        
        else:
            print("Invalid file type. No file saved.")
    else:
        print("Result not saved.")

if __name__ == "__main__":
    stock_tracker()
