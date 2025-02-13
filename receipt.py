import csv
from datetime import datetime, timedelta
import random

def read_dictionary(filename, key_column_index):
    """Read the contents of a CSV file into a compound
    dictionary and return the dictionary.
    Parameters
        filename: the name of the CSV file to read.
        key_column_index: the index of the column
            to use as the keys in the dictionary.
    Return: a compound dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header row if it exists
            
            for row in reader:
                if len(row) < 3:
                    continue  # Skip incomplete rows
                key = row[key_column_index]
                dictionary[key] = [row[0], row[1], float(row[2])]
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        exit()
    
    return dictionary

def main():
    products_dict = read_dictionary('products.csv', 0)
    
    total_cost = 0
    total_items = 0
    sales_tax_rate = 0.06
    discount_product = "D083"  # Buy One, Get One 50% Off item
    
    print("Inkom Emporium")
    print("\nRequested Items:")
    
    try:
        with open('request.csv', mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.reader(csvfile)
            next(reader, None)  # Skip header row if it exists
            
            purchased_items = []
            
            for row in reader:
                if len(row) < 2:
                    continue  # Skip incomplete rows
                product_number, quantity = row[0], int(row[1])
                
                product_info = products_dict[product_number]  # This will raise KeyError if not found
                product_name = product_info[1]
                product_price = product_info[2]
                
                # Apply BOGO 50% off discount
                if product_number == discount_product:
                    full_price_count = quantity // 2 + quantity % 2
                    half_price_count = quantity // 2
                    item_total = (full_price_count * product_price) + (half_price_count * product_price * 0.5)
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each (BOGO 50% Off applied)")
                else:
                    item_total = product_price * quantity
                    print(f"{product_name}: {quantity} @ ${product_price:.2f} each")
                
                total_cost += item_total
                total_items += quantity
                purchased_items.append(product_name)
    except FileNotFoundError as e:
        print("Error: missing file")
        print(e)
        exit()
    except PermissionError as e:
        print("Error: permission denied")
        print(e)
        exit()
    except KeyError as e:
        print("Error: unknown product ID in the request.csv file")
        print(e)
        exit()
    except ValueError as e:
        print("Error: Invalid data format in request.csv.")
        print(e)
        exit()
    
    sales_tax = total_cost * sales_tax_rate
    total_due = total_cost + sales_tax
    
    print(f"\nNumber of Items: {total_items}")
    print(f"Subtotal: ${total_cost:.2f}")
    print(f"Sales Tax: ${sales_tax:.2f}")
    print(f"Total: ${total_due:.2f}")
    print("\nThank you for shopping at the Inkom Emporium.")
    
    # Print current date and time
    current_date_and_time = datetime.now()
    print(f"{current_date_and_time:%a %b %d %I:%M:%S %Y}")
    
    # Days until New Year's Sale
    new_year = datetime(current_date_and_time.year + 1, 1, 1)
    days_until_new_year = (new_year - current_date_and_time).days
    print(f"\nReminder: Only {days_until_new_year} days until our New Year's Sale!")
    
    # Return By Date (30 days from today at 9:00 PM)
    return_by = current_date_and_time + timedelta(days=30)
    return_by = return_by.replace(hour=21, minute=0, second=0)
    print(f"Return by: {return_by:%a %b %d %I:%M %p %Y}")
    
    # Random Coupon Offer
    if purchased_items:
        coupon_item = random.choice(purchased_items)
        print(f"\nExclusive Offer: Get 10% off your next purchase of {coupon_item}!")

if __name__ == "__main__":
    main()
