



print ("Hello,")


User1 = input ("May I have your name please? ")

print  ("")

print ("Nice to meet you :)",User1,)

print ("")

print ("Our daily specials are:") 





print ("")

print ("Bacon ................$344400")
print ("Chicken ............$34543245")
print ("Curry ................$666873")
Meal = input ("What food would you like to have? ")
    
print ("")

print ("Great choice" ,User1,) 

print ("")

print ("What would you like to drink? We have")
print ("Milk .......$9999999")
print ("Coke ........$222222")
print ("Water ....$111111111")
Bev = input ("What would you like to drink? ")

print ("")

Bacon = float (344400)
Chicken = float (34543245)
Curry = float (666873)
Coke = float (222222)
Water = float (9999999)
Milk = float (111111111)


if Meal == "Bacon":
    Meal = float (344400)
if Meal == "Chicken":
    Meal = float (34543245)
if Meal == "Curry":
    Meal = float (666873)
if Bev == "Coke":
    Bev = float (222222)
if Bev == "Milk":
    Bev = float (9999999)
if Bev == "Water":
    Bev = float (111111111)

print ( "I will be right back" ,User1, "with your" ,Meal, "and" ,Bev)

print ('')
tax = int (0.05)
bill = float (Meal+Bev*tax)
Bill = float (Meal+Bev)
print ("Your bill without tax will be",Bill," and your bill with tax will be", bill) 
