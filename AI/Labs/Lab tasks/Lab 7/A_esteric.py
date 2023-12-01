import heapq

class WeightedGraph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, start, end, cost):
        if start not in self.graph:
            self.graph[start] = []
        self.graph[start].append((end, cost))

    def astar(self, start, goal, heuristic):
        priority_queue = [(0 + heuristic(start, goal), 0, start, [])]

        while priority_queue:
            _, current_cost, current_node, path = heapq.heappop(priority_queue)

            if current_node == goal:
                return path + [current_node]

            for neighbor, cost in self.graph.get(current_node, []):
                heapq.heappush(priority_queue, (current_cost + cost + heuristic(neighbor, goal),
                                                current_cost + cost,
                                                neighbor,
                                                path + [current_node]))

        return None  # No path found

# Example usage
if __name__ == "__main__":
    # Create a weighted graph
    g = WeightedGraph()

    g.add_edge('A', 'B', 5)
    g.add_edge('A', 'C', 3)
    g.add_edge('B', 'C', 2)
    g.add_edge('B', 'D', 4)
    g.add_edge('C', 'D', 6)

    # Define a heuristic function (Euclidean distance for demonstration)
    def euclidean_distance(node, goal):
        return 0  # Replace with actual heuristic calculation

    # Run A* Search algorithm
    start_node = 'A'
    goal_node = 'D'
    path = g.astar(start_node, goal_node, euclidean_distance)

    if path:
        print(f"A* Path from {start_node} to {goal_node}: {path}")
    else:
        print(f"No A* Path found from {start_node} to {goal_node}")
