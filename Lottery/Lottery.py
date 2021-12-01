import random
import csv

with open('Gifts.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Gift", "Amount", "Weight"])
    noOfGifts=int(input("Please enter the number of Gifts !! "))
    for i in range(noOfGifts) :
        print(" Gift :",i+1)
        gift = input("Enter Gift Name ")
        amount = input("Enter the Number of Gift")
        weight = input("Weight of the Gift")
        writer.writerow([gift, amount, weight])
    

    
    
