class Item():
	def __init__(self):
		self.name  = None
		self.description = None

	def set_name(self,name):
		self.name = name
	def set_description(self,description):
		self.description = description
	def get_name(self):
		return self.set_name
	def get_description(self):
		print( self.set_description)

	def describe(self):
		print( self.description  )

	def take(self):
		
		backpack.append(self.name)	
		print(backpack)
