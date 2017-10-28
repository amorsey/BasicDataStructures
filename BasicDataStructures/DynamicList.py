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
            self.end = (self.end+1)%self.listLen
            self.myList[self.end] = data
            self.eleNum += 1

    def pop(self):
        if self.eleNum == 0:
            print("ERROR: No elements in list")
        else:
            temp = self.start
            self.start = (self.start+1)%self.listLen
            self.eleNum -= 1
            return myList[temp]

    def __str__(self):
        s = "{"
        p = self.start
        for i in range(self.listLen):
            s = s + str(self.myList[p]) +","
            p = (p+1)%self.listLen
        s += "}"
        return s


l = DynamicList()
l.push(4)
l.push(2)
l.push(1)
l.push(3)
l.push(5)
print(l)
print(l.pop())
