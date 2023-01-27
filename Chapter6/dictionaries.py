### DICTIONARIES ###

#dictionaries allow you to connect pieces of related info
#Dictionary: collection of key-value pairs
#Each key is connected to a value
#A key can be a number, string, list or another dictionary
#Dictionaries use {} braces with key pairs inside

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])

#to get the value associated to a certain key, give name of dictionary
#then place the key inside a set of square brackets
#print(name of dictionary['key'])
#print(alien_0['points'])

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0['color'])
#print(alien_0['points'])
#new_points = alien_0['points']
#print("You just earned " + str(new_points) + " points!")


#Dictionaries are dynamic, can add new pairs anytime
#To add, type dictionary name then add [] with key inside, then = to new value

#alien_0 = {'color': 'green', 'points': 5}
#print(alien_0)
#alien_0['x_position'] = 0
#alien_0['y_position'] = 25
#print(alien_0)



### VIDEO ###
#my_dict = {}
#my_dict = dict()

#my_dict= {"key":"value"}
#my_dict = dict(key="value")

#steve = {
#    "name": "Steve",
#    "weight": 155.5,
#    "height": 70,
#    "foods": ['steak', 'chicken', 'tacos'],
#    "ice_cream": {
#       "vanilla":False,
#        "chocolate":True,
#        "coffee": False
#    },
#    10 : "This has an integer key"
#}

#for key, value in steve.items():
#    if isinstance(value,list):
#        print(f"The list is at {key}")
        

#print(steve.items())
#for key, value in steve.items():
#    print(key, end=": ")
#    print(value)

#print(steve.values())
#for value in steve.values():
#    print(value)
#    print(type(value))

#print(steve.get("candies", "No Candy list"))

#Can change value
#steve['name'] = "Joe"
#print(steve["name"])

#To print invididual values in list
#print(steve["foods"][1]) will print 2nd value in list

#To print value in dictionary nested in dictionary
#Syntax is print(big_dictionary[key of big_dictionary][key of small_dictionary])

#If key is not found, it will cause error
#To prevent, use print(steve.get("...")) and will print none
#Or, use for example print(steve.get("candies", "No Candy List"))
#Which will print the 2nd string of text

#Can update with .update function
#steve.update({"candies": ["snickers", "mars", "m&ms"]})

#To delete use del function

#favorite_languages = {
#    'jen': 'python',
#    'sarah': 'c',
#    'edward' : 'ruby',
#    'phil' : 'python',
#}

#friends = ['phil', 'sarah']
#for name in favorite_languages.keys():
#    print(name.title())
#    if name in friends:
#        print(" Hi " + name.title() + ", I see your favorite language is" +
#        favorite_languages[name].title() + "!")

# to go through in order, use the sorted() function
#for name in sorted(favorite_languages.keys()):
#    print(name.title())
#        print(" Hi " + name.title() + ", I see your favorite language is" +
#        favorite_languages[name].title() + "!")

#Looping through all the values in a dictionary
#print("The following languages have been mentioned:")
#for language in set(favorite_languages.values()):
#    print(language.title())

#set() funciton will build a list only from the unique items,
#eliminating the duplicate items

# Nesting
#Empty list to store aliens
#liens = []
#30 aliens
#for alien_number in range(30):
#    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
#    aliens.append(new_alien)
#to change first 3 aliens
#for alien in aliens[:3]:
#    if alien['color'] == 'green':
#        alien['color'] = 'yellow'
#        alien['speed'] = 'medium'
#        alien['points'] = 10
#Show first 5 aliens
#for alien in aliens[:5]:
#    print(alien)
#print("...")
#print("Total number of aliens: " + str(len(aliens)))

my_dict = {
    "name": "Troy",
    "position" : "QB",
    "team" : "Dallas Cowboys",
    "age" : 54,
    "weight" : 220,
    "superbowls" : ["XXVII", "XXVIII", "XXX"],
    "awards" : {
        "super_bowl_mvp" : "XXVII",
        "probowl" : [1991, 1992, 1993, 1994, 1995, 1996],
        "man_of_the_year" : 1997
    }
 }
print(my_dict.get("awards", "age")["probowl"][len(my_dict["position"])])