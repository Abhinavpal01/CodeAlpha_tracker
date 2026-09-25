import time

def show_menu():
    print("\n==================================")
    print("   STOCK PORTFOLIO TRACKER ")
    print("==================================")
    print("1. Add Stock")
    print("2. Remove Stock")
    print("3. View Portfolio Summary")
    print("4. Exit")
    print("----------------------------------")

def main():
    # Hardcoded dummy prices for stocks (Dict: Stock Symbol -> Price in USD/INR)
    stock_prices = {
        "AAPL": 180.50,
        "TSLA": 240.00,
        "GOOGL": 140.25,
        "AMZN": 175.00,
        "RELIANCE": 2900.00,
        "TCS": 3800.00,
        "INFY": 1500.00
    }

    # User's current portfolio holding: {Stock_Symbol: Quantity}
    portfolio = {}

    while True:
        show_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            print("\n--- Available Demo Stocks & Prices ---")
            for symbol, price in stock_prices.items():
                print(f" - {symbol}: ${price}")

            symbol = input("\nEnter Stock Symbol to Buy/Add: ").strip().upper()
            
            if symbol in stock_prices:
                try:
                    qty = int(input(f"Enter quantity for {symbol}: "))
                    if qty > 0:
                        portfolio[symbol] = portfolio.get(symbol, 0) + qty
                        print(f" Added {qty} shares of {symbol} to your portfolio!")
                    else:
                        print(" Quantity must be greater than 0.")
                except ValueError:
                    print("Invalid input! Please enter a valid number for quantity.")
            else:
                print(" Stock symbol not found in dummy price list.")

        elif choice == "2":
            symbol = input("\nEnter Stock Symbol to Remove: ").strip().upper()
            if symbol in portfolio:
                del portfolio[symbol]
                print(f" Removed {symbol} from your portfolio.")
            else:
                print(" You do not own this stock.")

        elif choice == "3":
            print("\n==================================")
            print("     YOUR PORTFOLIO SUMMARY")
            print("==================================")
            if not portfolio:
                print("Your portfolio is currently empty.")
            else:
                total_portfolio_value = 0
                print(f"{'STOCK':<10} | {'QTY':<8} | {'PRICE':<10} | {'TOTAL VALUE':<12}")
                print("-" * 50)

                for symbol, qty in portfolio.items():
                    price = stock_prices[symbol]
                    item_total = price * qty
                    total_portfolio_value += item_total
                    print(f"{symbol:<10} | {qty:<8} | ${price:<9.2f} | ${item_total:<11.2f}")

                print("-" * 50)
                print(f" TOTAL PORTFOLIO VALUE: ${total_portfolio_value:.2f}")

        elif choice == "4":
            print("\nExiting Stock Portfolio Tracker. Happy Investing! ")
            break
        else:
            print(" Invalid choice! Please select between 1 and 4.")

        time.sleep(1)

if __name__ == "__main__":
    main()