# create a class restaurant, that accepts
# itemname and quantity as input
# inside your class you are having the item
# and its cost(unit price) as a dictionary
# create a function  calculate totalcost
# that prints the itemname, quantity and totalcost.

class restuarant:

    def __init__(self , item_name , qty) -> None:
        self.item = item_name
        self.quant = qty
        self.menuitems = {
            'RICE' : 30 ,
            'CHICKEN' : 120 ,
            'DAL' : 60 ,
            'CHAPATHI' : 10
        }

    def totalcost(self):
        print('Total cost of the order: ')
        print('Item: \t' , self.item)
        print('Quantity: \t' , self.quant)
        
        total = self.quant * self.menuitems[self.item]
        print('Total: \t' , total)

order = restuarant('RICE' , 4)
order.totalcost()