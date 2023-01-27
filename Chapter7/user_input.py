### User input and While loops ###

# Flag - signal to program
#prompt = "\nTell me something, and I will repeat it back to you:"
#prompt += "\nEnter 'quit' to end the program."

#active = True
#while active:
#    message = input(prompt)
#    if message == 'quit':
#        active = False
#    else:
#        print(message)

# Using 'break' to exit a loop
#prompt = "\nPlease enter the name of a city you have visited:"
#prompt += "\nEnter 'quit' when you are finished."

#while True:
#    city = input(prompt)
#    if city == 'quit':
#        break
#    else:
#        print("I'd love to go to " + city.title() + "!")

# Using continue in a loop
#current_number = 0
#while current_number < 10:
#    current_number += 1
#    if current_number % 2 == 0:
#        continue

#    print(current_number)

# Moving Items from one list to another
#unconfirmed_users = ['alice', 'brian', 'candace']
#confirmed_users = []

#while unconfirmed_users:
#    current_user = unconfirmed_users.pop()

#    print("Verifying user: " + current_user.title())
#    confirmed_users.append(current_user)

#print("\nThe following users have been confirmed:")
#for confirmed_user in confirmed_users:
#    print(confirmed_user.title())

# Removing all instances of specific values from a list
#pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
#print(pets)
#while 'cat' in pets:
#    pets.remove('cat')
#print(pets)

# Filling a dictionary with User input
responses = {}
#Set a flag to indicate poll is active
polling_active = True
while polling_active:
    #Prompt users for name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday?")
    #Store the response in the dictionary
    responses[name] = response
    #find out if anyone else is going to take the poll
    repeat = input("Would you like to let another person respond? (yes/no) ")
    if repeat == 'no':
        polling_active = False
#polling is complete. show the results
print("\n--- Polling Results ---")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")



### Video

#while loop
# while Boolean or Booelean expression:
    # code block
    # to run while
    # condition is true

#You must be over 5 feet to ride my ride
#I have a magic potion that will let you grow one inch everytime you use it
#height = 55
#User input:
#height = int(input("What is your height in inches? "))
#while height < 60:
#    height += 1
#    if height < 58:
#        continue
#    print(f"You are {height} inches tall \n and too short to ride.")
#    print("Take this magic potion")
#print("Thanks for coming")


#while True:
#    response = input("What do you want to do? Say hi [h], Say goodbye [g], or Quit?[q]")
#    if response.lower() == "h":
#        print("hello")
#    elif response.lower() == "g":
#        print("goodbye")
#    elif response.lower() == "q":
#        break
#    else:
#        print("invalid response")

#age = int(input("What is your age? "))
#while age > 10:
#    age -= 1
#    print(age, end = " ")

#age = 13
#while age > 10:
#    print("You are too old", end = " ")
#    if age == 13:
#        break
#    age += 1

#age = 1 
#while age < 10:
#    if age % 2 == 1:
#        if age == 3:
#            print("ding", end = " ")
#        elif age == 4:
#            print("dong", end = " ")
#        elif age == 5:
#            print("the", end =" ")
#        print("which", end=" ")
#    age += 1 
#print("is dead", end = " ")


#i = 6
#while i <=10:
#while i is less than or equal to 10 run the following
#    for j in range(3):
    #for value in range 0,1,2,3 run
#        i *= j+2
        #i = 6*(0+2)
#        print(j, end = " ")
        #print(0 )
#        break


#num = 1 
#new_num = 0
#while num < 10:
#while num is less than 10 run following
    #for i in range(3):
    #for value in range 0,1,2 run...
    #    new_num += 1
        #0+1
        #1+1
        #2+1 = 3
    #num += 2
    #now num = 2, then continue running for loop
    #so next time num = 4, new_num = 6
    #logically, the while loop will run 5 times
    #each time, new_num will add 3, so
    #5 x 3 = 15
#print(new_num)
