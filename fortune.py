import  random

# getting answer for fortune for this function
def getans(ansnum):
    if ansnum == 1:
        return 'It is certain'
    elif ansnum == 2:
        return 'It is decidedly so'
    elif ansnum == 3:
        return 'Yes'
    elif ansnum == 4:
        return 'Reply hazy try again'
    elif ansnum == 5:
        return 'Ask again later'
    elif ansnum == 6:
        return 'Conceentrate and ask again'
    elif ansnum == 7:
        return 'My reply is no'
    elif ansnum == 8:
        return 'Outlook not so good'
    elif ansnum == 9:
        return 'Very doubtful'
    

# WE CAN WRITE LIKE THIS ALSO
# r = random.randint(1,9)
# fortune = getans(r)
# print(fortune)

# Using random randint to get values in between 1 to 9
print(getans(random.randint(1,9)))