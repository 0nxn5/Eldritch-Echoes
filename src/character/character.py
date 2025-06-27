
class character:
    def __init__(self, name: str, level: int = 1):
        self.name = name
        self.level = level
        self.health = 100
        self.sanity = 100
        self.experience = 0
        self.backstory = ""
        print(f"Character {self.name} created at level {self.level}.")

    def set_name(self, name: str):
        self.name = name
        print(f"Character's name has been set to {self.name}.")

    def set_level(self, level: int):
        self.level = level
        self.health = 100 + (level - 1) * 20
        self.sanity = 100 + (level - 1) * 10
        print(f"{self.name} is now at level {self.level} with {self.health} health and {self.sanity} sanity.")

    def get_info(self):
        return {
            "name": self.name,
            "level": self.level,
            "health": self.health,
            "sanity": self.sanity,
            "experience": self.experience,
            "backstory": self.backstory
        }    

    def set_backstory(self, backstory: str):
        self.backstory = backstory
        print(f"{self.name}'s backstory has been set.")

    def level_up(self):
        self.level += 1
        self.health += 20
        self.sanity += 10
        print(f"{self.name} has leveled up to level {self.level}!")

    def take_damage(self, amount: int):
        self.health -= amount
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
            self.health = 0

    def heal(self, amount: int):
        self.health += amount
        print(f"{self.name} has healed for {amount} health points.")

    def lose_sanity(self, amount: int):
        self.sanity -= amount
        if self.sanity <= 0:
            print(f"{self.name} has lost all sanity!")
            self.sanity = 0
    
    def regain_sanity(self, amount: int):
        self.sanity += amount
        print(f"{self.name} has regained {amount} sanity points.")

    def gain_experience(self, amount: int):
        self.experience += amount
        print(f"{self.name} has gained {amount} experience points.")
        if self.experience >= 100:
            self.level_up()
            self.experience -= 100