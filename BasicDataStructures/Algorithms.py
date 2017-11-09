# Algorithm Class
# binarySearch() finds and returns an item in an ordered list in O(logn) time.
# mergeSort() sorts an unordered list in O(nlogn) time.

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
            lList = self.mergeSort(unorderedList[:mid])
            rList = self.mergeSort(unorderedList[mid:])

            # Merge left and right list into unorderedlist
            n = 0
            m = 0
            lenL = len(lList)
            lenR = len(rList)

            while n+m < len(unorderedList):
                if m == lenR or n < lenL and m < lenR and lList[n] < rList[m]:
                    unorderedList[n+m] = lList[n]
                    n += 1
                else:
                    unorderedList[n+m] = rList[m]
                    m += 1

        return unorderedList






myList = [4, 5, 3, 3, 1]
alg = Algorithms()
print(alg.mergeSort(myList))







