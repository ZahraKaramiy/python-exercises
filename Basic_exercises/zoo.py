class Animal:
    zoo_name = "Zoooo"
    
    def __init__(self, name, species, age, sound):
        self.name = name
        self.species = species
        self.age = age
        self.sound = sound


    def make_sound(self):
         print(self.sound)
         

    def info(self):
        print(f"name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound}.")
    
    
    def __str__(self):
        return f"name: {self.name}, species: {self.species}, age: {self.age}, sound: {self.sound}."
    
    
lion = Animal("liloo", "lion", 2, "wooooww")
lion.info()
lion.make_sound()
lion.__str__()


class Bird(Animal):
    def __init__(self, name, species, age, sound, wing_span):
        super().__init__(name, species, age, sound)
        self.wing_span = wing_span
    
    
    def make_sound(self):
        print("jik jik jik...")


parrot = Bird("wody", "parrot", 6, "ding ding", 26)
parrot.info()
parrot.make_sound()
        
        
        