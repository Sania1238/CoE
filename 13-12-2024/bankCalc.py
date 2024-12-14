import streamlit as st
class Bank:
    acbal = 10000
    def validate(self, pin, c):
            if pin == 1234:
                return True
            else:
                st.error("Wrong pin")
                c += 1
                if c <= 2:
                    rp = st.number_input("re-enter your pin ", key="re-enter_pin_input_1")
                    return obj.validate(rp, c)

    def deposit(self):
        amt = st.number_input("Amount to deposit ", key="deposit_amount")
        if 100 <= amt and amt % 100 == 0 and amt <= 50000:
            self.acbal += amt
            st.success("Transaction successful")
        else:
            if amt % 100 != 0:
                st.error("Enter an amount as a multiple of 100")
            if amt > 50000:
                st.error("You cannot deposit more than 50000")

    def withdraw(self, k):
        wamt = st.number_input("Amount to withdraw: ", key="withdraw_amount")
        if k <= 2:
            if 100 <= wamt and wamt % 100 == 0 and wamt < self.acbal and self.acbal-wamt >= 500 and wamt <= 20000:
                self.acbal -= wamt
                st.success("Transaction successful")
            else:
                k += 1
                if wamt % 100 != 0:
                    st.error("Withdraw amount value as multiples of 100")
                if wamt >= self.acbal:
                    st.error("Your withdrawl is more than account balance")
                if self.acbal-wamt < 500:
                    st.error("Insufficient balance amt")
                if wamt > 20000:
                    st.error("Cannot withdraw more than 20k")
                return self.withdraw(k)
        else:
            st.error("Too many tries")

    def view_opt(self):
        st.success(" 1. Deposit \n 2. Withdraw \n 3. Bal Enquiry \n 0. Exit")
        opt = st.number_input("choose your option ", key="view_options")
        if opt == 1:
            obj.deposit()
        elif opt == 2:
            obj.withdraw(1)


st.title("Bank Transaction")
obj = Bank()
st.text("Welcome to ABC bank")
pinn = st.number_input("enter your pin:", key="pin_input")
if obj.validate(pinn, 0):
    obj.view_opt()