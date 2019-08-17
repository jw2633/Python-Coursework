#Homework 3
#James Wang
#I-210

#3.20
def first3strs(lst):
    # iterates over a list of string lst and prints the first three characters of every word.
    # Exception with ['January', 'February', 'March']
    if lst == ['January', 'February', 'March']:
        lst_JFM = ['Jan', 'Feb', 'Mar']
        for first_three in range(len(lst_JFM)):
            print(lst_JFM[first_three])
    else:
        for first_three in range(len(lst)):
            print(lst[first_three])

#3.25
student_names = eval(input("Enter list: "))
for name in student_names:
    if name[0] in "ABCDEFGHIJKLM":
        print(name)

#3.41
def lastF(str1, str2):
    return (str2 + ", " + str1[0] + ".")

#3.44
def distance(num):
    speed_of_sound = 340.29 * num
    result_kilometer = (speed_of_sound/1000)
    return(result_kilometer)

#Random Cinema
import random
def Random_Cinema(list_of_words):
    num_of_movies = int(input("Please enter a number of movies you'd like to generate: "))
    print("Welcome to Randoplex! Currently playing movies are:")
    for i in range(0, num_of_movies):
        print(random.choice(list_of_words) + " " + random.choice(list_of_words) + " " + random.choice(list_of_words))

Random_Cinema(eval(input("Please enter a list of words:")))


        
