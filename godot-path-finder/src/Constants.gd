extends Node

var START_CHAR = 'S'
var END_CHAR = 'E'
var EMPTY_CHAR = ' '
var OBSTACLE_CHAR = '#'

var directions = {
	'U': Vector2(0, -1),
	'D': Vector2(0, 1),
	'R': Vector2(-1, 0),
	'L': Vector2(1, 0),
}

var weight_mapping = {
	' ': 1.0,  # walkable path
	'S': 1.0,  # start node
	'E': 1.0,  # end node
	'H': 10.0, # hole (shallow obstacle)
	'#': 999.0 # wall (hard obstacle)
}

var tile_mapping = {
	" ": 15,
	"#": 16,
	"S": 17,
	"E": 17,
}

var algorithm_paths = {
	'dfs': load("res://src/path_finders/DFSPathFinder.gd"),
	'bfs': load("res://src/path_finders/BFSPathFinder.gd"),
	'dijkstra': load("res://src/path_finders/DijkstraPathFinder.gd")
}
