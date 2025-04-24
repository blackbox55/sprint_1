class Wallet:

# first thing to run when making a new class
# Outline required user-provided input values
    def __init__(self, initial_amount = 0):
        # save user provided initial amount as an atribute.
        # self refers to whatever object im working with
        # params with default values assigned are optional
        self.balance = initial_amount
    
    #spend cash Method
    def spend_cash(self, amount):
        if self.balance < amount:
            return 'not enough money'
        else:
            self.balance = self.balance - amount
            return f'remaining balance of {self.balance}'

    def add_cash(self, amount):
        self.balance = self.balance + amount
        return f'new balance of {self.balance}'

        #__repr__ method 
        # changes how the object looks when printed out
        #the presence of the self keyword allows me to access
        #or modify attributes within this function
    def __repr__(self):
        return f'Wallet with balance of: ${self.balance}'
            


if __name__ == '__main__':
    wallet1 = Wallet(50)
    print(wallet1.balance)
 



