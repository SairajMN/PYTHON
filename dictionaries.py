person = {
    "name" : "Alice",
    "age" : 25,
    "Occupation" : "programmer"
}
print('About Alice')
print('')
print(person)
print(person["name"])
person["age"] = 26
person["hobby"] = "reading"
del person ["Occupation"]
for key, value in person.items():
    print(key,value)
animal = dict(
    name = "Leo",
    species = "Lion",
    age = 5
)
print('')
print('About Lion')
print(animal)
