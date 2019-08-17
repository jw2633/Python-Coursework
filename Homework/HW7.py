#James Wang
#I210
#HW7

#8.20
#Class BankAccount

class BankAccount(object):
    def __init__(self, amount):
        self.amount = float(amount)

    def withdraw(self, amount):
        self.amount -= float(amount)

    def deposit(self, amount):
        self.amount += float(amount)

    def balance(self):
        value = round(self.amount,3)
        return value

        
#8.22
#Class Worker

class Worker(object):
    def __init__(self, name, rate):
        self.name = name
        self.rate = rate

    def changeRate(self, adjust):
        self.rate = adjust

    def pay(self, hours):
        print("Not Implemented")

class HourlyWorker(Worker):
    def pay(self, hours):
        curr = hours - 40
        if curr > 0:
            hrpay = (self.rate * 2) * curr
            hrpay += (self.rate * hours)
        else:
            hrpay = (self.rate * hours)
        return hrpay

class SalariedWorker(Worker):
    def pay(self, hours = 40):
        hours = 40
        return self.rate * hours

#8.35
#Class Stack

class Stack(object):
    def __init__(self):
        self.lst = []
        
    def push(self, item):
        self.lst.append(item)

    def pop(self):
        popper = self.lst.pop()
        return popper
    

    def isEmpty(self):
        if len(self.lst) == 0:
            return True
        else:
            return False



#8.40
#Modified BankAccount class

class BankAccount2(object):
    def __init__(self, amount):
        try:
            if amount < 0:
                raise ValueError
            else:
                self.amount = float(amount)
        except ValueError:
            print("Illegal balance")

    def withdraw(self, amount):
        try:
            if self.amount - float(amount) < 0:
                raise ValueError
            else:
                self.amount -= float(amount)
        except ValueError:
            print("Overdraft")

    def deposit(self, amount):
        try:
            if amount < 0:
                raise ValueError
            else:
                self.amount += float(amount)
        except ValueError:
            x = print("Negative deposit")

    def balance(self):
        value = round(self.amount, 3)
        return value

        
