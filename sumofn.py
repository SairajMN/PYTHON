num = int(input("Enter a positive number : "))
if num < 0 :
    print("Please enter a positive number.")
else:
    total = 0
    while num > 0 :
        total += num
        num -=1
    print(f"The sum of given natural number is : {total}")