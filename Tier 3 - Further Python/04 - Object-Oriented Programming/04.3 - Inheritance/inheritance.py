class Parents:
    def walk(self):
        print("WALK")

class Child1(Parents):
    pass

class Child2(Parents):
    pass

child_1 = Child1()
child_2 = Child2()
child_1.walk()
child_2.walk()