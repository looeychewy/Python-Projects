# Justin Liu
# INF308 Assignment 10
# November 2, 2025



'''
Basic Grocery Store admin program
Introduce program to user, print store "directory" of items 
Present user with the following menu options:
   1. Add an Item
   2. Remove an Item
   3. Sort Items A-Z
   4. View List
'''

# storeItms = "directory" of items available in store, changeable
# itemName = specific item identifier
class storeDirectory:
    def __init__(self, storeItms = None):
        self.storeItms = storeItms or ["Simply Orange Juice", "Organic Bananas",
                                       "Snapdragon Apples"]

    def addItm(self, itemName):
        self.storeItms.append(itemName)
        print(itemName, "successfully added to directory!")

    def removeItm(self, itemName):
        if itemName in self.storeItms:
            self.storeItms.remove(itemName)
            print (itemName, "successfully removed!")
            return itemName
        else:
            print("Item not found or already removed")

    def sortItms(self): # Sorts directory alphabetically and prints it
        self.storeItms.sort()
        print("Here is the sorted directory: ")
        for item in self.storeItms:
                print (f" - {item}")

    def viewItms(self):
        print("\nHere is the full directory: ")
        for item in self.storeItms:
                print (f" - {item}")




# New directory object initialized
newDirectory = storeDirectory()

print ("Welcome to the Homegrown Grocers Sales Associate program!")
userInput = input("A new shipment was recently RECEIVED to the store. Would you like to access the store directory? [yes/no]: ").lower()

if userInput == "yes" or userInput == "y":
    print("\nGreat!")
    newDirectory.viewItms()

    done = False
    while done == False:
        
        appOptions = ["Add an Item", "Remove an Item", "Sort Items A-Z", "View List"]
        
        print("\nSome items may or may not have been entered into the system, while others may be too damaged to put onto the salesfloor.")

        print("AVAILABLE MENU OPTIONS: ")
        for i, item in enumerate(appOptions, start=1): # Enumerate prints a numerical list vertically
            print(f"{i}. {item}")
        userChoice = input("\nEnter menu option (1-4), or q to quit: ")


        if userChoice == "1":
            newItem = input("Enter the name of item to be added: ")
            newDirectory.addItm(newItem)
            
        elif userChoice == "2":
            newItem = input("Enter the name of item to be removed: ")
            newDirectory.removeItm(newItem)
            
        elif userChoice == "3":
            newDirectory.sortItms()
            
        elif userChoice == "4":
            newDirectory.viewItms()
            
        elif userChoice == "q":
            print ("Program terminated.")
            break
else:
    print("Program terminated.")
