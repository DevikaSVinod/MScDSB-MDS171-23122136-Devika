# Write a Python program to implement a Stack class that has the following functions

#Push Item
#Pop Item
#Print the Items in the stack
#Size of Stack
#The top item in the stack
#Check if the stack is empty

class stack:

    def __init__(self) -> None:
        self.stack=[]

    def push(self,value):
        self.stack.append(value)
        print (self.stack)

    def pop(self,value):
        self.stack.pop(value)
        print (self.stack)

    def print(self):
        for items in self.stack:
            print(items)

    def len(self):
        print(len(self.stack))

    def topmost_item(self):
        print(self.stack[len(self.stack)-1])

    def checking_stack(self):
        if len(self.stack)==0:
            print('Stack is empty')
        else:
            print('Stack is not empty')

set_stack=stack()

set_stack.push('Pen')
set_stack.push('Pencil')
set_stack.push('Eraser')
set_stack.push('Paper')
set_stack.pop(2)
set_stack.print()
set_stack.len()
set_stack.topmost_item()
set_stack.checking_stack()


    



