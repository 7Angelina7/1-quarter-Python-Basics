class Car:
    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.speed = int(self.speed)
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'{self.name} тронулась.'

    def stop(self):
        return f'\n{self.name} остановилась.'

    def turn(self, direction):
        return f'\n{self.name} повернула {direction}'

    def show_speed(self):
        return f'\nВаша скорость: {self.speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВаша скорость слишком высокая. Ваша скорость: {self.speed} км/ч'
        else:
            return f'Скорость {self.name} в пределах нормы'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.speed < 40:
            return f'\nВаша скорость слишком низкая. Ваша скорость: {self.speed} км/ч'
        else:
            return f'Скорость {self.speed} в пределах нормы'

class PoliceCar(Car):
    pass

town = TownCar('Mazda', '70','white', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('направо'), town.turn('налево'), town.stop())

sport = SportCar('Mazda-RX8', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('направо'), sport.stop())

work = WorkCar('Scania', 30, 'grey', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())

police = PoliceCar('Ford', 100, 'blue', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())

