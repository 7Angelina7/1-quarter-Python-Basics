def fun_sum(nums):
    sum = 0
    symbol = False
    for num in nums:
        try:
            if num:
                sum += float(num)
        except ValueError:
            symbol = True
    return sum, symbol

general_sum = 0
while True:
    num_str = input("Введите числа через пробел:").split(" ")
    sum, stop_symbol = fun_sum(num_str)
    general_sum += sum
    print(f'сумма {general_sum}')
    if stop_symbol:
        break