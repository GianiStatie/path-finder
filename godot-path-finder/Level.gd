extends Node2D

onready var agent = get_node("Agent")
onready var maze = get_node("Maze")

var is_ready = false
var is_maze_ready = false

func _ready():
	is_ready = true

func _on_Maze_map_initialized():
	while not is_ready:
		yield(get_tree(),"idle_frame")
	agent.set_maze(maze)
	is_maze_ready = true

func _on_UI_updated_algorithm(algorithm_name):
	while not is_maze_ready:
		yield(get_tree(),"idle_frame")
	agent.set_algorithm(algorithm_name)
	maze.reset_map()
	maze.draw_path(agent.path, true)
