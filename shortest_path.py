import json
from functools import reduce

import matplotlib.pyplot as plt


class QuickWayFinder(object):

    def __init__(self, node1, node2):
        self.node1 = node1
        self.node2 = node2
        self.node_coordinates = None
        self.node_names = None
        self.weights_node_coordinates = None
        self.node_paths = None
        self.process_json()
        self.prepare_coordinates()
        self.highlight_the_shortest_path()

    def process_json(self):
        with open(r"shortest_path.json") as json_file:
            data = json.load(json_file)
            self.node_coordinates = data["node_coordinates"]
            self.node_names = data["node_names"]
            self.weights_node_coordinates = data["weights_node_coordinates"]
            self.node_paths = data["node_paths"]

    def prepare_coordinates(self):
        xCoord = [int(self.node_coordinates[k][0]) for k in sorted(self.node_coordinates)]
        yCoord = [int(self.node_coordinates[k][1]) for k in sorted(self.node_coordinates)]
        plt.plot(xCoord, yCoord, 'bo')
        plt.axis([-1, 7, -1, 9])
        for i in range(8):
            plt.text(xCoord[i] - 0.5, yCoord[i], self.node_names[str(i + 1)])
        for i in range(8):
            for j in range(8):
                if self.weights_node_coordinates[i][j]:
                    plt.plot([xCoord[i], xCoord[j]], [yCoord[i], yCoord[j]], 'b')

    def get_the_quickest_path(self):
        traversed_path, distance = self.find_shortest_path(self.node_paths, self.node1, self.node2)
        print(f"The traversed path is {traversed_path}")
        print(f"The total weight along the traversed path {distance}")
        return traversed_path

    def highlight_the_shortest_path(self):
        traversed_path = self.get_the_quickest_path()
        # Drawing of coordinates
        mydrawing = traversed_path.split('-> ')
        plt.plot([int(self.node_coordinates[n.rstrip()][0]) for n in mydrawing],
                 [int(self.node_coordinates[n.rstrip()][1]) for n in mydrawing], color="red")
        plt.show()

    def find_shortest_path(self, graph, start, target):
        inf = reduce(lambda x, y: x + y, (i[1] for u in graph for i in graph[u]))
        dist = dict.fromkeys(graph, inf)
        prev = dict.fromkeys(graph)
        q = list(graph.keys())
        dist[start] = 0
        while q:
            u = min(q, key=lambda x: dist[x])
            q.remove(u)
            for v, w in graph[u]:
                alt = dist[u] + w
                if alt < dist[v]:
                    dist[v] = alt
                    prev[v] = u

        trav = []
        temp = target
        while temp != start:
            trav.append(prev[temp])
            temp = prev[temp]
        trav.reverse()
        trav.append(target)
        return " -> ".join(trav), dist[target]


if __name__ == '__main__':
    quick_way_finder = QuickWayFinder('F', 'H')
