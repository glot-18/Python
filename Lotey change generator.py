print ("Welcome to the Change Generator")

print ("")

cost1 = input ("How much did the item cost: $")
cost2 = input ("How much did the person give you: $")

cost1 = float (cost1)
cost2 = float (cost2)
chang1e = float (cost2-cost1)

print ("")

print ("The bills or the change should be $ ",chang1e,round,)

print ((round(chang1e//20)), "twenties")
(chang1e%20)

print ((round(chang1e//10)), " tens")
(chang1e%10)

print ((round(chang1e//5)), " fives")
(chang1e%5)

print ((round(chang1e//1)), " ones")
(chang1e%1)

print ((round(chang1e//0.25)), " quarters")
(chang1e%0.25)

print ((round(chang1e//0.10)), " dimes")
(chang1e%0.10)

print ((round(chang1e//0.05)), " nickels")
(chang1e%0.05)

print ((round(chang1e//0.01)), " pennies")
(chang1e%0.01)

