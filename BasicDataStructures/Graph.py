from collections import deque


class Graph:
    def __init__(self):
        self.adjacent = {}

    def add(self, data, children):
        self.adjacent[data] = children

    def bfs(self, start):
        visited = {start}
        queue = deque([start])
        while len(queue) > 0:
            print(queue)
            node = queue.popleft()
            for child in self.adjacent[node]:
                if child not in visited:
                    visited.add(child)
                    queue.append(child)

    def dfs(self, start):
        visited = set()
        self.dfs_helper(visited, start)

    def dfs_helper(self, visited, parent):
        visited.add(parent)
        print(parent)
        for child in self.adjacent[parent]:
            if child not in visited:
                self.dfs_helper(visited, child)

    def __str__(self):
        s = ""
        for ele in self.adjacent:
            s += ele + ': '
            for child in self.adjacent[ele]:
                s += child + ", "
            s += "\n"
        return s

my_graph = Graph()
my_graph.add('A',['B'])
my_graph.add('B',['A','C','D'])
my_graph.add('C',['B','D'])
my_graph.add('D',['B','C','E','G','H'])
my_graph.add('E',['D','F'])
my_graph.add('F',['E','G'])
my_graph.add('G',['D','F'])
my_graph.add('H',['D'])
my_graph.dfs('E')
