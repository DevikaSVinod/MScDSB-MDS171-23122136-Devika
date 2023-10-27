# create a sportmart class where you will have inventory or shelf of items and order of customers
# create a csv file which will store your inventory details and order details
# with the help of file handling techniques in python read the files and create an object for trinity store and populate
# the inventory items and orders for the trinity store object
# to make sure that you have added all the items in your file use a display method to show your inventory and order history

class sportMart:
    def __init__(self):
        self.inventory = {}
        self.orders = {}

    def createOrder(self,Orderid,ItemName,Quantity,price,total):
        temp = {
            "orderid" : Orderid,
            "itemname" : ItemName,
            "quantity" : Quantity,
            "price" : price,
            "total" : total

        }
        self.orders[Orderid] = temp

    def createInventoryItem(self,Productid,ProductName,Quantity,Price):
        add = {
            "Productid" : Productid,
            "ProductName" : ProductName,
            "Quantity" : Quantity,
            "Price" : Price
        }            
        self.inventory[Productid] = temp

    def printOrders(self):
        print(self.orders)

    def printInventory(self):
        print(self.inventory)

# Create a menu driven program that will 
# Create new orders and update the inventory accordingly
# Export the final data to the file

trinity = sportMart()

# Menu Driven Part

while True:
    print("\nMenu Driven Program\n")
    print("1.Print Orders\n2.Print Inventory\n3.Export Data")
    choice=int(input("Enter your choice: "))
    if choice == 1:
        orders = open("Sportsshop.csv","+r")
        orders_header = orders.readline()
        orders_orders = orders.readlines()
        for item in orders_orders:
            temp = item.strip().split(',')
            trinity.createorder(temp[0],temp[1],temp[2],temp[3],temp[4])
        trinity.displayorder()

    elif choice == 2:
        inventory = open("Inventory.csv","+r")
        inventory_header = inventory.readline()
        inventory_orders = inventory.readlines()
        for item in inventory_orders:
            temp1 = item.strip().split(',')
            trinity.createorder(temp1[0],temp1[1],temp1[2],temp1[3],temp1[4])
        trinity.displayorder()

    elif choice == 3:
        pass
    else:
        print("Invalid Entry")
orders = open("Sportsshop.csv","r")
orders_header = orders.readline()
orders_orders = orders.readlines()
for item in orders_orders:
    temp = item.strip().split(",")
    trinity.createOrder (temp[0],temp[1],temp[2],temp[3],temp[4])
trinity.printOrders()








