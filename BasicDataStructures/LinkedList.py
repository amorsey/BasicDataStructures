#Linked list class

#Node object
class Node:
	def __init__(self, initData):
		self.data = initData
		self.next = None

#List class
class LinkedList:
	def __init__(self):
		self.head = None

	def append(self, data):
		newNode = Node(data)

		if self.head is None:
			self.head = newNode
		else:
			newNode.next = self.head
			self.head = newNode

	def search(self, k):
		p = self.head

		while p is not None:
			if p.data is k:
				return p
			p = p.next
		return None

	def pop(self):
		if self.head is not None:
			temp = self.head
			self.head = self.head.next
			return temp.data


	def __str__(self):
		s = ""
		p = self.head
		while p is not None:
			s += p.data
			p = p.next
		return s

myList = LinkedList()
myList.append('d')
myList.append('a')
myList.append('b')
myList.append('c')
print(myList)
myList.pop()
myList.pop()
myList.pop()
myList.pop()
myList.pop()




#print(myList.pop())
#print(myList.pop())
#print(myList.pop())


