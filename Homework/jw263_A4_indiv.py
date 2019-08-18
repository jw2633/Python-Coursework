#James Wang
#I211
#Indiv. HW4
#Team 13

#1
# %B displays the full name of the month.

#2
#import needed modules
#define a function
#set data to open .csv file and read
#implement a for loop
#write if statments if they're "Saturday" or "Sunday"
#append it to empty list items if "Saturday" or "Sunday"
#print results


#3
#Write a program that reads in the information from a file called
#ShopRecords.csv and displays all of the items that were sold on a weekend.

import csv,datetime

def printinfo():
    data = csv.DictReader(open("ShopRecords.csv","r"))
    items = []
    for day in data:
        #classify datez as the dates from the csv
        datez = day["Date"].split("/")
        #date right now
        now = datetime.date.today()
        dayz = datetime.date(int(datez[2]),int(datez[0]),int(datez[1]))
        #difference between now and the list of dates
        age = now - dayz

        #get year of age
        age_in_years = int(age.days/365)
        
        #if item was on Saturday or Sunday
        if dayz.strftime("%A") == "Saturday":
            items.append(day["Item"])
        elif dayz.strftime("%A") == "Sunday":
            items.append(day["Item"])
    print("\n".join(items))
    #Converts list into printing each item on its own line.



