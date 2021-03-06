import json

def init(root):
	root.load_modes={}
	#register_load_mode(root, "item", item._deserialize_item)

class SerializableObject:
	def save_to_config_node(self):
		return {}

def register_load_mode(root, load_type, load_function):
	root.load_modes[load_type]=load_function

def save_game(root, filename):
	with open(filename, 'w') as fd: #json.dumps(node, indent=4)
		pass #TODO: Finish 

def load_game(root, filename):
	with open(filename, 'r') as fd:
		pass #TODO: Finish

def save_object(item):
	assert isinstance(item, SerializableObject)
	return item.save_to_config_node()

def load_from_node(root, node, parent):
	return root.load_modes[node["__deserialize_handler__"]](root, node, parent)