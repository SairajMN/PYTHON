def add (x,y):
    return x + y 
def sub (x,y):
    return x - y
def multiple (x,y):
    return x * y
def div (x,y):
    return x / y

print("Select operation : ")
print("1.add")
print("2.sub")
print("3.multiple")
print("4.div")

while True:
    choice = input("Enter your choice (1/2/3/4):")
    if choice in ('1','2','3','4'):
        try:
            num1 = float(input("Enter first number : "))
            num2 = float(input("Enter second number : "))
        except ValueError:
            print("Invalid input. Please enter a number : ")
            continue
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {sub(num1,num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiple(num1,num2)}")
        elif choice == '4':
            print(f"{num1} / {num2} = {div(num1,num2)}")
        next_calculation = input("Let's do the next calculation? (YES/NO):")
        if next_calculation.lower() == "no" or next_calculation.lower() == 'n':
            break
        elif next_calculation.lower() == "yes" or next_calculation.lower() == 'y':
            print("")
        else:
            print("Invalid input.")
            break