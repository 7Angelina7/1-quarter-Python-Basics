class Road:
    def __init__(self,lenght,width):
        self.lenght = lenght
        self.width = width
        self.weight = 25
        self.height = 0.05
    def mass(self):
        mass = self.lenght * self.width * self.weight * self.height / 1000
        print(f"Для покрытия дорожного полотна необходимо: {round(mass)} тонн асфальта")
r = Road(5000, 20)
r.mass()
