from random import randrange

random_number = randrange(1, 10)
print random_number

count = 0
# Start your game!

while count < 3:
    guess = int(raw_input("Enter guess #{}: ".format(count + 1)))
    count += 1
    if guess == random_number:
        print "You win!"
        break
else:
    print "You lose :("