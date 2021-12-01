import random
import csv

with open('Gifts.csv','w+', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Gift", "Amount", "Weight"])
    noOfGifts=int(input("Please enter the number of Gifts !! "))
    for i in range(noOfGifts) :
        print(" Gift :",i+1)
        gift = input("Enter Gift Name : ")
        amount = int(input("Enter the Number of Gift : "))
        weight = int(input("Weight of the Gift : "))
        writer.writerow([gift, amount, weight])
    while (1) :
        Decision = input("Add Gift(A) or Spin the wheel(S)  \n Choose A or S ")

        if Decision == "A" :
            gift = input("Enter Gift Name ")
            amount = input("Enter the Number of Gift : ")
            weight = input("Weight of the Gift : ")
            writer.writerow([gift, amount, weight])

        elif Decision == "S" :
            rand = random.Random(0,100)
            if rand > 80 :
                print("No Luck !!")
                break
            elif rand >70 :
                print("try again")
            
            
            total = 0
            for row in csv.reader(file):
                for col in row[2]:
                    total += int(col)

        elif Decision == "E" :
            break

        else :
            print("Input is Wrong ! Choose Between A/ S / E")