class Diagnostics:

    def __init__(self, body_part, time, temp, *args):
        self.body_part = body_part
        self.time = time
        self.temp = temp
        self.my_store_full = []
        self.my_store = []
        self.my_unit = {'Болит': self.body_part, 'Часов в состоянии боли': self.time, 'Температура тела': self.temp}

    def __str__(self):
        return f'{self.body_part} болит {self.time} часов, температура тела {self.temp}'

    def reception_patient(self):

        try:
            unit = input(f'Что болит? ')
            unit_t = int(input(f'Сколько часов болит? '))
            unit_tp = int(input(f'Введите температуру тела: '))
            unique = {'Болит': unit, 'Часов в состоянии боли': unit_t, 'Температура тела': unit_tp}
            self.my_unit.update(unique)
            self.my_store.append(self.my_unit)
            print(f'Симптомы -\n {self.my_store}')
        except:
            return f'Ошибка ввода данных'

        print(f'Для выхода нажмите - Q, продолжение нажмите - Enter')

        q = input(f'---> ')
        if q == 'Q' or q == 'q':
            self.my_store_full.append(self.my_store)

            print(f'История болезни -\n {self.my_store_full}')
            return f'Программа сбора симптомов завершена'
        else:
            return Diagnostics.reception_patient(self)


class Head_part(Diagnostics):
    def to_head(self):
        pass


class Back_part(Diagnostics):
    def to_back(self):
        pass


class Belly_part(Diagnostics):
    def to_belly(self):
        pass


unit_1 = Head_part('мигрень', 1, 38)
unit_2 = Back_part('грыжа', 12, 37)
unit_3 = Belly_part('аппендицит', 4, 39)
print(unit_1.reception_patient())
print(unit_2.reception_patient())
print(unit_3.reception_patient())
print(unit_1.to_head())
print(unit_3.to_belly())


