print("\n\n----------welcome to Hotal bilal----------\n\n")


print("1.chicken biriyani\n2.mutton biriyani\n3.fried rice\n4.egg rice\n5.parotta\n\n")

foods = ["1.chicken biriyani", "2.mutton biriyani", "3.fried rice", "4.egg rice", "5.parotta"]
price = [160,350,100,110,60]

myfoodorder = []
myordercost = []
quantity = 0
counter = 0
total = 0




print("----------welcome to Hotal bilal----------\n\n")


order = input("can i take your order: Yes  or No :")
if order == "No":
    exit()
else:
    print("thank you\nwelcome to our hotal.....")

anotherorder = True

while anotherorder == True:

    foodorder = input("please enter the food item:\n")

    if foodorder == "chicken biriyani" or foodorder == "1":
        print("your choose food is:\t" + (foods[0]) + "\n")
        print("your Food price    :\t" + str(price[0]) + "\n")
        myfoodorder.append(foods[0])
        myordercost.append(price[0])
        counter = counter + 1
        quantity = int(input("enter your quantity:"))
        quantity = quantity * (price[0])
        total = total + quantity
        

    elif foodorder == "mutton biriyani" or foodorder == "2":
        print("your choose food is:\t" + (foods[1]) + "\n")
        print("your Food price    :\t" + str(price[1]) + "\n")
        myfoodorder.append(foods[1])
        myordercost.append(price[1])
        counter = counter + 1
        quantity = int(input("enter your quantity:"))
        quantity = quantity * (price[1])
        total = total + quantity
        

    elif foodorder == "fried rice" or foodorder == "3":
        print("your choose food is:\t" + (foods[2]) + "\n")
        print("your Food price    :\t" + str(price[2]) + "\n")
        myfoodorder.append(foods[2])
        myordercost.append(price[2])
        counter = counter + 1
        quantity = int(input("enter your quantity:"))
        quantity = quantity * (price[2])
        total = total + quantity
        

    elif foodorder == "egg rice" or foodorder == "4":
        print("your choose food is:\t" + (foods[3]) + "\n")
        print("your Food price    :\t" + str(price[3]) + "\n")
        myfoodorder.append(foods[3])
        myordercost.append(price[3])
        counter = counter + 1
        quantity = int(input("enter your quantity:"))
        quantity = quantity * (price[3])
        total = total + quantity
        
        

    elif foodorder == "parotta" or foodorder == "5":
        print("your choose food is:\t" + (foods[4]) + "\n")
        print("your Food price    :\t" + str(price[4]) + "\n")
        myfoodorder.append(foods[4])
        myordercost.append(price[4])
        counter = counter + 1
        quantity = int(input("enter your quantity:"))
        quantity = quantity * (price[4])
        total = total + quantity
        

    else:
        print("not on menu")
        anotherorder = True
    finised = input("have you finished your order: Y/N : ")
    if finised == "N":
        anotherorder=True
    else:
        anotherorder = False 


print("Your order is:")
print("              ")
print("**************")
print("choose item of foods count : " + str(counter) )   
print("item:" + str(myfoodorder))

print("total is :" + str(total))



