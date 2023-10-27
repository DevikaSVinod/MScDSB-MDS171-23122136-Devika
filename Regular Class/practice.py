class restuarant:

    def __init__(self,item_name,quantity) -> None:

        self.item = item_name
        self.qnty = quantity
        self.menuitems = {

            'RICE' :30,
            'WHEAT' :40,
            'DAL' :15,
            'TEA' :60

                }
#method to find  total cost of the itemm
    def totalcost(self):

        print('total cost of the order')
        print('item:\t' , self.item)
        print('quantity:\t',self.qnty)

        total = self.qnty * self.menuitems[self.item]
        print('total:\t',total)

order = restuarant('TEA',4)
order.totalcost()