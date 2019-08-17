#Lab Practical 2 James Wang

from tools import *

# Section 1
with open ("california.txt", "r") as f:
    counties = f.readlines()

county_stats = {}

for i in range(len(counties)):
    name, population = counties[i].strip().split("\t ")
    county_stats[name] = int(population.replace(",",""))

print(county_stats)


with open ("texas.txt", "r") as g:
    counties2 = g.readlines()

county_stats2 = {}
for j in range(len(counties2)):
    name2, population2 = countes2[i].strip().split('\t ')
    county_stats2[name2] = int(population2.replace(',',''))

print(county_stats2)

which_state = input("Which state's totals would you like to compute?")
if which_state == california:
    print(county_stats)
else:
    print(county_stats2)

# Section 2
state = {}
section2 = input("Which states totals would you like to compute? (or STOP) ")

while section2.upper() != "STOP":
    if section2 == 'california':
        print(county_stats)
    elif section2 == 'texas':
        print(county_stats2)

print(state)

#Section 3
section3 = input("Which states totals would you like to compute? (or STOP) ")

labels1 = [('\t '), "Name", "Votes"]
votes1 = [(name, reverse(sorted(population)))]

lables2 = [('\t '), "Name", "Votes"]
votes2 = [(name2, reverse(sorted(population2)))]


while section3.upper() != "STOP":
    if section3 == 'california':
         table_print(labels1, votes1)
    elif section3 == 'texas':
          table_print(labels2, votes2)

print("The candidates earned this many votes:")
print(section3)

#Section 4
print("The breakdown by percent:")
total1 = sum(population)
total2 = sum(population2)
labels1.1 = [('\t '), "Name", "Percentage"]
votes1.1 = [(name, ((total1)/5), "%"]

lables2.2 = [('\t '), "Name", "Percentage"]
votes2.2 = [(name2, ((total2)/5), "%"]


while section3.upper() != "STOP":
    if section3 == 'california':
         table_print(labels1.1, votes1.1)
    elif section3 == 'texas':
          table_print(labels2.2, votes2.2)
        
        
