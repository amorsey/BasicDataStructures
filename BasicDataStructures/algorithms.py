# Binary Search class
# Finds and returns an item in an ordered list in O(log(n)) time.

class Algorithms:
    def binarySearch(self, orderedList, desiredElement):
        searchSpace = len(orderedList)//2
        guess = searchSpace

        while searchSpace > 0:
            #print(searchSpace)
            value = orderedList[guess]
            searchSpace = searchSpace//2
            if value == desiredElement:
                return value
            elif value < desiredElement:
                guess += searchSpace
            else:
                guess -= searchSpace

            #print(guess)
            #print(searchSpace)
            print(value)


myList = [1, 4, 5, 6, 11, 13, 15, 16, 17, 22, 31]
alg = Algorithms()
print(alg.binarySearch(myList, 17))
