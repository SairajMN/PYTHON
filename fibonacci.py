def is_fibonacci(num):
    a, b = 0, 1
    while b <= num: 
        if b == num:
            return True
        a, b = b, a + b
    return False 

fib = int(input("Enter number: "))
if is_fibonacci(fib):
    print(f"{fib} is a part of fibonacci sequence")
else:
    print(f"{fib} is not part of fibonacci sequence")
