import random
import csv
import pandas as pd

giftDict = {}
k=[]
df = pd.read_csv("Gifts.csv")
print(df)
giftlist = ()

while (1) :
        Decision = input("Add Gift(A) or Spin the wheel(S)  \n Choose A or S : ")
        flag = 0
        if Decision == "A" :
            gift = input("Enter Gift Name ")
            amount = int(input("Enter the Number of Gift : "))
            weight = input("Weight of the Gift : ")
            for i in range(len(df)) :
                if df['Gift'][i] == gift :
                    df.loc[i,'Amount'] -= amount
                    df.loc[i,'Weight'] = weight
                    flag=1
                

            if flag==0 :
                df.loc[i+1,'Gift'] = gift
                df.loc[i+1,'Amount'] = amount
                df.loc[i+1,'Weight'] = weight

        elif Decision == "S" :
            rand = random.randint(0,100)

            if rand > 95 :
                print("No Luck !!")
                break
            elif rand > 90 :
                print("try again")

            else :
                prob = 0
                total = 0
                x=0
                print ("Check point 1")
                for col in df["Weight"]:
                    total += int(col)
                        
                print(total)
               
                for col in df["Weight"]:
                        x = int(col)
                        prob = x/total
                        k.append(prob)

                giftlist = list(df["Gift"])
                giftDict = dict(zip(k,giftlist))
                
                #giftDict = dict(giftDict)
                rand = random.randint(0,100)/100
                for i in sorted(giftDict):
                    if rand < i :
                        print("Congratulations You have won ", giftDict[i])
                        gift = giftDict[i]
                        break
                
                for i in range(len(df)) :
                    if df['Gift'][i] == gift :

                         df.loc[i,'Amount'] -= 1

            #break

        else :
            print("Input is Wrong ! Choose Between A / S ")

df.to_csv('Gifts.csv',index= False)