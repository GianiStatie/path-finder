extends Node2D

# TileMap autotiles
const coordinates = {
	'N': 1, 
	'E': 2,
	'S': 4,
	'W': 8
}
const top_margin = 1
const bottom_margin = 2

const road_connections = {
	Vector2(0,  1): coordinates.N, Vector2(-1, 0): coordinates.E,
	Vector2(0, -1): coordinates.S, Vector2( 1, 0): coordinates.W
}

# Pathfinding algorithm variables
var starting_point
var ending_point
var algo
var final_path

# Changeable variables
var diagonal = 20
var num_obstacles = 5
var size_obastacles = 5

onready var Map = $MapTemplate

func _ready():
	algo = AStar.new()
	reset_tile_map()

func _physics_process(_delta):
	if Input.is_action_just_pressed("ui_select"):
		reset_tile_map()

func reset_tile_map():
	_init_map()
	_init_algo()
	_init_start_end_points()
	compute_final_path()
	draw_final_path()

func _coordinate_sum():
	return coordinates.N|coordinates.E|coordinates.S|coordinates.W

func _init_map():
	for y in range(diagonal / 2):
		for x in range(diagonal - (2 * y)):
			Map.set_cell(x + y, y, 15)
			# ignore second pass over diagonal
			if y != 0: Map.set_cell(x + y, -y, 15)

func _init_algo(): 
	for y in range(diagonal / 2):
		var length = diagonal - (2 * y)
		for x in range(length):
			if top_margin <= x and x <= (length - bottom_margin):
				var current_id = algo.get_available_point_id()
				algo.add_point(current_id, Vector3(x + y, y, 0))
				if x > top_margin:
					algo.connect_points(current_id, algo.get_closest_point(Vector3(x + y - 1, y, 0)))

				if y != 0:
					algo.connect_points(current_id, algo.get_closest_point(Vector3(x + y, y - 1, 0)))
					current_id = algo.get_available_point_id()
					algo.add_point(current_id, Vector3(x + y, -y, 0))
					algo.connect_points(current_id, algo.get_closest_point(Vector3(x + y, -y + 1, 0)))
					if x > top_margin:
						algo.connect_points(current_id, algo.get_closest_point(Vector3(x + y - 1, -y, 0)))

func _init_start_end_points(random_seed=null):
	if not random_seed:
		randomize()
	
	var height = diagonal / 2
	var starting_point_offset = (randi() % (height - (top_margin + bottom_margin))) + top_margin
	var ending_point_offset = (randi() % (height - (top_margin + bottom_margin))) + top_margin
	
	starting_point = Vector2(starting_point_offset, starting_point_offset)
	ending_point = Vector2((diagonal-1) - ending_point_offset, -ending_point_offset)
	
	Map.set_cellv(starting_point, 17)
	Map.set_cellv(ending_point, 17)

func compute_final_path():
	var starting_id = algo.get_closest_point(Vector3(starting_point.x, starting_point.y, 0))
	var ending_id = algo.get_closest_point(Vector3(ending_point.x, ending_point.y, 0))
	final_path = algo.get_point_path(starting_id, ending_id)

func draw_final_path():
	for tile in final_path:
		Map.set_cell(tile.x, tile.y, 17)
		yield(get_tree(), "idle_frame")
	
	for tile in final_path:
		var current_tile = _coordinate_sum()
		for dir in road_connections:
			if Map.get_cellv(Vector2(tile.x, tile.y) + dir) != _coordinate_sum():
				if Map.get_cellv(Vector2(tile.x, tile.y) + dir) != 16:
					current_tile -= road_connections[dir]
		Map.set_cellv(Vector2(tile.x, tile.y), current_tile)

