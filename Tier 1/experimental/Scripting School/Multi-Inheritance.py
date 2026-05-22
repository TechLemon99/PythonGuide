class Bird:
	def fly(self):
		print("I can fly!")
		
class Horse:
	def run(self):
		print("I can run!")
		
class Pegasus(Bird, Horse):
	def do_both(self):
	    print("I can fly and run!")

pegasus = Pegasus()
pegasus.fly()
pegasus.run()
pegasus.do_both()