extends Node

onready var graph = get_node("Graph")

func _on_Maze_updated():
	graph._add_nodes()
	graph._connect_nodes()
