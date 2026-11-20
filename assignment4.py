class sbi_bank():

    def __init__(self,y,x):
        self.name=y
        self.balance=x
    
    
    def view_balance(self):
        print(self.balance)

    def deposit(self,x):
        print("deposit successful")
        self.balance=self.balance+x

    def withdrowal(self,x):
        if x > self.balance:
            print("insufficient balance")

        else:    
            print("withdrowal successful")
            self.balance=self.balance-x       

s1=sbi_bank("alwin",500)            

  