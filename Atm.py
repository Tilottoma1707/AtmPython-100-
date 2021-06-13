class Atm(object):
    def __init__(self,user,atmCardNum,pinNumber):
        self.user = user
        self.atmCardNum = atmCardNum
        self.pinNumber = pinNumber

    def cashWithDrawl(self):
        print("WithDrawing cash")

    def balanceEquiry(self):
        print("Balance Enquiry")

emma = Atm("Tom", "12345121212","123456#")
print(emma.cashWithDrawl())
print(emma.balanceEquiry())
