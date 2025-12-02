class Superhero:
    def __init__(self, name: str, strength: int, speed: int, can_fly: bool):
        self.name = name
        self.strength = strength
        self.speed = speed
        self.can_fly = can_fly

    def __str__(self):
        if self.can_fly:
            fly_status = "and can fly"
        else:
            fly_status = "and can't fly"
        return f"{self.name} has {self.strength} strength, {self.speed} speed {fly_status}\n"

class BadgerMan(Superhero):
    def perform_ability(self):
        print(f"{self.name} tunnels underground with his sharp claws\n")

class TigerWoman(Superhero):
    def __init__(self, name, strength, speed, can_fly, powerup, damage_multiplier: int = 1):
        super().__init__(name, strength, speed, can_fly)
        self.powerup = powerup
        self.damage_multiplier = damage_multiplier

    def perform_ability(self):
        print(f"{self.name} uses her super strength to tear through solid stone\n")
        print(f"{self.name} lets out a powerful {self.powerup} that stuns her enemies\n")

    def __str__(self):
        if self.can_fly:
            fly_status = "and can fly"
        else:
            fly_status = "and can't fly"
        return f"{self.name} has {self.strength} strength, {self.speed} speed {fly_status}, powerup is {self.powerup} and damage multiplier is {self.damage_multiplier}\n"


badger_man = BadgerMan("Badger-Man", 7, 9, False)
print(badger_man)
badger_man.perform_ability()

tiger_woman = TigerWoman("Tiger-Woman", 10, 8, False, "Roar", 2)
print(tiger_woman)
tiger_woman.perform_ability()