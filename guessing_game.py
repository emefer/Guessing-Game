import random

MAX = 10
MIN = 1

genNumber = random.randint(MIN, MAX)
#print ("Generated number: " + str(genNumber))
print ("Guessing game\n\n")
number = input ("Insert a number between " + str(MIN) + " and " + str(MAX) + ": ")
try:
    number = int(number)
except:
    print ("Please enter only numbers\n")    
tries = 1

while (number != genNumber):    
    tries = tries + 1
    if (genNumber < number):
        print ("My number is lower. Try again!\n")
    else:
        print ("My number is higher. Try again!\n")    
    number = input ("Insert a number between " + str(MIN) + " and " + str(MAX) + ": ")
    number = int(number)

print ("You guessed it in " + str(tries) + " tries!\n")
