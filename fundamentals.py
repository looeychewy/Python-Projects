# CS50 Work/Python Fundamentals Reteach


# Python Exercises (Retraining Brain): https://pynative.com/python-basic-exercise-for-beginners/


''' Exercise 1: Write a FUNCTION that accepts two int numbers. If product of the two numbers is <= 100, return product, else return their sum

def numCalculator(num1, num2):
    numProduct = num1*num2
    if (numProduct <= 1000):
        return (numProduct) # Return can only be used within a function 
    else:
        return (num1+num2)
    
def main():
    print("Test Case 1: ", numCalculator(20, 30))
    print ("Test Case 2: ", numCalculator(40,30)) # Function name not defined?

main()


'''


''' # Exercise 2: Iterate through the first 10 numbers (0-9). In each iteration, print current number, previous, and their sum


    for i in range (10): # My Solution
    if i ==0:
        prevNum = 0
    else:
        prevNum = i-1
    print("Current number:", i, "Previous number:", prevNum, "Sum:", i+prevNum)
    
    prevNum = 0 # Official Solution
    for i in range(10):
    x_sum = prevNum + i
    print(f"Current Number {i} Previous Number {prevNum} Sum {x_sum}")

    prevNum = i
    '''

'''# Exercise 3: Display only those characters which are present at an even index number in a given string

# Find number of characters in a string -> len()
# Find character at a given index? -> indexing, square brackets
# Determine even index

strInput = input("Please enter a string: ")
strLen = len(strInput)

char = 0
for char in range(0, strLen-1, 2): #Step by 2 function -> first value is where to begin, second is where to end, third is how many steps
    print(strInput[char], char) 
    
'''

'''# Exercise 4: Write a function to remove characters from a given string with a given number n , starting from
# index 0 to n, and return a new string (str) -> taking a while, postpone

#def remove_chars(input, numChars):

final_string = ""

strInput = input("Enter the string to modify: ") 

numChars = int(input("How many characters to remove?: "))



print(numChars)
 #.index returns index num of given value, but how do we reverse it '''

#-----------------------------------------------------------------------------------------------------------------------

'''# Leetcode 1: Two Sum (Easy)
Given an array of integers nums and an integer target, return indices of the two numbers in a list such that they add up to target. 
    - Indices: index values of numbers in an array
    - Target: Target value
    - Trying to return indices of two numbers in an array that would add up to the target value

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.




class Solution(object):
    def twoSum(self, nums, target): #Self parameter? - Refers to specfic instance of the class on which object is called
        
        Solution 1 (47/63 Test Cases), checks for adjacent values only
        i=0
        for i in range(len(nums)-1): #len(nums) = 4, range of 4 = 0,1,2,3, ends before reaching end of list
            num1 = nums[i] #Returns value of nums at i index
            num2 = nums[i+1] #Returns value of nums at the next i index
            sum = num1+num2
            if (sum==target): 
                indice1 = nums.index(num1, 0, len(nums))
                indice2 = nums.index(num2, indice1, len(nums)) #.index() returns the first found instance of the variable, but what if there's dupes?
                if(indice2==indice1):
                    indice2 = nums.index(num2, indice1, len(nums)) + 1
                outList = [indice1, indice2]
                return outList # Return index of the array value
        

        # Solution 2: Use a hash map? Brush up on your data structures (what about non adjacent values)

        i=0
        for i in range(len(nums)-1): #len(nums) = 4, range of 4 = 0,1,2,3, ends before reaching end of list
            num1= nums[i]
            num2 = target - num1 #subtract num1 from target, assign to num2, search for value in list
            #logic still flawed as nums[0] is assigned to num1
            print(num2)
            if num2 in nums:
                print("Found: ", nums[i])
            else:
                print("Not found")

        
        # Workaround 1: Stack Overflow
        d={} #Initialize empty dictionary, holds {index,value} pairs
        for i, e in enumerate(nums): #enumerate gives (index,value) pairs for a list, I=INDEX, e=ELEMENT
            k = target - e #Set k(num2) to the difference between target and e(num1)
            if k in d: #If difference is in the empty dictionary
                return [d[k], i] #Return element found at index num2 in dictionary, index?
            d[e] = i #Set element at dictionary[num1] equal to index 

        # First iteration for case nums=[2,7,11,15], target = 9
            # i=0, e=2. 9-2 = 7. 7 is NOT in d (d is empty), set d[2] = 0 (d[key] = value -> d[element] = index)
        # Second iteration:
            # i=1, e=7. 9-7 = 2. 2 IS in d, so return d[2], i -> 0,1 (d[2] was set in the previous loop)
        


nums = [3,2,3] #0,1,2
target = 6 #Retrieve first value, num2 = target - x



newSol = Solution()
print(newSol.twoSum(nums,target))
'''

'''# Leetcode 2: Longest Common Prefix (HAVEN'T TRIED SELF YET)

Write a function to find the longest common prefix from an array of strings
If no common prefix, return empty string

Example:
    Input: strs = ["flower","flow","flight"]
    Output: "fl"

prefix = ""
'''



