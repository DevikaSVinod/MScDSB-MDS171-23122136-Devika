# Define a class expense tracker that stores the
# expenses and income in a dicticonary
# implement the method to 
# - store the transactions:
# - view transactions:
# - calculate the total expense/income
# create a method in the class
# to export the details in the from of csv
# add export details to a file in the menu options

class expenseTracker:
    def __init__(self):
        self.expense = {
            "income":[],
            "expense":[]
        }
        print(self.expense)

    def store_transactions(self,type,amount,date):
        trans = {
            "type":type,
            "amount":amount,
            "date":date
        }
        if trans["type"]=="income":
            self.expense["income"].append(trans)

        else:
            self.expense["expense"].append(trans)

    def view_transactions(self):
        print(self.expense)

    def total(self):
        total_income = 0
        total_expense = 0
        for item in self.expense["income"]:
            total_income += item["amount"]
        for item in self.expense["expense"]:
            total_expense += item["amount"]
        print("total income: ","total expense: ", total_income,total_expense)

    def store_to_csv(self):
        file=open("expense tracker.csv","w+")
        for item in self.expense["income"]:
            file.write(str(item))
        for item in self.expense["expense"]:
            file.write(str(item))

    def collect_input(self):
        amount = int(input("Enter the amount:"))
        type = input("Enter the type: ")
        date = input("Enter the date: ")
        return amount,type,date

obj = expenseTracker()
obj.collect_input()
obj.store_transactions("income",5000,"10/10/2023")
obj.view_transactions()
obj.total()
obj.store_to_csv()




class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,value):
        self.stack.append(value)
        print(self.stack)
    
    def pop(self,value):
        self.stack.pop(value)
        print(self.stack)

    def display(self):
        for items in self.stack:
            print(items)

    def size(self):
        print(len(self.stack))

    def topmost(self):
        print(self.stack[len(self.stack0)])

    def check(self):
        if len(self.stack)==0:
            print("The stack is empty")
        else:
            print("The stack is not empty")






class stacking:
    def __init__(self):
        self.stack=[]

    def push(self,value):
        self.stack.apppend(value)
        print(stack.self)

    def pop(self.value):
    
    print(


class expenseTracker:
