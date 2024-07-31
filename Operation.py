# Read the laptop stock file and create a table
import datetime
import Write
from DateTime import getDate, getTime
from Read import readfile


laptop_stock = readfile()


# Define a function to get the index of a product in the table


def get_product_index(name):

    for i, product in enumerate(laptop_stock):
        if product[0] == name:
            return i
    return None


def Sell_Product():
    # Display the list of products
    print('Select a laptop from the list below:')
    print("Option\t\t\tName\t\t\t\tQuantity")
    for i, product in enumerate(laptop_stock):
        print('-'*90+'|')
        print(f"{i}\t\t\t{product[0]}\t\t\t{product[3]}")


    # Get the user's choice
    while True:
        try:
            choice = int(
                input("Enter the option of the product you want to sell: "))
            if choice < 0 or choice >= len(laptop_stock):
                print("Invalid choice.")
            else:
                break
        except:
            print("Invalid choice. Please enter a number.")

    # Get the quantity of the product to sell
    while True:
        try:
            quantity = int(
                input(f"Enter the quantity of {laptop_stock[choice][0]} you want to sell: "))
            if quantity < 1 or quantity > int(laptop_stock[choice][3]):
                print("Invalid quantity.")
            else:
                # Update the quantity of the sold product in the laptop_stock table
                # laptop_stock = get_product_index(laptop_stock[choice][0])
                laptop_stock[choice][3] = str(
                    int(laptop_stock[choice][3]) - quantity)

                # Write the updated stock to the file
                f = open('Laptop_Center.txt', 'w')
                for product in laptop_stock:
                    f.write(','.join(product) + '\n')
                f.close()

                break  # Exit the loop if the input is valid
        except:
            print("Invalid quantity. Please enter a number.")

    # Calculate the total price
    try:
        price = float(laptop_stock[choice][2].replace('$', '')) * quantity
    except:
        print("Invalid price.")
        return

    # Ask if the customer wants shipping
    shipping_cost = 0
    shipping_choice = input("Do you want shipping? (y/n): ")
    while shipping_choice.lower() not in ["y", "n"]:
        shipping_choice = input(
            "Invalid input. Please enter 'y' or 'n' only: ")
    if shipping_choice.lower() == "y":
        shipping_cost = 70.0
    elif shipping_choice.lower() == "n":
        print("You should come to pick your product in Distributor office -- pokhara ")
    else:
        print("Invalid input. Please enter 'y' or 'n' only.")

    print(
        f"Sold {quantity} {laptop_stock[choice][0]} for ${price:.2f}. Shipping cost: ${shipping_cost:.2f}.")

    print('''
                                    
                            ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ █▀▀ ─▀─ █▀▀▄ █▀▀▀ 　 █▀▀ █▀▀█ █▀▀█ █───█ █▀▀█ █▀▀█ █▀▀▄ 
                            ░█▄▄█ █▄▄▀ █──█ █── █▀▀ ▀▀█ ▀▀█ ▀█▀ █──█ █─▀█ 　 █▀▀ █──█ █▄▄▀ █▄█▄█ █▄▄█ █▄▄▀ █──█ 
                            ░█─── ▀─▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▀── ▀▀▀▀ ▀─▀▀ ─▀─▀─ ▀──▀ ▀─▀▀ ▀▀▀─
            \n''')
    while True:
        customer_name = input('Please type your name: ')
        if customer_name.isalpha():
            break
        else:
            print("Invalid input. Please enter alphabetic characters only.")

    while True:
        location = input('Please type your address: ')
        if location.isalpha():
            break
        else:
            print("Invalid input. Please enter alphabetic characters only.")
    while True:
        contact_number = input('Please type your mobile number: ')
        if contact_number.isdigit():
            break
        else:
            print("Invalid input. Please enter only digits.")
    Write.Sell_bill(customer_name, location, contact_number,
                    shipping_cost, price, quantity, choice)

#print the bill in console 
    print(' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+----+---+-+--+\n')
    print('                                           Laptop Center Store \n')
    print(' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    print(
        f'                                                         Date: {getDate()}   Time: {getTime()}\n\n')
    print('                                                                                                        ')
    print('                                                                                                        ')
    print(f'                Purchase By : {customer_name}\n')
    print(f'                Address     : {location}\n')
    print(f'                Contact     : {contact_number}\n\n')
    print("                                                                                                      \n")
    print("                                                                                                      \n")
    print("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    print("| Laptop          | Brand          | Price per unit (USD) | Quantity       | Total price (USD) |\n")
    print("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    print(
        f"| {(laptop_stock[choice][0]):<12}|| {laptop_stock[choice][1]:<19}||{laptop_stock[choice][2]:<20}||{quantity:<19}| |${price + shipping_cost}|\n")
    print("                                                                                                      \n")
    print("                                                                                                      \n")
    print("                                                                                                      \n")
    print("                                                                                                      \n")
    print(
        f"                                               Shipping cost     :\t${shipping_cost}                       \n")
    print(
        f"                                               Total             :\t${price + shipping_cost}                       \n")
    print(" +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n")
    print("                                    Thankyou  for Buying                                                \n")
    print(' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')

    print(
        f"Sold {quantity} {laptop_stock[choice][0]} for ${price}. Shipping cost: ${shipping_cost}.")
    print("""
                                            ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   ░ ░ ░
                                            ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   ▄ ▄ ▄
                                            
                                            █░█ █ █▀ █ ▀█▀   ▄▀█ █▀▀ ▄▀█ █ █▄░█   █ █ █
                                            ▀▄▀ █ ▄█ █ ░█░   █▀█ █▄█ █▀█ █ █░▀█   ▄ ▄ ▄
                                                                                    
        """)

# /////////////////////////////////////////////////////////Add Stock/////////////////////////////////////////////////////////////////////////////////////


# ===================================================================

def get_product_index(name):

    for i, product in enumerate(laptop_stock):
        if product[0] == name:
            return i
    return None


#

def addLaptop():
    # Define the variable at the beginning of the function
    total_price = 0
    vat_rate = 0.13  # 13% VAT rate
    # Display the list of products
    print('Select a laptop from the list below:')
    print("Option\t\t\tName\t\t\t\tQuantity")
    i=1
    for i, product in enumerate(laptop_stock):
        print('-'*90+'|')
        print(f"{i}\t\t\t{product[0]}\t\t\t{product[3]}")
    i=+1

    # Get the user's choice
    while True:
        try:
            choice = int(
                input("Enter the option of the product you want to Add : "))
            if choice < 0 or choice >= len(laptop_stock):
                print("Invalid choice.")
            else:
                break
        except:
            print("Invalid choice. Please enter a number.")

    # Get the quantity of the product to sell
    while True:
        try:
            quantity = int(
                input(f"Enter the quantity of {laptop_stock[choice][0]} you want to Add : "))
            if quantity < 0:
                print("Invalid quantity.")
            else:
                laptop_stock[choice][3] = str(
                    int(laptop_stock[choice][3]) + quantity)

                # Write the updated stock to the file
                f = open('Laptop_Center.txt', 'w')
                for product in laptop_stock:
                    f.write(','.join(product) + '\n')
                f.close()

                break  # Exit the loop if the input is valid
        except:
            print("Invalid quantity. Please enter a number.")

    # Calculate the total price
    try:
        price = float(laptop_stock[choice][2].replace('$', '')) * quantity
    except:
        print("Invalid price.")
        return
    amount = int(price) * quantity
    vat = amount * vat_rate
    total_price += amount + vat
    print(
        f"Added {quantity} to {laptop_stock[choice][0]}. New quantity: {laptop_stock[choice][3]}. Total price with VAT: ${total_price:.2f}")

    print('''
                                    
                            ░█▀▀█ █▀▀█ █▀▀█ █▀▀ █▀▀ █▀▀ █▀▀ ─▀─ █▀▀▄ █▀▀▀ 　 █▀▀ █▀▀█ █▀▀█ █───█ █▀▀█ █▀▀█ █▀▀▄ 
                            ░█▄▄█ █▄▄▀ █──█ █── █▀▀ ▀▀█ ▀▀█ ▀█▀ █──█ █─▀█ 　 █▀▀ █──█ █▄▄▀ █▄█▄█ █▄▄█ █▄▄▀ █──█ 
                            ░█─── ▀─▀▀ ▀▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀▀▀ ▀──▀ ▀▀▀▀ 　 ▀── ▀▀▀▀ ▀─▀▀ ─▀─▀─ ▀──▀ ▀─▀▀ ▀▀▀─
            \n''')
    while True:
        Vender_name = input('Please type your name: ')
        if Vender_name.isalpha():
            break
        else:
            print("Invalid input. Please enter alphabetic characters only.")

    while True:
        Vender_location = input('Please type your address: ')
        if Vender_location.isalpha():
            break
        else:
            print("Invalid input. Please enter alphabetic characters only.")
    while True:
        contact_number = input('Please type your mobile number: ')
        if contact_number.isdigit():
            break
        else:
            print("Invalid input. Please enter only digits.")

    Write.add_bill(Vender_name, Vender_location, contact_number,
                   choice, quantity, amount, vat, total_price)
    # Get the current date and time

    print('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+----+---+-+--+\n')
    print('                                           Laptop Center Store \n')
    print('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    print(
        f'                                                         Date: {getDate()}   Time: {getTime()}\n\n')
    print(f'                                                                                                        ')
    print(f'                                                                                                        ')
    print(f'                Purchase By : {Vender_name}\n')
    print(f'                Address     : {Vender_location}\n')
    print(f'                Contact     : {contact_number}\n\n')
    print(f"                                                                                                      \n")
    print(f"                                                                                                      \n")
    # print order summary to file
    print("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    print("| Laptop          | Brand          | Price per unit (USD) | Quantity       | Total price (USD) |\n")
    print("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    print(
        f"| {(laptop_stock[choice][0]):<11}| {laptop_stock[choice][1]:<19}|{laptop_stock[choice][2]:<20}|{quantity:<19}|${amount}|\n")
    print(f"                                                                                                      \n")
    print(f"                                                                                                      \n")
    print(f"                                                                                                      \n")
    print(f"                                                                                                      \n")
    print(
        f"                                                                VAT Amount        :\t${vat}                       \n")
    print(
        f"                                                                Total             :\t${total_price}                       \n")
    print(f" +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n")
    print(f"                                    Thankyou for Buying                                                \n")
    print(f' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    print(
        f"Sold {quantity} {laptop_stock[choice][0]} for ${price}. VAT Amount: ${total_price}.")
    print("""
                                            ▀█▀ █░█ ▄▀█ █▄░█ █▄▀   █▄█ █▀█ █░█   ░ ░ ░
                                            ░█░ █▀█ █▀█ █░▀█ █░█   ░█░ █▄█ █▄█   ▄ ▄ ▄
                                            
                                            █░█ █ █▀ █ ▀█▀   ▄▀█ █▀▀ ▄▀█ █ █▄░█   █ █ █
                                            ▀▄▀ █ ▄█ █ ░█░   █▀█ █▄█ █▀█ █ █░▀█   ▄ ▄ ▄
                                                                                    
        """)
