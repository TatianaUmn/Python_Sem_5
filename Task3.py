# 3.	Создайте программу для игры в "Крестики-нолики".

field = list(range(1, 10))

victories = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (1, 4, 7), (2, 5, 8), (3, 6, 9), (1, 5, 9), (3, 5, 7)]

def draw_field(): # создала игровое поле
    print('-------------')
    for i in range(3):
        print('|', field[0 + i*3], '|', field[1 + i*3], '|', field[2 + i*3], '|')
        print('-------------')

def number_input(symbol):
    while True:
        value = input('В какую клетку поставить ' + symbol + '? ')
        if not (value in '123456789'): # проверка, что игрок ввел цифру не больше 9
            print('Неверно. Введите правильное число')
            continue
        value = int(value)
        if str(field[value - 1]) in 'XO': # проверка, занята клетка или нет
            print('Эта клетка уже занята')
            continue
        field[value - 1] = symbol # присвоение указаной клетке символа
        break


def chek_victory(): # проверка выигрышных комбинаций
    for each in victories:
        if (field[each[0] - 1]) == (field[each[1] - 1]) == (field[each[2] - 1]):
            return field[each[1] - 1]
        else:
            return False


def main():
    counter = 0 # нумерация хода
    while True:
        draw_field()
        if counter % 2 == 0:
            number_input('X')
        else:
            number_input('O')
        counter += 1
        if counter > 4: # больше 4 ходов - проверка на выигрыш
            winner = chek_victory()
            if winner:
                draw_field()
                print (winner, 'Выиграл!')
                break
        if counter > 8: # если больше 8 ходов и выигрыша не было, то игра закончилась ничьей 
            draw_field()
            print('Ничья!')
            break


main()