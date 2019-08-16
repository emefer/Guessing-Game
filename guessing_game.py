MAX = 10
MIN = 1
print ("Guessing game\n\n")
number = input ("Insert a number between " + str(MIN) + " and " + str(MAX) + ": ")
number = int(number)
while (number < MIN or number > MAX):
    print ("Number is out of range!\n")
    number = input ("Insert a number between " + str(MIN) + " and " + str(MAX) + ": ")
    number = int(number)