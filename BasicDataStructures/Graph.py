class Graph:
    def __init__(self):
        self.adjacent = {}

    def add(self, data, children):
        self.adjacent[data] = children

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
my_graph.add('D',['E','G','H'])
my_graph.add('E',['D','F'])
my_graph.add('F',['E','G'])
my_graph.add('G',['D','F'])
my_graph.add('H',['D'])
print(my_graph)
