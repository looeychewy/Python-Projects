def main():

    list = ['a','b','c','d','e','f']
    list_a = []

    for i in range(len(list) - 1, -1, -1):
        list_a.append(list[i]) # Append item at index, working backwards

    print(list_a)


def pointer_swap():
    list = ['a','b','c','d','e','f']

    left = 0
    right = len(list) - 1

    while left < right: # first loop:
        temp_var = list[left] # first element of list, which is 'a'
        list[left] = list[right] # og first element gets replaced w/ 5th item (e)
        list[right] = temp_var # og 5th element gets replaced with 'a', held in temp_var

        left += 1
        right -= 1

        # Temp variable approach, working towards the middle with pointers
    print(list)

def longest_common_prefix(word_list):
    ''' Write function to find longest common prefix amongst array of strings.
    If no common prefix exists, return an empty string'''

    # list_strs -> input of list of strings (["flower", "flight", "flow"])


    #TODO: find first common letter between string elements

    prefix = ""

    # for i in word_list: # for each element in the word_list
    #     newword = word_list[i]

    # for word in word_list :
    #     print(" ")
    #     for letter in word: # for each letter in given word
    #         print(letter)

    # word = word_list[0]

    # find length of longest word in a given list, and iterate off of that?
    # What about how to preventing IndexErrors?
    # (start: stop: step) -> would js be range(len(word_list)) -> range(3)

    # implement if-else somewhere?? -> check for if input is blank (blank condition here), else if there is something, run the try except suite
    max_word_len = max(len(word) for word in word_list)
    for n in range(len(word_list), max_word_len ): # range(len(word_list)) imperfect, stops at 3 given list of 3 "flower"
        some_list = [word[n] for word in word_list]
        # print(some_list)
        # try:
        #     some_list = [word[n] for word in word_list] # word[n] = letter
        #     if len(set(some_list)) == 1:
        #         prefix = prefix + some_list[n]
        # except IndexError:
        #     print("blank")

        print(set(some_list), prefix) # myset = {"apple", "banana", "cherry"}

    print(prefix)

    # if len(set here) == 1 -> hblbljhb

def long_word(word_list):

    word_len = max(len(word) for word in word_list) # for word in word_list, find how long each object is, and take the highest value
    print(word_len)

if __name__ == "__main__":
    longest_common_prefix(["flower", "flower", "flower"])
    # long_word(["flower", "flower", "flower"])




