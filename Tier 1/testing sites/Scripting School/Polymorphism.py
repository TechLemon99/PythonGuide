class Food:
	def identify(self):
		print("This is a food")
		
class Apple(Food):
	def identify(self):
		print("This is an apple")
		
greenapple = Apple()
greenapple.identify()