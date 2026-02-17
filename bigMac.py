# Justin Liu, 2/16/26
# code me a big mac lil bro

# Big Mac, McNugget, Quarter Pounder, Coke -> List/array/hash map/dict. to store items?
# user input for specific food item
# print using hashes, for/while loops


# incorrect input checking
userInput = input(
    "What food item you tryna see big back [Big Mac, Quarter Pounder, McNugget, Coke]: ") # Food specific functions (ie bigMac(), quarterPounder(), etc.)

if userInput == "Big Mac":

    bmHeight = int(input("How tall would you like your Big Mac?: "))
    h = 0
    #s = bmHeight - 1 

    while h < bmHeight: 
        for w in range(0, bmHeight):  # Handles width
            print("#", end='')
        # for s in range (0, bmHeight - 1): -> Space testing
        print("#")
        h += 1


else:
    print("cool")


'''if userInput == "Big Mac":
    print("Big Mac\n###\n####\n####\n###")
else:
    print(foodDict["burger1"])'''
