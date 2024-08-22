# Check for odd number or even number
number = int(input("Enter a number: "))

print("You entered:", number)
print()

if number > 0:
    print("The number is positive.")
    print()
    if number % 2 == 0:
        print("The number is even.")
        print()
    else:
        print("The number is odd.")
        print()
elif number < 0:
    print("The number is negative.")
    print()
    if number % 2 == 0:
        print("The number is even.")
        print()
    else:
        print("The number is odd.")
        print()
else:
    print("The number is zero.")
    print()

# Multiplication table
k= int(input("Enter a number: "))

for i in range(1, 11):
     print (k, "x", i, "=", k * i)
print()

# Largest number
x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))
print()

if x > y and x > z:
    print("The largest number is:", x)
    print()
elif y > x and y > z:
    print("The largest number is:", y)
    print()
else:
    print("The largest number is:", z)
    print() 
    
# Count number of vowels
b = "Hello World zvbisdiozaaosidanadovnadoaicaod"

count = 0
for vowels in b:
    if vowels in "aeiou":
        count += 1
print("The number of vowels 'Hello World' is ", count)
print()
