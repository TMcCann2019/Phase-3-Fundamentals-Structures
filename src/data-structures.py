# lists and list comprehension
#list is the same as an array in javascript

#ordered and mutable and zero indexed
nums = [1, 2, 3, 4, 5]
print(nums[2:4]) #starts at index 2 and goes up to but does not include index 4
#no value after the colon means it goes to the end of the list
#no value before the colon means it goes up to but does not include the index chosen after the colon

#to add to a list you use .append() (but not the only way to make it longer)
nums.append(6)
print(nums)

nums[5] = "six"

nums.pop() #removes the element that is specificed in the () and if nothing is specified it will remove the last element
#removes and returns that item

nums2 = [1, 2, 3, 4, 5, 6]
for num in nums2:
    print(num)

squares = []
for num in nums2:
    num_squared = num ** 2
    squares.append(num_squared)

print(squares)

#list comprehension
squares2 = [num ** 2 for num in nums2]
print(squares2)

even_cubes = []
for num in nums2:
    if num % 2 == 0: #checks to see if even
        even_cubes.append(num ** 3)
print(even_cubes)

even_cubes2 = [num ** 3 for num in nums2 if num % 2 == 0] #list comprehension of the even_cubes
print(even_cubes2)

# dictionaries
#made up of key value pairs

ages = {"Eleanor": 25, "Tim": 32, "Jay": 29, "Andrew": 23, "Ethan": 31, "Isaiah": 33, "Dave": 37, "Kylie": 28, "Kevin": 29}

print(ages["Dave"]) #accessed via keys to get values
ages["Tyler"] = 30 #a way to add that key value pair to the dictionary

ages["Dave"] = 15 #a way to update the value of that key in the dictionary

for key in ages:
    print(key) #a way to print out the keys
    print(ages[key]) #a way to print out the values

#there is a dictionary comprehension that is similar to the list comprehension

# sets
#unordered and non-repeated, declared with {}
plants = set()
plants.add("tree")
plants.add("flower")
plants.add("grass")
plants.add("flower")
plants.add("dandelion")

print(plants)

print(len(plants)) #says the length of the set

# tuples
#immutable
coordinate = (20, 30) #coordinates; an x and y set of numbers stuck together
color = (3, 200, 0) #rgb color pickers are tuples

#start at 0 index and have indices
print(coordinate)
print(color)