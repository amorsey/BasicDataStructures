class DynamicList:
    def __init__(self):
        self.myList = [None, None, None, None, None]
        self.listLen = len(myList)
        self.start = self.end = 0
        self.eleNum = 0

    def push(self, data):
        if self.eleNum == self.listLen:
            print("ERROR: List to large")
        self.end = (self.end + 1)%self.listLen



    def pop(self):


