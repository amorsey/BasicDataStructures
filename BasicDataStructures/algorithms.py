# Binary Search class
# Finds and returns an item in an ordered list in O(log(n)) time.

class algorithms:
    def __init__(self, orderedList, desiredElement):
        searchSpace = len(orderedList)/2
        sel.guess = searchSpace

        while searchSpace > 1:
            value = orderedList[guess]
            searchSpace = searchSpace/2
            if value == desiredElement:
                return guess
            elif value < desiredElement:
                guess += searchSpace
            else:
                guess -= searchSpace


myList = [1, 4, 5, 6, 11, 13, 15, 16, 17, 22, 31, 32]
mySearch = BinarySearch()
