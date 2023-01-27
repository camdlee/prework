### USING LOOPS IN LISTS ###

#magicians = ['alice', 'david', 'carolina']
#for magician in magicians:
# the 'for' line of code tells python to go through the list and assigns each value to 'magician'
# then after it prints it goes back and loops to the next variable and reassigns that to 'magician'
    #print(magician)
    #print(magician.title() + ', that was a great trick!')
    #print("I can't wait to see your next trick," + magician.title() + ".\n")
    
#Anything inside the for loop is indented, anything not is not included in the loop
#print("Thank you for the show everyone!")

# Formatted strings - cleaner line of code
#foods = ['pizza', 'sushi', 'tacos']
#for food in foods:
#    print(f"I like to eat {food}")

# If statements
#foods = ['pizza', 'sushi', 'tacos']
#for food in foods:
#    print(f"I like to eat {food}")    
#    if food == 'pizza':
#        break
# once the code loops to pizza, the if statement runs the 'break' command and stops the for loop
#    if food == 'pizza':
#        continue
#    print(f"I like to eat {food}")
# continue command will skip the value in the if statement

#foods = ['pizza', 'sushi', 'tacos']
#for index in range(len(foods)):
# len(foods) will give length of list, range(len(foods)) will go through length of list
# for loop will assign each value in the range of the foods list to index as it runs the following commands
# and loop back to the next value
#    print(index)
#    print(foods[index])

#print(list(enumerate(foods)))
#enumerate will provde index of value in list to next to the value
# when printed it will result in 
# [(0, 'pizza'), (1, 'sushi'), (2, 'tacos')]
#for index, food in enumerate(foods):
#    print(f"My No {index + 1} food is {food.title()}")




### NUMERICAL LISTS ###

# range() function will list values within range specified
#for value in range(1,5):
    #print(value)
# Notice how it'll only print '1,2,3,4' for this range function

# Use range() and list() to make a list of numbers
#numbers = list(range(1,11))
#print(numbers)
# you can make it go through only even or odd numbers
# however, this will start at the 1st value, end at 2nd value, then go to every other value)
#even_numbers = list(range(2,11,2))
#print(even_numbers)
#odd_numbers = list(range(1,11,2))
#print(odd_numbers)

#squares = []
#for value in range(1,11):
    #squares.append(value**2)
#print(squares)

#Simple stats with number lists - min, max and sum
#digits = [1,2,3,4,5,6,7,8,9,0]
#print(min(digits))
#print(max(digits))
#print(sum(digits))

#List Comprehensions
# combines for loop and the creation of new elements into one line
#squares = [value**2 for value in range(1,11)]
# syntax:
# variable = [expression + for loop]
#print(squares)


### EXERCISE ###
for value in range(1,21):
    print(value)
#numbers = list(range(1,1000001))
#print(numbers)
#print(min(numbers))
#print(max(numbers))
#print(sum(numbers))
#odd_numbers = list(range(1,20,2))
#for value in range(1,20,2):
#    print(value)
#for value in range(3,30,3):
#    print(value)
#cubes = [value**3 for value in range(1,10)]
#print(cubes)


### WORKING WITH PART OF A LIST ###
#Slicing a list
#players = ['charles', 'martina','michael', 'florence', 'eli']
#print(players[0:3])
#if you omit the first value in the slice, it will automatically start from the beginning
#print(players[:4])
#if you omit the last value in the slice, it will automatically run to the end
#print(players[2:])
#if you use negative values in the slice, it will start from the end of the list
#print(players[-3:])

#Looping through a slice
#print("Here are the first three players in the roster:")
#for player in players[:3]:
#    print(player.title())

#Copying lists
#my_foods = ['pizza', 'falafel', 'carrot cake']
#friend_foods = my_foods[:]

#my_foods.append('cannoli')
#friend_foods.append('ice cream')

#print("My favorite foods are:")
#print(my_foods)
#print("\nMy friend's favorite foods are:")
#print(friend_foods)

#Tuples: an immutable list (unchangeable)
#looks just like a list but uses parentheses instead of square brackets
#dimensions = (200, 50)
#print(dimensions[0])
#print(dimensions[1])
# dimensions[0] = 250 does not work because tuples doesn't allow changes
#for dimension in dimensions:
#    print(dimension)

#You can assign new value to a variable that holds a tuple (in this case assign a new tuple to the same variable)
#dimensions = (200, 50)
#print("Original dimensions:")
#for dimension in dimensions:
#    print(dimension)

#dimensions = (400, 100)
#print("\nModified dimensions:")
#for dimension in dimensions:
#    print(dimension)

### Styling your code ###
# Python programmers usually prefer code that's easier to read than code that's easier to write.
# PEP8 recommends that you use 4 spaces per indentation level, mixing tabs and spaces will cause problems
# Each line of code should be less than 80 characters long
# Limit comments to 72 characters per line
# Use blank lines to visually group lines of code
