class Dog():
    # class object attributes
    species = "mammel"
    def __init__(self, input_breed, name):
        self.breed = input_breed
        self.name = name

x = Dog('a','b')

print(x.breed,x.name)
print(x.species)