def sequential_search(dlist, item):
    pos = 0
    found = False
    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1
    return found, pos
my_list = [11,23,58,31,56,77,43,12,65,19]

search_item = int(input("Enter item to be searched : "))
result, position = sequential_search(my_list, search_item)
if result == True:
    print(f"Is {search_item} found? {result}, at position {position}")
else:
    print(f"Is {search_item} found? {result}")
