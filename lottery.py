from random import randint, shuffle

def luckyNumbers(rangeLeft, rangeRight, size):
    """ determines the lucky numbers which win the lottery! """
    originalRange = range(rangeLeft, rangeRight)
    shuffle(originalRange)
    return originalRange[:size]

randomnumbers = luckyNumbers(1, 59, 6)

for y in randomnumbers:
    print(y)

randomnumbers1 = []

for z in range (0,6):
    try:
        number = int(raw_input("Choose six numbers and enter them one by one from 1 to 49:"))
        if not (1 <= number <= 49):
            raise ValueError()
    except ValueError:
        print "Invalid option, enter numbers from 1 to 49"
        number = raw_input
    else:
        randomnumbers1.append(number)
        print "Your number is", number


for i in randomnumbers: 
    for j in randomnumbers1:
        if i == j:
            print "number %i matches %i" % (i, j)



