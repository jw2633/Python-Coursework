#James Wang
#I210
#HW6

#6.20
#Takes a phonebook and return reverse phonebook while making phonenumber the key

phonebook = {
    "Smith, Jane":"123-45-67",
    "Doe, John": "987-65-43",
    "Baker, David": "567-89-01"
    }

def reverse(phonebook):
    returnDict = {}
    for key, value in phonebook.items():
        returnDict[value] = key
    return returnDict

print(reverse(phonebook))

#6.22
#Mirrors a string (except for strings with the letter 'e')
non_e = ['e']

def mirror(word):
    returnString = ""
    for i in range(len(word)):
        if word[len(word)-i-1] == 'b':
            returnString += 'd'
        elif word[len(word)-i-1] == 'd':
            returnString += 'b'
        elif word[len(word)-i-1] in non_e:
            return "INVALID"
        else:
            returnString += word[len(word)-i-1]
    return returnString

print(mirror('vow'))
print(mirror('wood'))
print(mirror('bed'))

#6.24
#Repeatedly asks user to enter first name of student in class.
#It then prints every name the number of students with that name when user enters empty string.

def names():
    new_Dict = {}
    while True:
        new_Name = input("Enter the next name:")
        if new_Name == '':
            break
        elif new_Name in new_Dict:
            new_Dict[new_Name] += 1
        else:
            new_Dict[new_Name] = 1
    for key, value in new_Dict.items():
        if value == 1:
            print("There is 1 student named", key)
        else:
            print("There are",str(value)," named ",key)

names()
            
#6.28
#Provides a rudimentary translation service.

def translate(phrase):
    trans_Dict = {
        "my":"mei",
        "fly": "fli"
    }
    returnString = ""
    phraseArray = phrase.split(" ")
    for word in phraseArray:
        if word in trans_Dict:
            returnString += trans_Dict[word] + " "
        else:
            returnString += "____"
    return returnString

print(translate(input("Enter a phrase to be translated:")))

#6.33
#Takes r of a roll of pair of dice and simulates repeated rolls until 100 rolls of r have been obtained
from random import randrange
def diceprob(r):
    total_rolls = 0
    count = 0

    while count < 100:
        roll = randrange(2, 13)
        total_rolls += 1
        if roll == r:
            count += 1
        print("It took {} rolls to get 100 rolls of {}".format(total_rolls, r))
    
