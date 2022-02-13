vir = input("Введите выручку:")
vir = int(vir)
izd = input("Введите издержки:")
izd = int(izd)
if vir > izd:
    print("фирма в прибыли")
if vir < izd:
    print("фирма работает в убыток")
if vir == izd:
    print("фирма работает в ноль")
