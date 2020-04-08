num_1 = input('Введите число 1: ')
num_2 = input('Введите число 2: ')
def my_func(num_1, num_2):
    try:
        num_1, num_2 = float(num_1), float(num_2)
        answer = num_1 / num_2
    except ValueError:
        return 'Ошибка'
    except ZeroDivisionError:
        return 'На ноль делить нельзя!'
    return answer
print (my_func(num_1, num_2))