# tictactoe using the dict and random module
import random

theboard = {'top-L' : ' ', 'top-M' : ' ', 'top-R' : ' ', 'mid-L' : ' ', 'mid-M' : ' ', 'mid-R' : ' ', 'low-L' : ' ', 'low-M' : ' ', 'low-R' : ' '}

def printboard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])



# x are user, o are computer or random moves
turn = 'X'
for i in range(9):
    printboard(theboard)
    if turn == 'X': # user's turn
        print('Your turn. Enter a position (top-L, top-M, top-R, mid-L, mid-M, mid-R, low-L, low-M, low-R): ')
        move = input()
        if theboard[move] == ' ':
            theboard[move] = 'X'
            turn = 'O'
        else:
            print('Position already taken. Try again.')
            continue
    else: # computer's turn or random move
        print("Computer's turn.")
        available_moves = [key for key, value in theboard.items() if value == ' ']
        move = random.choice(available_moves)
        theboard[move] = 'O'
        turn = 'X'
printboard(theboard)
print('Game Over.')
