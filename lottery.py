from random import randint
randomnumbers = []
for y in range (0, 6):
    y = randint(1,5)
    randomnumbers.append(y)
    print(y)

randomnumbers1 = []
for z in range (0,6):
    z = number(1,5)
    randomnumbers1.append(z)
    
    try:
        number = int(raw_input("Choose six numbers and enter them one by one from 1 to 49:"))
        if not (1 <= number <= 49):
            raise ValueError()
    except ValueError:
        print "Invalid option, enter numbers from 1 to 49"
        number = raw_input
    else:
        print "Your number is", number


for i in randomnumbers: 
    for j in randomnumbers1:
        if i == j:
            print "whatever"




