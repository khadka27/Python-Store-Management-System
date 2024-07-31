
import datetime
from Read import readfile
from DateTime import getDate, getTime
laptop_stock = readfile()


def Sell_bill(customer_name, location, contact_number, shipping_cost, price, quantity,choice):
    now = datetime.datetime.now()
    filename = f"{now.strftime('%Y-%m-%d_%H-%M-%S')}__{customer_name}.txt"
    f = open(filename, 'w')
    f.write('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+----+---+-+--+\n')
    f.write('                                           Laptop Center Store \n')
    f.write('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    f.write(
        f'                                                         Date: {getDate()}   Time: {getTime()}\n\n')
    f.write(f'                                                                                                        ')
    f.write(f'                                                                                                        ')
    f.write(f'                Purchase By : {customer_name}\n')
    f.write(f'                Address     : {location}\n')
    f.write(f'                Contact     : {contact_number}\n\n')
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    # Write order summary to file
    f.write("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    f.write("| Laptop          | Brand          | Price per unit (USD) | Quantity       | Total price (USD) |\n")
    f.write("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    f.write(
        f"| {(laptop_stock[choice][0]):<8}|| {laptop_stock[choice][1]:<17}||{laptop_stock[choice][2]:<18}||{quantity:<14}| |${price + shipping_cost}|\n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(
        f"                                               Shipping cost     :\t${shipping_cost}                       \n")
    f.write(
        f"                                               Total             :\t${price + shipping_cost}                       \n")
    f.write(f" +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n")
    f.write(f"                                    Thankyou for Buying                                                \n")
    f.write(f' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    f.close()
    
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
def add_bill(Vender_name,Vender_location,contact_number,choice,quantity,amount,vat,total_price):
    now = datetime.datetime.now()
    filename = f"{now.strftime('%Y-%m-%d_%H-%M-%S')}__{Vender_name}.txt"
    f = open(filename, 'w')
    f.write('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+----+---+-+--+\n')
    f.write('                                           Laptop Center Store \n')
    f.write('  +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    f.write(
        f'                                                         Date: {getDate()}   Time: {getTime()}\n\n')
    f.write(f'                                                                                                        ')
    f.write(f'                                                                                                        ')
    f.write(f'                Purchase By : {Vender_name}\n')
    f.write(f'                Address     : {Vender_location}\n')
    f.write(f'                Contact     : {contact_number}\n\n')
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    # Write order summary to file
    f.write("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    f.write("| Laptop          | Brand          | Price per unit (USD) | Quantity       | Total price (USD) |\n")
    f.write("+-----------------+----------------+----------------------+----------------+-------------------+\n")
    f.write(
        f"| {(laptop_stock[choice][0]):<8}|| {laptop_stock[choice][1]:<17}||{laptop_stock[choice][2]:<18}||{quantity:<14}| |${amount}|\n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(f"                                                                                                      \n")
    f.write(
        f"                                               VAT Amount        :\t${vat}                       \n")
    f.write(
        f"                                               Total             :\t${total_price}                       \n")
    f.write(f" +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n")
    f.write(f"                                    Thankyou for Buying                                                \n")
    f.write(f' +-+--+--+---+----+--+--+--+--+--+--+--+--+--+--+--+--+--++-+--+--+---+----+--+-+--+--+- --+--+--+--+\n\n')
    f.close()