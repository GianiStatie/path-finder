extends CanvasLayer

onready var algorithm_option_button = get_node("OptionButton")

var algo_names = Constants.algorithm_paths.keys()

signal updated_algorithm(algorithm_name)

func _ready():
	for algo_idx in range(len(algo_names)):
		var algo_name = algo_names[algo_idx]
		algorithm_option_button.add_item(algo_name, algo_idx)
	emit_signal('updated_algorithm', algo_names[0])

func _on_OptionButton_item_selected(index):
	emit_signal('updated_algorithm', algo_names[index])
