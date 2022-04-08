extends Node2D

onready var agent = get_node("Agent")
onready var maze = get_node("Maze")

var is_ready = false

func _ready():
	is_ready = true

func _on_Maze_map_initialized():
	while not is_ready:
		yield(get_tree(),"idle_frame")
	agent.maze = maze
	agent.calculte_path()
	maze.draw_path(agent.path, true)
