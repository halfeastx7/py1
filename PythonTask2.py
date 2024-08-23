def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Jack")
print()

def greet_user(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet_user("Jane")
print()

def sum_numbers(a, b):
    return a + b   

result = sum_numbers(5, 10) 
print(result)
print()

fruits = ["apple", "banana", "cherry", "date"]
print(fruits)
fruits.append("elderberry")
print(fruits)
fruits.remove("banana")
print(fruits)
fruits.insert(2, "blueberry")
print(fruits)
fruits.sort()
print(fruits)
print()


for i in range(1, 11):
    print(i)
    if i == 7:
        print("Breaking the loop")
        break
print()

for n in range(1, 11):
    if n == 3:
        continue
    print("Current number is:", n)
print()
