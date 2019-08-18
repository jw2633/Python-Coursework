#James Wang
#I211
#Indiv. HW1
#Team 13

#1
#Takes string as input. It reverses the order of all characters and prints it
#back to the user. For example: AbC123 would be printed out as 321CbA

def reverseString(String):
    outputString = []
    for char in range(0, len(String)):
        outputString.append(str(String[len(String) - char - 1]))
    print("".join(outputString))

reverseString(input("Please enter a string."))

#2
#Program that calculates how many vowels are in a word. For example: "queen" should display 3

count = 0
vowels = ["A","E","I","O","U"]

word = input("Please enter a word: ")
word = word.upper()

for char in word:
    if char in vowels:
        count += 1

print("There are ",count," vowels.")





    
