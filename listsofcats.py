# print('Enter the name of cat1 : ')
# catname1= input()
# print('Enter the name of cat2 : ')
# catname2= input()
# print('Enter the name of cat3 : ')
# catname3= input()
# print('Enter the name of cat4 : ')
# catname4= input()
# print('Enter the name of cat5 : ')
# catname5= input()
# print('Enter the name of cat6 : ')
# catname6= input()
# print('The cat names are : ')
# print(catname1 + ' ' + catname2 + ' ' + catname3 + ' ' + catname4 + ' ' + catname5 + ' ' + catname6)

# a bove is one way to do it

# now using lists

catsnames = []

while True:
    print('Enter the name of the cats ' + str(len(catsnames)+1) + ' (or type "done" to finish): ')
    name = input()
    if name.lower() == 'done':
        break
    catsnames= catsnames + [name]  # or catsnames.append(name)
print('The cat names are : ')
for name in catsnames:
    print(' ' + name)