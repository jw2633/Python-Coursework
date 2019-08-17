#James Wang
#I210
#HW5

#5.29
# Returns a list of all first names (in a list) and all last names (in a list)

def lastfirst(lst):
    lastNames = []
    firstNames = []
    for x in lst:
        indx = int(x.index(','))
        lastNames.append(x[indx + 2: ])
        firstNames.append(x[0:indx])
    print([lastNames, firstNames])

#5.39
# takes string and returns it with its modification
# (every vowel is replaced by four consecutive copies of itself
# and an exclamation mark added at the end.)

def exclamation(string):
    newString = ""
    vowels = ['a', 'e', 'i', 'o', 'u']
    for letter in string:
        if letter in vowels:
            newString += (letter * 4)
        else:
            newString += letter
    newString += "!"
    return newString

print(exclamation('argh'))
print(exclamation('hello'))

#5.43
# takes 2-dimensional list of integers and returns True
# if each row of the table sums up to an even number and False otherwise.

def evenrow(two_d_ints):
    for row in two_d_ints:
        sums_up = 0
        for elem in row:
            sums_up += elem
        if not sums_up % 2 == 0:
            return False
    else:
        return True

print(evenrow([[1, 3], [2, 4], [0, 6]]))
print(evenrow([[1, 3, 2], [3, 4, 7], [0, 6, 2]]))
print(evenrow([[1, 3, 2], [3, 4, 7], [0, 5, 2]]))
