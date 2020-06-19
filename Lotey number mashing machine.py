print ("Welcome to the amazing number machine!")

print ("I can take your numbers and mash them any way I see fit")

print ("")

print ("May I have your first number please:")

onum = input (" ")

print ("") 

print ("May I have your second number please:")

tnum = input (" ")
print ( "Aha!")

onum = int (onum)
tnum = int (tnum)

print ("The answer is" ,(onum+tnum), "when I add",onum,"by",tnum,)
print ("The answer is" ,(onum-tnum), "when I subract",onum,"by",tnum,)
print ("The answer is" ,(onum*tnum), "when I multiply",onum,"by",tnum,)
print ("The answer is" ,(onum/tnum), "when I divide",onum,"by",tnum,)
print ("The answer is" ,(onum**tnum), "when I take",onum,"^",tnum,)
print ("and finally...When I divide",onum,"by",tnum,"I get",(onum//tnum),"and the remander is" ,(onum%tnum),)

