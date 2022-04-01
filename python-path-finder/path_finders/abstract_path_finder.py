import sys
sys.path.append("..")

from constants import directions
from utils import add_vectors

class AbstractPathFinder:
    def __init__(self, obstacle_weight: int = 999):
        self.points = {}
        self.connections = {}
        self.start_id = None
        self.end_id = None
        self.obstacle_weight = obstacle_weight

    def add_point(self, id:int, position: list, weight_scale:float = 1.0):
        self.points[id] = {
            "position": position,
            "weight_scale": weight_scale
        }

    def connect_points(self, id: int, to_id: int, bidirectional: bool = True):
        self._add_connection(id, to_id)
        if bidirectional: self._add_connection(to_id, id)

    def get_point_path(self, from_id: int, to_id: int):
        raise NotImplementedError

    def _add_connection(self, id: int, to_id: int):
        if id not in self.connections:
            self.connections = []
        self.connections.append(to_id)

    def _get_position_weight(self, position: list):
        for pair in self.points.values():
            if pair['position'] == position:
                return pair['weight_scale']
        return self.obstacle_weight

    def _canceles_previous_move(self, move_sequence: str):
        if len(move_sequence) > 1:
            move_direction = add_vectors(
                directions[move_sequence[-1]], 
                directions[move_sequence[-2]])
            if move_direction == (0, 0):
                return True
        return False

    def _is_obstacle(self, position: list):
        return self._get_position_weight(position) == self.obstacle_weight

    def _walk_path(self, move_sequence: str):
        meta = {
            'is_end': False,
            'is_valid': False,
            'path': []
        }

        if self._canceles_previous_move(move_sequence):
            return meta

        current_position = self.points[self.start_id]['position']
        meta['path'].append(current_position)
        for direction in move_sequence:
            current_position = add_vectors(current_position, directions[direction])
            meta['path'].append(current_position)
            if self._is_obstacle(current_position):
                return meta
        
        meta['is_valid'] = True
        meta['is_end'] = current_position == self.points[self.end_id]['position']
        return meta

    