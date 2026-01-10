import random, sys
print('ROCK, PAPER, SCISSORS')
wins = 0
losses = 0
ties = 0

while True:#MAIN GAME LOOP
    print('%s Wins, %s Losses, %s Ties' %(wins, losses, ties))
    while True:
        print('Enter your move : (r)ock, (p)aper, (s)cissor or (q)uit')
        playermove = input()
        if playermove == 'q':
            sys.exit()
        if playermove == 'r' or playermove == 'p' or playermove == 's':
            break
        print('Type one of r, p, s, or q.')

    #DISPLAYS WT PLAYER GAVE
    if playermove == 'r':
        print('ROCK Versus.....')
    elif playermove == 'p': 
        print('PAPER Versus.... ')
    elif playermove == 's':
        print('SCISSORS Versus....')

    #WT COMP CHOSE
    randomnum = random.randint(1,3)
    if randomnum == 1:
        compmove = 'r'
        print('ROCK')
    elif randomnum == 2:
        compmove = 'p'
        print('PAPER')
    elif randomnum == 3:
        compmove = 's'
        print('SCISSORS')

    #win/losses/ties
    if playermove == compmove:
        print('It Is A Tie!')
        ties=ties+1
    elif playermove == 'r' and compmove == 's':
        print('YOU WIN!')
        wins=wins+1
    elif playermove == 'p' and compmove == 'r':
        print('YOU WIN!')
        wins=wins+1
    elif playermove == 's' and compmove == 'p':
        print('YOU WIN!')
        wins=wins+1
    elif playermove == 'r' and compmove == 'p':
        print('YOU LOSE!')
        losses=losses+1
    elif playermove == 'p' and compmove == 's':
        print('YOU LOSE!')
        losses=losses+1
    elif playermove == 's' and compmove == 'r':
        print('YOU LOSE!')
        losses=losses+1

    
