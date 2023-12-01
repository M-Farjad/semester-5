import queue


class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, weight):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, weight))

    def get_neighbors(self, node):
        return self.graph.get(node, [])

def priority_queue_for_graph(graph):
    pq = queue.PriorityQueue()
    pq.put(('A', 0))  # Starting node and its priority

    while not pq.empty():
        current_node, current_priority = pq.get()
        print(f"Processing {current_node} with priority {current_priority}")

        for neighbor, weight in graph.get_neighbors(current_node):
            next_priority = current_priority + weight
            pq.put((neighbor, next_priority))

# main program
# Create the weighted graph

g = WeightedGraph()

g.add_edge('A', 'B', 5)
g.add_edge('A', 'C', 3)

g.add_edge('B', 'C', 2)

g.add_edge('B', 'D', 4)

g.add_edge('C', 'D', 6)

# Use a priority queue to process the nodes
priority_queue_for_graph(g)
