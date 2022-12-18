emp = '-'
pl1 = 'x'
pl1_str = 'Игрок 1'
pl2 = '0'
pl2_str = 'Игрок 2'
str_title = '  0 1 2'
str_zero_leg = '0 - x -'
str_one_leg_1 = '1 - - -'
str_one_leg_2 = '1 0 - -'
str_two_leg = '2 - - -'
str_zero = {'00':emp, '01':emp, '02':emp}
str_one = {'10':emp, '11':emp, '12':emp}
str_two = {'20':emp, '21':emp, '22':emp}
disp = 'Сейчас обстановка на поле выглядит так:'

def screen():
    print(disp)
    print ('')
    print(str_title)
    print('0 '+' '.join(str_zero.values()))
    print('1 '+' '.join(str_one.values()))
    print('2 '+' '.join(str_two.values()))
    print ('')


def legend():
    print ('ЛЕГЕНДА')
    print('')
    print (f'{pl1_str} ходит с x')
    print(f'{pl2_str} ходит с 0')
    print('')
    print('Чтобы сделать ход, введите в консоль сначала номер строки, а потом номер столбца БЕЗ ПРОБЕЛА')
    print('')
    print('Например, при вводе "01" обстановка на поле будет выглядеть так:')
    print('')
    print(str_title)
    print(str_zero_leg)
    print(str_one_leg_1)
    print(str_two_leg)
    print('')
    print('А при вводе "10" обстановка на поле будет выглядеть уже вот так:')
    print('')
    print(str_title)
    print(str_zero_leg)
    print(str_one_leg_2)
    print(str_two_leg)
    print('')
    screen()

legend()


def change(player, player_str):
    inp = str(input(f'{player_str} твой ход:'))
    print ('')
    for k in str_zero.keys():
        if k == inp:
            str_zero[inp] = player
        elif k != inp:
            for k in str_one.keys():
                if k == inp:
                    str_one[inp] = player
                elif k != inp:
                    for k in str_two.keys():
                        if k == inp:
                            str_two[inp] = player


def game():
    while True:
        change(pl1, pl1_str)
        screen()
        change(pl2, pl2_str)
        screen()
        if all([emp not in str_zero.values(),
                emp not in str_one.values(),
                emp not in str_two.values()]):
            print('Ничья!')
            break

        elif any([all([str_zero['00'] == pl1,
                       str_zero['01'] == pl1,
                       str_zero['02'] == pl1]),

                  all([str_one['10'] == pl1,
                       str_one['11'] == pl1,
                       str_one['12'] == pl1]),

                  all([str_two['20'] == pl1,
                       str_two['21'] == pl1,
                       str_two['22'] == pl1]),

                  all([str_zero['00'] == pl1,
                       str_one['10'] == pl1,
                       str_two['20'] == pl1]),

                  all([str_zero['02'] == pl1,
                       str_one['12'] == pl1,
                       str_two['22'] == pl1]),

                  all([str_zero['00'] == pl1,
                       str_one['11'] == pl1,
                       str_two['22'] == pl1]),

                  all([str_zero['02'] == pl1,
                       str_one['11'] == pl1,
                       str_two['20'] == pl1])]):
            print('Игрок 1 победил!')
            break

        elif any([all([str_zero['00'] == pl2,
                       str_zero['01'] == pl2,
                       str_zero['02'] == pl2]),

                  all([str_one['10'] == pl2,
                       str_one['11'] == pl2,
                       str_one['12'] == pl2]),

                  all([str_two['20'] == pl2,
                       str_two['21'] == pl2,
                       str_two['22'] == pl2]),

                  all([str_zero['00'] == pl2,
                       str_one['10'] == pl2,
                       str_two['20'] == pl2]),

                  all([str_zero['02'] == pl2,
                       str_one['12'] == pl2,
                       str_two['22'] == pl2]),

                  all([str_zero['00'] == pl2,
                       str_one['11'] == pl2,
                       str_two['22'] == pl2]),

                  all([str_zero['02'] == pl2,
                       str_one['11'] == pl2,
                       str_two['20'] == pl2])]):
            print('Игрок 2 победил!')
            break


game()



















