class studdetails:

    def _init_(self):
        self.cls = {
            'Students' : []
        }

    def collectinfo(self,roll,name,subject,mark):
        self.info = {
            roll : {
                'Name' : name,
                'Subject' : subject,
                'Mark' : mark
            }
        }

        self.cls['Students'].append(self.info)
        print(self.cls)

    def view(self):
        print(self.cls)

object = studdetails()
print("1.Student")
print("2.Office")
while True:
        choice_1 = input("Enter your choice:")
        if choice_1 == "1":
            while True:
                print("1.view")
                choice_2 = input("enter your choice:")
                if choice_2 == "1":
                    object.view()
                else :
                    break

        elif choice_1 == "2":
           print('1.collectinfo')
           while True:
            choice_3 = input("Enter your choice:")
            if choice_3 == "1":
                n = int(input("Enter the numbers to be entered:"))
                for i in range(n):
                    name = input("enter the name:")
                    subject = input("enter the name of the subject:")
                    mark = int(input("enter the mark:"))   
                    object.collectinfo()          
            else: 
                break
        else:
            break
        

            