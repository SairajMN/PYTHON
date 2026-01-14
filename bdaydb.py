#using dictionaries to store BDAY info
bdaydb = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'} # Alice is key, Apr 1 is value (key:value pair)

while True:
    print('Enter a name (or type "exit" to see the methods): ')
    name = input().capitalize()
    if name.lower() == 'exit':
        break
    if name in bdaydb:
        print(name + "'s birthday is " + bdaydb[name])
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        bdaydb[name] = bday
        print('Birthday DB updated.')


# keys and values methods
print('\nAll names in the BDAY DB:')
for name in bdaydb.keys():
    print(name)

print('\nAll BDAYs in the BDAY DB:')
for bday in bdaydb.values():
    print(bday)

# To see all entries in the BDAY DB using items() method
print('\nBDAY DB:')
for name, bday in bdaydb.items():
    print('key: ' + name + ': ' +'value: ' + bday)


# using get method
print('\nUsing get method:')
name = input('Enter a name to look up their BDAY: ').capitalize()
bday = bdaydb.get(name, 'Not found in DB.')
print(name + "'s Birthday is: " + bday)

# setdefault method for new entries
print('\nUsing setdefault method:')
name = input('Enter a name to add to the BDAY DB: ').capitalize()
bday = input('Enter their birthday: ')
#setting default birthday is 'Jan 1' if name not in DB
bdaydb.setdefault(name, bday if bday else 'Jan 1')
print('Updated BDAY DB:')
print(name + "'s Birthday is: " + bdaydb[name])