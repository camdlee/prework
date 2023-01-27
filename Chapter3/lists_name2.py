### ORGANIZING LISTS ###
#cars = ['audi', 'toyota', 'honda']

#Use sort() to sort through list and alphabetize it permanently
    #cars.sort()
    #print(cars)
#cars.sort(reverse=True) will alphabetize it in the opposite order

#Use sorted() function to temporarily sort list without affecting original list
    #print("Here is the original list:")
    #print(cars)
    #print("\nHere is the sorted list:")
    #print(sorted(cars))

#Use .reverse() function to reverse order of list permanently
    #cars.reverse()
    #print(cars)

#Use len() function to find the length of a list
    #len(cars)
    #print(len(cars))


### EXERCISE ###
#places = ['Tokyo', 'Seattle', 'Vancouver', 'Sydney', 'Singapore']
#print(places)
#print(sorted(places))
#print(sorted(places, reverse = True))
#print(places)
#places.reverse()
#print(places)
#places.reverse()
#print(places)
#places.sort()
#print(places)
#places.sort(reverse = True)
#print(places)
#print(len(places))


my_list = [1, 3.0, ["a", "b", ["A", "B", "C"], "d", "John"]]
#print(my_list[2][2][0])
#[2][2][0] means that it will grab the 3rd value in the outer list, the 3rd value in the mid list
#then the 1st value in the inner list

for member in my_list:
    if isinstance(member, list):
        for m in member:
            if isinstance(m, list):
                print(m, end=" ")
#isinstance checks if value in list is the type that follows the text, so
# if 'member' of the outer list is a list type, then it goes to the next function