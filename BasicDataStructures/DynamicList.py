class DynamicList:
    def __init__(self):
        self.myList = [None]
        self.listLen = 1
        self.start = self.end = 0
        self.eleNum = 0

    def push(self, data):
        if self.eleNum == self.listLen:
            newList = [None]*(self.listLen*2)
            p = self.start
            for i in range(self.eleNum):
                newList[i] = self.myList[p]
                p = (p+1)%self.listLen
            newList[self.eleNum] = data
            self.myList = newList
            self.listLen *= 2
            self.eleNum += 1
            self.end = self.eleNum-1
            self.start = 0
        else:
            self.end = (self.end+1)%self.listLen
            self.myList[self.end] = data
            self.eleNum += 1

    def pop(self):
        if self.eleNum == 0:
            return None
        else:
            temp = self.start
            self.start = (self.start+1)%self.listLen
            self.eleNum -= 1
            return self.myList[temp]

    def __str__(self):
        s = "["
        p = self.start
        for i in range(self.eleNum):
            s = s + str(self.myList[p])+","
            p = (p+1)%self.listLen
        s += "]"
        return s


l = DynamicList()
l.push(1)
l.push(2)
l.push(3)
l.push(4)
l.push(5)
l.push(6)
l.push(7)
print(l)
l.pop()
l.pop()
l.pop()
print(l)
l.push(8)
l.push(9)
l.pop()
l.pop()
l.pop()
print(l)
l.push(10)
l.push(11)
l.push(12)
l.push(13)
l.push(14)
l.push(15)
l.push(16)
l.push(17)
l.push(18)
print(l)




