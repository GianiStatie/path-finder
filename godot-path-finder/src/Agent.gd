extends Node

var path = []
var ready = false

onready var graph = get_node("Graph")
onready var brain = get_node("Brain")

func _ready():
	ready = true

func set_maze(maze):
	while not ready:
		yield(get_tree(),"idle_frame")
	graph.maze = maze
	graph._add_nodes()
	graph._connect_nodes()

func set_algorithm(algorithm):
	brain.set_script(Constants.algorithm_paths[algorithm])
	brain.graph = graph
	path = brain.get_node_path()
