#Program to understand classes and functions with deposit and withdraw functions

class Bank:
    acbal = 10000
    def validate(self, pin, c):
        if pin == 1234:
            return True
        else:
            print("Wrong pin")
	    c += 1
            if c <= 3:
		c += 1
                rp = int(input("re-enter your pin "))
                return obj.validate(rp, c)

    def deposit(self):
        amt = int(input("Amount to deposit "))
        if 100 <= amt and amt % 100 == 0 and amt <= 50000:
            self.acbal += amt
            print("Transaction successful")
        else:
            if amt % 100 != 0:
                print("Enter an amount as a multiple of 100")
            if amt > 50000:
                print("You cannot deposite more than 50000")

    def withdraw(self, k):
        wamt = int(input("Amount to withdraw: "))
        if k <= 3:
            if 100 <= wamt and wamt % 100 == 0 and wamt < self.acbal and self.acbal-wamt >= 500 and wamt <= 20000:
                self.acbal -= wamt
                print("Transaction successful")
                k += 1
            else:
                if wamt % 100 != 0:
                    print("Withdraw amount value as multiples of 100")
                if wamt >= self.acbal:
                    print("Your withdrawl is more than account balance")
                if self.acbal-wamt < 500:
                    print("Insufficient balance amt")
                if wamt > 20000:
                    print("Cannot withdraw more than 20k")
		return self.withdraw(self,k)
        else:
            print("Too many tries")

    def view_opt(self):
        print(" 1. Deposit \n 2. Withdraw \n 3. Bal Enquiry \n 0. Exit")
        opt = int(input("choose your option "))
        if opt == 1:
            obj.deposit()
        elif opt == 2:
            obj.withdraw(1)

obj = Bank()
print("Welcome to ABC bank")
pinn = int(input("enter your pin:"))
if obj.validate(pinn, 0):
        obj.view_opt()