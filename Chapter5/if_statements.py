### IF STATEMENTS ###

#cars = ["audi", "bmw", "subaru", "toyota"]
#for car in cars:
#    if car == "bmw":
#        print(car.upper())
#    else:
#        print(car.title())

#if statement is essential a conditional statement; if condition is true then it will execute code
#== means that it must be equal to this value; = only assigns right value to left side
#Python is case sensitive, so be careful of capitalization
#can use .lower() function or .upper() function to temporarily change value

#use != to check for inequality; != means not equal to 
#requested_topping = 'mushrooms'
#if requested_topping != 'anchovies':
#    print("Hold the anchovies!")

#To check multiple conditions use "and" or "or" in if statement
#age1 = 18
#age2 = 21
#age1 >= 21 or age2 >= 21

#Checking if a value is in a list
#toppings = ['mushrooms', 'onions', 'pineapple']
#'mushrooms' in toppings
#should print true

#Check if value is not in a list
#banned_users = ['andrew', 'carolina', 'david']
#user = 'marie'
#if user not in banned_users:
#    print(user.title() + ", you can post a response if you wish")

#Boolean Expression means conditional test 
#boolean value is either True or False


### EXERCISE ###
#sport = "volleyball"
#print("Is sport == 'volleyball'? I predict True.")
#print(sport == 'volleyball')
#print("\nIs sport == 'golf'? I predict False.")
#print(sport == 'golf')

### VIDEO ###

#my_bool = True
#print(my_bool)
#my_bool = False
#print(my_bool)
#print(bool([1]))

# Boolean expression evaluates true or false
# Operators:
# < less than
# > greater than
# == equal to
# != not equal to

#print(4 == 4.0)

#x = 10
#y = 10
#z = 20
#print(x ==10 or z == 10)

#x = 8
#y = 9
#print(x != y)
# can also print it this way
# print(not x == y)

#Advice:start thinking in if then statements, it will help formulate solutions

#if BOOLEAN OR BOOLEAN EXP:
    #code block
    #for if true
# else:
    # for the if false code block

#height = 65
# must be 5 ft tall to ride my ride
# must be under 6 ft tall to ride
#if height < 60:
#    print('You are too short to ride.')
#elif height > 72:
#    print('You are too tall to ride.')
#else:
#    print('You are able to ride.')

#elif is 'else if...' meaning after checking the first condition it will check this condition next

### Nesting if statements in for loops ###

#requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
#for requested_topping in requested_toppings:
#    if requested_topping == 'green peppers':
#        print('Sorry, we are out of green peppers right now.')
#    else:
#        print("Adding " + requested_topping + ".")
#print("\nFinished making your pizza.")

### Checking that list is not empty
#requested_toppings = ['mushroom']
#if requested_toppings:
#    for requested_topping in requested_toppings:
#        if requested_topping == 'green peppers':
#            print('Sorry, we are out of green peppers right now.')
#        else:
#            print("Adding " + requested_topping + ".")
#    print("\nFinished making your pizza.")
#else:
#    print("Are you sure you want a plain pizza?")

### Using mulpitle lists
available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple','extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']
for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")
print("\nFinished making your pizza.")
