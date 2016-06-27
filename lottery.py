from random import randint
randomnumbers = []
for x in range (0, 6):
    y = randint(1,5)
    randomnumbers.append(y)
    print(y)


for number in range (0,6):
    z = number
    try:
        number = int(raw_input("Choose six numbers and enter them one by one from 1 to 49:"))
        if not (1 <= number <= 49):
            raise ValueError()
    except ValueError:
        print "Invalid option, enter numbers from 1 to 49"
        number = raw_input
    else:
        print "Your number is", number


if x == number :
    print "You are lucky."
else:
    print "You're not lucky today."
