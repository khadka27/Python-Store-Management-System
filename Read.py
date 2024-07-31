
def read():

    file = open("Laptop_Center.txt", "r")
    lines = file.readlines()
    laptop = []
    for line in lines:
        line = line.rstrip('\n')
        line = line.split(", ")
        laptop.append(line)
    file.close()
    return laptop



def displayLaptop():
    Laptop_list = []
    column = ['SN', 'Name', ' Brand', ' Price',' Quantity', ' Processor', ' Graphic card']
    Laptop_list.append(column)

    file = open('Laptop_Center.txt', 'r')
    sn = 1
    for line in file.readlines():
        Laptop_list.append([str(sn), *line.rstrip().split(',')])
        sn += 1
        print()
    file.close()

    return Laptop_list


def readfile():
    file=open('Laptop_Center.txt', 'r')
    laptop_stock = [line.rstrip().split(',')for line in file]
    for product in laptop_stock:
            product[2] = product[2]
    file.close()
    return laptop_stock


# if __name__ == "__main__":
#     displayLaptop()


