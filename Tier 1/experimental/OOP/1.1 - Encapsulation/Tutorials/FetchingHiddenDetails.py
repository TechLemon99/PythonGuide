class MyClass:
    def __init__(self, attribute):
        self._internal_data = "This is internal data."
        self._attribute = attribute

    def get_internal_data(self):
        return f"{self._internal_data} {self._attribute}"

    def set_internal_data(self, new_data):
        self._internal_data = new_data
        self._attribute = "I still love playing Roblox"

obj = MyClass("I love playing Roblox")
print(obj.get_internal_data()) # Access via public method

obj.set_internal_data("New internal data.") # Modify via public method
print(obj.get_internal_data())