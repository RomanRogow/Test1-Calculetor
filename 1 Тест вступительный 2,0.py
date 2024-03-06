calc = input('Введите выражение через пробел: ')

number = calc.split()

try:
    if len(number) < 3:
    	raise Exception("т.к. строка не является математической операцией")
    if len(number) > 3:
        raise Exception("Формат математической операции не удовлетворяет \n заданию - два операнда и один оператор (+, -, /, *)")
    a = int(number[0])
    b = int(number[2])
    c = number[1]
    if a > 10 or b > 10:
        raise Exception("Ввод только от 0 до 10 включительно")
    if c == '+':
        print(a + b)
    elif c == '-':
        print(a - b)
    elif c == '*':
        print(a * b)
    elif c == '/':
        print(a // b)
    else:
        raise Exception("Неверный опереатор")
except ValueError:
    print("Неверный ввод чисел")
finally:
    print("Выполнение завершено")

