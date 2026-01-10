import random
secretnum = random.randint(1,20)
print('I am thinking of a number between 1 to 20.')
for guesstaken in range(1,7):
    print('Take a guess.')
    guess=int(input())

    if guess < secretnum:
        print('Your guess is too low.')
    elif guess > secretnum:
        print('your guess is too high.')
    else:
        break

if guess  == secretnum:
    print('Good job! you guessed my number in ' +str(guesstaken) +' guesses!')
else:
    print('Nope. The number I was thinking of was ' +str(secretnum))