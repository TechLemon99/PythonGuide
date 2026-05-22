class Apple:
	def bite(self):
		print("Apple bitten")
		return self
	
	def chomp(self):
		print("Apple chomped")
		return self
	
	def eaten(self):
		print("Apple eaten")
		return self

yellowapple = Apple()
yellowapple.bite().chomp().bite().bite().eaten()