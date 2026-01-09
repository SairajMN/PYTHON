def spam():
    print(eggs)

# spam() if spam fun called here it would through erro like
# PS C:\Users\saira\OneDrive\Desktop\python> python .\ex.py
# Traceback (most recent call last):
#   File "C:\Users\saira\OneDrive\Desktop\python\ex.py", line 4, in <module>
#     spam()
#     ~~~~^^
#   File "C:\Users\saira\OneDrive\Desktop\python\ex.py", line 2, in spam
#     print(eggs)
#           ^^^^
# NameError: name 'eggs' is not defined

eggs = 42
spam()# here eggs is already defined before fun call
print(eggs)