extends Node

var path = []
var seen_nodes = []
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
	seen_nodes = brain.seen_nodes

func get_path(open_interval=false):
	if open_interval:
		var path_copy = path
		return _remove_start_end_nodes(path_copy)
	return path

func get_seen_nodes(open_interval=false):
	if open_interval:
		var seen_nodes_copy = seen_nodes
		return _remove_start_end_nodes(seen_nodes_copy)
	return seen_nodes

func _remove_start_end_nodes(node_list):
	for node in [brain.start_node_position, brain.end_node_position]:
		if node in node_list:
			node_list.erase(node)
	return node_list
