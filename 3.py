class Toy:
    def __init__(self, name, color):
        self.name = name
        self.color = color
 
 
class Cat:
    def __init__(self, name, color, pol):
        self.name = name
        self.color = color
        self.pol = pol
 
    def meow(self):
        if self.pol == 'f':
            print(f"{(self.color).capitalize()} кошка {self.name} мяукнула")
        elif self.pol == 'm':
            print(f"{(self.color).capitalize()} кот {self.name} мяукнул")
 
    def play(self, toy: Toy):
        if self.pol == 'f':
            print(f"{(self.color).capitalize()} кошка {self.name} поиграла с {toy.color} {(toy.name).lower()}")
        elif self.pol == 'm':
            print(f"{(self.color).capitalize()} кот {self.name} поиграл с {toy.color} {(toy.name).lower()}")
 
 
toy1 = Toy('Курица', 'жёлтая')
toy2 = Toy('Корова', 'синяя')
kot = Cat('Басик', 'жёлтый', 'm')
koshka = Cat('Муся', 'чёрная', 'f')
kot.meow()
kot.play(toy1)
koshka.play(toy2)
