class DynamicList:
    def __init__(self):
        self.myList = [None, None, None, None, None]
        self.listLen = 5
        self.start = self.end = 0
        self.eleNum = 0

    def push(self, data):
        if self.eleNum == self.listLen:
            print("ERROR: List too large")
        else:
            self.myList[self.end] = data
            self.end = (self.end+1)%self.listLen
            self.eleNum += 1

    def pop(self):
        if self.eleNum == 0:
            print("ERROR: No elements in list")
        else:
            temp = self.start
            self.start = (self.start+1)%self.listLen
            self.eleNum -= 1
            return self.myList[temp]

    def __str__(self):
        s = "["
        p = self.start
        for i in range(self.eleNum):
            s = s + str(self.myList[p]) +","
            p = (p+1)%self.listLen
        s += "]"
        return s


l = DynamicList()
l.push(4)
print(l)
l.push(2)
print(l)
l.push(1)
print(l)
l.push(3)
print(l)
l.push(5)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
l.push(7)
l.push(8)
l.push(9)
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)
print(l.pop())
print(l)




