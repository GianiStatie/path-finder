extends Node

onready var graph = get_node("Graph")
onready var brain = get_node("Brain")
export(NodePath) onready var maze = get_node(maze) as TemplateMaze

func _on_Maze_updated():
	graph.maze = maze
	graph._add_nodes()
	graph._connect_nodes()
	var path = brain.get_node_path()
	maze.draw_path(path)
