class ModeOfTransport:
  def __init__(self, brand, model):
    self.brand = brand
    self.model = model


class Car(ModeOfTransport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Drive!")


class Boat(ModeOfTransport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Sail!")


class Plane(ModeOfTransport):
  def __init__(self, brand, model):
    super().__init__(brand, model)

  def move(self):
    print("Fly!")


car1 = Car("Ford", "Mustang")       #Create a Car object
boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
plane1 = Plane("Boeing", "747")     #Create a Plane object


for x in (car1, boat1, plane1):
  x.move()