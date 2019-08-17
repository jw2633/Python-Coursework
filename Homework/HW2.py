# James Wang
# I210
# Homework 2

#3.19

a, b, c = 3, 4, 5
#(a)

if a < b:
    print('OK')

#(b)

if not c < b:
    print('NOT OK')

#(c)

if not (a + b) == c:
    print('NOT OK')

#(d)

if ((a**2) + (b**2)) == (c**2):
    print('OK')


#3.24
my_program = eval(input("Enter list of words: "))
for char in my_program:
    if 'secret' in my_program:
        my_program.remove('secret')

    print(char)

#3.30
first_num = eval(input("Enter first number: "))
second_num = eval(input("Enter second number: "))
third_num = eval(input("Enter third number: "))
last_num = eval(input("Enter last number: "))

average = ((first_num + second_num + third_num)/(3))

if average == last_num:
    print('Equal')

#3.34
def pay(num1, num2):
    payday = num1 * num2
    if num2 > 40:
        payday = ((num1 * 40) + (num1 * (num2 - 40) * (1.5)))
    print(payday)
    


    


