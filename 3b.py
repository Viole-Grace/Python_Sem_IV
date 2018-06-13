class bank:
    def __init__(self):
        print('Enter A/c no, Balance, Rate of Interest, Overdraft Limit, Overdraft Fee Rate ')
        self.acno,self.bal,self.rate,self.olim,self.ofee=[int(x) for x in raw_input().split()]
        self.overdraft=0
    def withdraw(self,amt):
        if amt + self.overdraft < self.olim and self.bal - amt>0:
            self.overdraft += amt
            self.bal -= amt
        elif self.bal - amt>0:
            self.overdraft += amt + amt * self.ofee/100
            self.bal -= amt
    def deposit(self,amt):
        self.bal += amt
    def interest(self,time):
        self.bal += self.bal * self.rate * time / 100
    def display(self):
        print('A/C number ',self.acno,'\nBalance ',self.bal)
obj=bank()
while True:
    ch = int(input('Enter Choice 1 to Withdraw, 2 to Deposit, 3 to Add Interest, 4 to Display Balance, 5 to exit\t'))
    if ch==1:
        obj.withdraw(int(input('Enter Amount ')))
    elif ch==2:
        obj.deposit(int(input('Enter Amount ')))
    elif ch==3:
        obj.interest(int(input('Enter Time in years ')))
    elif ch==4:
        obj.display()
    else:
        break