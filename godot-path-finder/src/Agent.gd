extends Node

var algorithm_paths = {
	'dfs': load("res://src/path_finders/DFSPathFinder.gd"),
	'bfs': load("res://src/path_finders/BFSPathFinder.gd"),
	'dijkstra': load("res://src/path_finders/DijkstraPathFinder.gd")
}

var path = []
var ready = false

onready var graph = get_node("Graph")
onready var brain = get_node("Brain")

export(NodePath) onready var maze = get_node(maze)
export(String, 'dfs', 'bfs', 'dijkstra') var algorithm = 'dijkstra' setget set_algorithm

func _ready():
	ready = true

func _on_Maze_updated():
	graph.maze = maze
	graph._add_nodes()
	graph._connect_nodes()
	
	_update_brain_algorithm(algorithm)
	maze.draw_path(path, true)

func _update_brain_algorithm(algorithm):
	brain.set_script(algorithm_paths[algorithm])
	brain.graph = graph
	path = brain.get_node_path()

func set_algorithm(algorithm):
	if ready:
		_update_brain_algorithm(algorithm)
		maze.draw_path(path, true)
