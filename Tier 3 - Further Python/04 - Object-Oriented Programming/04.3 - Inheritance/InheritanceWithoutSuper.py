class Bird:
    def fly(self):
        print("Bird is flying!")

class Penguin(Bird):
    pass

maurice = Penguin()
maurice.fly()