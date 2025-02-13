import datetime

def main():
    # Get the current day of the week
    today = datetime.datetime.now().strftime('%A')
    
    # Initialize subtotal
    subtotal = 0.0

    # Loop to get price and quantity until the user enters 0 for price
    while True:
        try:
            price = float(input("Enter the price of an item (or 0 to finish): "))
            if price == 0:
                break
            quantity = int(input("Enter the quantity: "))
            subtotal += price * quantity
        except ValueError:
            print("Invalid input. Please enter numeric values.")

    print(f"\nSubtotal: ${subtotal:.2f}")
    discount = 0.0

    # Check for discount
    if subtotal >= 50 and (today == "Tuesday" or today == "Wednesday"):
        discount = subtotal * 0.10
        print(f"Discount applied: ${discount:.2f}")
    elif today == "Tuesday" or today == "Wednesday":
        additional_needed = 50 - subtotal
        print(f"Spend an additional ${additional_needed:.2f} to receive a discount.")

    # total after discount
    subtotal -= discount
    sales_tax = subtotal * 0.06
    total = subtotal + sales_tax

    # Print sales tax and total
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total Amount Due: ${total:.2f}")

if __name__ == "__main__":
    main()
