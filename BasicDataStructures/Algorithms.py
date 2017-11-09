# Binary Search class
# Finds and returns an item in an ordered list in O(log(n)) time.

class Algorithms:
    def binarySearch(self, orderedList, desiredElement):
        startSS = 0
        endSS = len(orderedList)-1

        while endSS-startSS >= 0:
            guess = startSS+(endSS-startSS+1)//2
            value = orderedList[guess]

            if value == desiredElement:
                return guess
            elif value < desiredElement:
                startSS = guess+1
            else:
                endSS = guess-1

    def mergeSort(self, unorderedList):
        mid = len(unorderedList)//2

        if mid != 0:
            lList = self.mergeSort(mid:)
            rList = self.mergeSort(:mid)
            return merge(lList, rList)

        return unorderedList






myList = [1, 4, 5, 6, 11, 13, 15, 16, 17, 22, 31]
alg = Algorithms()
print(myList[:4])







