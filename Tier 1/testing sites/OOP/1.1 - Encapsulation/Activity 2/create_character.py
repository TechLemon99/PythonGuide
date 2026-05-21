class CreateCharacter:
    def __init__(self, name: str, classtype: str, level: int = 1):
        self.__name = name
        self.__classtype = classtype
        self.__level = max(1, level)
        
    # Getter methods
    def get_name(self) -> str:
        return self.__name

    def get_classtype(self) -> str:
        return self.__classtype

    def get_level(self) -> int:
        return self.__level

    # Setter methods
    def set_name(self, new_name: str):
        if isinstance(new_name, str) and len(new_name.strip()) > 0:
            self.__name = new_name.strip()
        else:
            print("Error: Name must be a non-empty string")

    def set_classtype(self, new_classtype: str):
        valid_classes = ["warrior", "wizard", "archer", "rogue", "cleric"]
        if new_classtype.lower() in valid_classes:
            self.__classtype = new_classtype.lower()
        else:
            print(f"Error: Class must be one of {valid_classes}")

    def set_level(self, new_level: int):
        if isinstance(new_level, int) and new_level >= 1:
            self.__level = new_level
        else:
            print("Error: Level must be a positive integer")

    def level_up(self):
        self.__level += 1
        print(f"{self.__name} leveled up to {self.__level}!")

    def __str__(self):
        return (f"Character: {self.__name}\n"
                f"Class: {self.__classtype.capitalize()}\n"
                f"Level: {self.__level}")