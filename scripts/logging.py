from datetime import datetime
# from rich import print


class Logger:
	def __init__(self, name):
		self.name = name

	def log(self, *objects):
		text = ""
		for object in objects:
			text += str(object)		

		print("(" + datetime.now().strftime("%H:%M:%S") + ")" + "[" + self.name + "]: " + text) # TODO: Use format string

	def warning(self, *objects):
		text = ""
		for object in objects:
			text += str(object)

		print("[yellow](" + datetime.now.strftime("%H:%M-%S") + ")" + "[" + self.name + "]: " + text)  # TODO: Use format string

	def error(self, *objects):
		text = ""
		for object in objects:
			text += str(object)
		
		print("[red](" + datetime.now.strftime("%H:%M-%S") + ")" + "[" + self.name + "]: " + text)  # TODO: Use format string
		
