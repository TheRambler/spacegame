import datetime

def init(r):
	r.tasks_index={}

def add_group(root, tag):
	if not tag in root.tasks_index:
		root.tasks_index[tag]=[]

def add_task(root, tag, task):
	if not tag in root.tasks_index:
		root.tasks_index[tag]=[]
	root.tasks_index[tag].append(task)

def run_group(root, tag):
	for i in root.tasks_index[tag]:
		i.update(root)
		if i.delete:
			del root.tasks_index[tag][root.tasks_index[tag].index(i)]

class Task:
	def __init__(self, update, duration, data=None):
		self._update=update
		self.duration=duration
		self.start=datetime.datetime.now()
		self.data=data
		self.timeout=datetime.timedelta(seconds=duration)
		self.delete=False

	def update(self, root):
		self._update(self, root)
		if datetime.datetime.now()-self.start>self.timeout:
			self.delete=True