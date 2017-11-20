# Algorithm Class
# binarySearch() finds and returns an item in an ordered list in O(logn) time.
# mergeSort() sorts an unordered list in O(nlogn) time.
# quickSort() is randomized, so it sorts an unordered list in O(nlogn) average time.

from random import randint
from random import sample

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
            n = 0
            m = 0
            lenL = len(lList)
            lenR = len(rList)
            while n+m < len(unorderedList):
                if m == lenR or n < lenL and m < lenR  and lList[n] < rList[m]:
                    unorderedList[n+m] = lList[n]
                    n += 1
                else:
                    unorderedList[n+m] = rList[m]
                    m += 1
        return unorderedList

    def quick_sort(self, a_list):
        self.quick_helper(a_list, 0, len(a_list)-1)

    def quick_helper(self, a_list, start, end):
        if end-start > 0:
            pivot = self.partition(a_list, start, end)
            self.quick_helper(a_list, start, pivot-1)
            self.quick_helper(a_list, pivot+1, end)

    def partition(self, a_list, start, end):
        pivot = randint(start,end)
        a_list[pivot], a_list[start] = a_list[start], a_list[pivot]
        pivot = start
        p = a_list[pivot]
        m = start+1
        n = end
        while m < n:
            a = a_list[m]
            b = a_list[n]
            if a > p and b < p:
                a_list[n], a_list[m] = a_list[m], a_list[n]
                n -= 1
            elif a < p and b > p:
                n -= 1
            elif a > p and b > p:
                n -= 1
            else:
                m += 1
        if a_list[n] < p:
            a_list[pivot], a_list[n] = a_list[n], a_list[pivot]
            pivot = n
        return pivot



alg = Algorithms()
answer = [0,1,2,3,4,5,6,7,8,9]
for i in range(0, 100):
    my_list = sample(range(0,10), 10)
    original = my_list
    alg.quick_sort(my_list)
    if my_list != answer:
        print(original)
        print(my_list)







