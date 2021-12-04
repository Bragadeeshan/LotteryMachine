import random
import csv
import pandas as pd

giftDict = {}
k=[]
df = pd.read_csv("Gifts.csv")
print(df)
giftlist = ()

while (1) :
        Decision = input("Add Gift(A) or Spin the wheel(S)  \n Choose A or S : ") #decision between adding and Spinning the wheel
        flag = 0 #flag to check whether a gift is already there or not
        if Decision == "A" : #if the user wanted to add an item
            gift = input("Enter Gift Name ")
            amount = int(input("Enter the Number of Gift : "))
            weight = input("Weight of the Gift : ")
            for i in range(len(df)) : #loop to check through the csv
                if df['Gift'][i] == gift :
                    df.loc[i,'Amount'] = df.loc[i,'Amount'] + amount #if the gift is already there adding the amount
                    df.loc[i,'Weight'] = weight #changing the weight if changed
                    flag=1
                

            if flag==0 : #if the item is not in the csv
                df.loc[i+1,'Gift'] = gift 
                df.loc[i+1,'Amount'] = amount
                df.loc[i+1,'Weight'] = weight #adding the item to the list

        elif Decision == "S" : #if Spinning the wheel got selected by the user
            rand = random.randint(0,100) #selecting a random number

            if rand > 95 : # if the random number is above 95 the player loses
                print("No Luck !!")
                break
            elif rand > 60 : #if the number is between 95 and 90 player can try again
                print("try again")

            else :
                prob = 0
                total = 0
                x=0
                #print ("Check point 1")
                for col in df["Weight"]: #calculating the total weight
                    total += int(col)
                        
                #print(total)
               
                for col in df["Weight"]:
                        x = int(col)
                        prob = x/total #calculating the probability
                        k.append(prob) #appending it to a lis

                giftlist = list(df["Gift"])
                giftDict = dict(zip(k,giftlist)) #creating a list to hold the gift and the probability
                
                #giftDict = dict(giftDict)
                rand = random.randint(0,1000)/1000 #getting a random number between 100
                gift = 0
                j=0
                for i in sorted(giftDict):
                    j=j+i
                    if rand < j :
                        print("Congratulations You have won ", giftDict[i])
                        gift = giftDict[i]
                        break
                if(gift == 0) :
                    print("Congratulations You have won ", giftDict[i])
                    gift = giftDict[i]    
               
                for i in range(len(df)) :
                    if df['Gift'][i] == gift :

                         df.loc[i,'Amount'] = df.loc[i,'Amount'] - 1 #deducting the gift from the dataframe
                         if  df.loc[i,'Amount'] == 0 :
                             data = data.drop(index = gift, axis=0) #if the number of gifts go to zero drop it 
                break
            

        else :
            print("Input is Wrong ! Choose Between A / S ")

df.to_csv('Gifts.csv',index= False)