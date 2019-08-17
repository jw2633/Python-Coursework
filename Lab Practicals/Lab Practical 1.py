import random
import donation

lst = []
for i in range(200):
     lst.append(random.randrange(20) + 1)


# main

# Section 1 - get all of the donations and output the values

(print("The donation amounts: "))

print(total_donations)


# As an example of how to get an amount, this gets 1 donation and prints it out
# Run the program a few times and notice that the amount changes.
# If the code won't run, did you put this file and donation.py in the same directory?
#amount = donation.get_donation()
#print("One donation was received, in the amount of:", amount)

(print("The donations in order: "))
total_donations.sort()
print(total_donations)

# Section 2 - Compute basic categories


def small_donation(total_donations):
    total = 0 
    for i in total_donations:
        if i < 5:
            total +=1 
    return total
        
def medium_donation(total_donations):
    total = 0
    for i in total_donations:
        if (i > 6) and (i <=15):
            total += 1
            return total

def large_donation(total_donations):
    total = 0 
    for i in total_donations:
        if (i > 16):
            total += 1 
    return total
        
   
            
            


print("There were ", small_donations(total_donations), "small donations ($5 or less).")
print("There were ", medium_donations(total_donations), "medium donations ($6 - $15).")
print("There were ", large_donations(total_donations) , "large donations ($16 or more).")


# Section 3 - Compute success or failure

def total_money(total_donations):
    add = 0
    for i in total_donations:
        add +=  i
    return add
        
    

def goal(total_donations):
    if total_money(total_donations) > 2017:
        print("The total amount of money raised is: ", total_donations)
        print("The fundraising goal was met!")
    else:
        print("The fundraising goal was not met.")





# Section 4 - What can you expect from the bank?



def cash_it_out(total_donations):
    print("Hundreds: ", total_donations//100)
    total_donations = total_donations % 100
    print("Twenties: ", total_donations //20)
    total_donations = total_donations % 20
    print("Fives: ", total_donations //5)
    total_donations = total_donations % 5
    print("Ones: ", total_donations //1)
    total_donations = total_donations % 1

print("The bank cashed this amount out as:")
print("-----------------------------------")
print(cash_it_out(total_donations))


