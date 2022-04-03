from src.constants import directions
from src.utils import add_vectors
from .abstract_path_finder import AbstractPathFinder

class DijkstraPathFinder(AbstractPathFinder):
    """ Subclass of AbstractPathFinder
    Finds the path using Dijkstra's search approach.

    """
    def __init__(self):
        super().__init__()
        self.default_distance = 1e7
        self.transition_cost = []
        self.transition_node = []

    def set_graph(self, graph):
        super().set_graph(graph)
        self.transition_cost = [self.default_distance] * len(self.graph.nodes)
        self.transition_node = [None] * len(self.graph.nodes)
        self.transition_cost[self.graph.start_node] = 0

    def get_node_path(self):
        """Finds a path from start_node to end_node using depth first search approach.

        Returns:
            path (list): A list containing node coordinates which form a path from start to end.
        """
        self._calculate_transitions()

        start_node = self.graph.start_node
        current_node = self.graph.end_node

        path = [self.graph.nodes[current_node]['position']]
        while current_node != start_node:
            current_node = self.transition_node[current_node]
            path.append(self.graph.nodes[current_node]['position'])

        return path[::-1]

    def _calculate_transitions(self):
        unvisited_nodes = list(self.graph.nodes.keys())

        while len(unvisited_nodes) > 0:
            current_node = self._get_minimum_cost_index(unvisited_nodes)
            if current_node == -1:
                break
            unvisited_nodes.remove(current_node)
            for connected_node in self._get_connected_nodes(current_node):
                connected_node_idx = self.graph.get_position_index(connected_node)
                connected_node_weight = self.graph.get_position_weight(connected_node)
                transition_cost = self.transition_cost[current_node] + connected_node_weight
                if self.transition_cost[connected_node_idx] > transition_cost:
                    self.transition_cost[connected_node_idx] = transition_cost
                    self.transition_node[connected_node_idx] = current_node

    def _get_connected_nodes(self, node_idx):
        connected_nodes = []
        current_position = self.graph.nodes[node_idx]['position']
        for move_vector in directions.values():
            next_position = add_vectors(current_position, move_vector)
            if self._is_valid_move(current_position, next_position) and \
                not self._is_obstacle(next_position):
                connected_nodes.append(next_position)
        return connected_nodes

    def _get_minimum_cost_index(self, unvisited_nodes):
        min_index = -1
        min_distance = self.default_distance
        for idx in unvisited_nodes: 
            if self.transition_cost[idx] < min_distance:
                min_distance = self.transition_cost[idx]
                min_index = idx
        return min_index
