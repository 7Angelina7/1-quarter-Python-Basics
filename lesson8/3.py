class Error:
    def __init__(self, *args):
        self.list = []

    def input(self):

        while True:
            try:
                val = int(input('Введите значения - '))
                self.list.append(val)
                print(f'Текущий список - {self.list} \n ')
            except:
                print(f"Недопустимое значение")
                y_or_n = input(f'Попробовать еще раз? Y/N ')

                if y_or_n == 'Y' or y_or_n == 'y':
                    print(try_except.input())
                elif y_or_n == 'N' or y_or_n == 'n':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.input())