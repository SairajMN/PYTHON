import re
text = "Hello, i am Python program, i can help to create projects."
pattern = r"\bp\w+"
matches = re.findall(pattern,text)
print(matches)