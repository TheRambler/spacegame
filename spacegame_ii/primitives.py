
def init(root):
	if not 'primitives' in dir(root):
		root.primitives_list={}

def register_primitive(root, name, primitive):
	root.primitives_list[name]=primitive

def run_primitive(root, name, data, parent):
	if name in root.primitives_list:
		r= root.primitives_list[name](root, data, parent)
		if not r:
			print "WARNING: PRIMITIVE '"+name+"' FAILED (Called from "+str(parent)+") [TERMINATES PRIMITIVE CHAIN]"
		return r
	else:
		print "WARNING: PRIMITIVE '"+name+"' NOT DEFINED (Called from "+str(parent)+") [TERMINATES PRIMITIVE CHAIN]"
		return False