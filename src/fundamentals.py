# variables and data types
    # string concatenation: "string1" + "string2"
    # f-string interpolation: f"{string1}{string2}"

name = "Eleanor" #can you single or double quotes here
favorite_color = 'purple'
age = 25

print(name)
print(f"My name is {name}") #could also do print("My name is " + name)
print("I am " + str(age) + " years old.") #the str function turns integers into strings to concatenate (called type casting)

# conditional statements
if name == 'Eleanor':
    print("You are teaching the lecture!")

if favorite_color == 'green':
    print("Your favorite color is green")
else:
    print("Your favorite color is not green")

if age < 0:
    print("Negative ages don't exist!")
elif age > -1 and age < 19:
    print("You are a child")
else:
    print("You are an adult")

# loops and sequences
    # for loops
    # while loops
for i in range(10): #automatically starts at 0
    print(i)

for i in range(5, 10): #first number is what number it starts at, second is the number it ends at
    print(i)

for i in range(5, 10, 2): #3rd number is how many to increment by
    print(i)

for i in range(10, -1, -1): #the way to decrease and reverse the numbers
    print(i)

for letter in name: #similar to the foreach loop in JS
    print(letter)

counter = 0
while counter < age:
    print(counter)
    counter += 1 #or can do counter = counter + 1, also the ability to decrement via -=

# functions
#lambda functions are asynchronous functions
        
def say_hello():
    print("Hello!")

say_hello()

def say_hello_to_someone(name):
    print(f"Hello, {name}!")

say_hello_to_someone("Isaiah")