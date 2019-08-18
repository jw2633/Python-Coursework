#James Wang
#I211
#Indiv. HW3
#Team 13

#1
#Algorithms

###2
#Download "runners.txt"
#Open "runners.txt"
#For every name followed by a number, put each at their own list and split them from the rest.

###3
#print("In the 2017 100 yard dash the top finishers were: ")
#In file_contents, try to grab each sublist from the list and call it "element".
#Pop the last element in each sublist.
#Join the element so that it won't print out a list (or with commas)
#print out the result.

###4
#Print("Names with two parts to them: ")
#Stay within the print statement.
#Make a list called "two_part" that has a list of names with two parts.
#Use variable "i" in file_contents 
#If position 0 of i contains a name from list two_part, implement that to i
#Join with " " to remove commas between the names
#print out the result

###5
#print("People in top positions: ")
#Make a new list called top_3 with the numbers 1, 2, and 3 in that list
#Use variable "i" in file_contents
#If position 1 of i contains a number from list top_3, implement that to i
#Join with " " to remove commas between the names
#print out the result



#2
#Use a list comprehension to load the data from a file named “runners.txt”.
#There’s a sample file on Canvas with the data shown above.

file_contents = [line.strip().split(" ") for line in open("runners.txt","r")]
##opens up the runners.txt file into read format and puts the names/position into their own sublist
##within the overall list.
two_part = ["De", "Grasse", "Youssef", "Meite"]
top_3 = ["1", "2", "3"]

#3
#Use the information read in from the file to print out the names
#of the top 6 finishers formatted as shown in the example above.

print("In the 2017 100 yard dash the top finishers were: ")
for element in file_contents:
    element.pop(-1)
    print(" ".join(element))
##This takes every name from each sublist of file_contents and prints them out. Pops out the position number.

#4
#Use a list comprehension to create a list of the names that have two parts to them.

print("Names with two parts to them: ", [(" ".join(i)) for i in file_contents if i[0] in two_part])

##If the name is within two parts, it takes position 0 of that name and joins it together to create one name.

#5
#Use a list comprehension to create a list of the people who finished in the top the positions.
file_contents = [line.strip().split(" ") for line in open("runners.txt","r")]
top_3 = ["1", "2", "3"]

print("People in top positions: ", [(" ".join(i)) for i in file_contents if i[1] in top_3])
