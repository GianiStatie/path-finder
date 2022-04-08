extends Node

var path = []
var ready = false
var algorithm = 'dijkstra'

onready var graph = get_node("Graph")
onready var brain = get_node("Brain")

export(NodePath) onready var maze = get_node(maze)

func _ready():
	ready = true

func calculte_path():
	while not ready:
		yield(get_tree(),"idle_frame")
	graph.maze = maze
	graph._add_nodes()
	graph._connect_nodes()
	_update_brain_algorithm()

func _update_brain_algorithm():
	brain.set_script(Constants.algorithm_paths[algorithm])
	brain.graph = graph
	path = brain.get_node_path()
