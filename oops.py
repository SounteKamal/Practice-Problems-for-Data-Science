'''
class Account:
    def __init__(self):
        self.balance = 100000
        self.atm_pin = 2025
        self.account_no = 2024921625362

    def debit(self,withdrawal_amount,pin):
        if self.balance > withdrawal_amount and pin == self.atm_pin:
            self.balance = self.balance - withdrawal_amount
        elif self.balance <= withdrawal_amount:
            print("Insufficient Balance in your account")
        elif pin!=self.atm_pin:
            print("Incorrect Pin")

    def credit(self,deposit_amount):
        print("Your account has credited the amount:",deposit_amount)
        self.balance +=deposit_amount

    def balance_inquiry(self,pin):
        if pin==self.atm_pin:
            print("Your Balance :",self.balance)
        else:
            print("pin is incorrect")

Acc = Account()
print("1. Withdraw Money")
print("2. Balance Inquiry")

print("Enter the  number of instructions which you want to perform")
num = int(input())
if num == 1 :
    Acc.debit( int(input("Enter the withdrawal amount\n")),int(input("Enter the pin\n")))
elif num == 2:
    Acc.balance_inquiry(int(input("Enter the pin\n")))
else:
    print("Invalid Instruction")
'''