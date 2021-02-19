"""== Лото ==

Правила игры в лото.

Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
    Если цифра есть на карточке - она зачеркивается и игра продолжается.
    Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
    Если цифра есть на карточке - игрок проигрывает и игра завершается.
    Если цифры на карточке нет - игра продолжается.

Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать
модуль random: http://docs.python.org/3/library/random.html"""

import random


class Card:
    def __init__(self, name):
        self.name = name
        self.create_card()
        self.data = self.card_new

    def create_card(self):
        randls = random.sample(Chips.chips, 15)
        slices = []
        slices.append(sorted(randls[:5]))
        slices.append(sorted(randls[5:10]))
        slices.append(sorted(randls[10:15]))
        self.card_new = []
        for el in slices:
            for i in range(0, 4):
                el.insert(random.randint(1, len(el) - 1), ' ')
            self.card_new.append(el)
        return self.card_new

    def __str__(self):
        return '-'*30 + '\n' + '\n'.join('  '.join(map(str, el)) for el in self.card_new) + '\n' + '-'*30

    def verify_player(self, new_num, input_player):
        if input_player == 'y':
            for i in self.card_new:
                if new_num in i:
                    i[i.index(new_num)] = '-'
                    break
                elif i.count(new_num) == 0 and i == self.card_new[-1]:
                    print('Такой цифры нет в карточке. Вы проиграли.')
                    raise SystemExit
        if input_player == 'n':
            for i in self.card_new:
                if new_num in i:
                    print(f'Цифра {new_num} есть в карточке. Вы проиграли.')
                    raise SystemExit

    def verify_computer(self, new_num):
        for i in self.card_new:
            if new_num in i:
                i[i.index(new_num)] = '-'

    def compare(self, computer):
        test = 0
        for i in self.card_new:
            for el in i:
                if type(el) == int:
                    test += el
        if test == 0:
            print('Поздравляем! Вы выйграли!')
            raise SystemExit
        else:
            Card.compare_comp(computer)

    def compare_comp(self):
        test = 0
        for i in self.card_new:
            for el in i:
                if type(el) == int:
                    test += el
        if test == 0:
            print('Выйграл компьютер')
            raise SystemExit


class Chips:
    chips = [x for x in range(1, 91)]


class LotoGame:
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer

    def start(self):
        while len(Chips.chips) != 0:
            self.num = random.choice(Chips.chips)
            Chips.chips.remove(self.num)
            print(f'Новый бочонок: {self.num} (осталось {len(Chips.chips)})')
            print(f'Ваша карточка\n{self.player}\nКарточка компьютера\n{self.computer}')
            self.input_player = input('Зачеркнуть цифру? (y/n)  ')
            if self.input_player == 'y' or self.input_player == 'n':
                Card.verify_player(self.player, self.num, self.input_player)
            else:
                print('вы ввели неверный символ. игра завершена')
                break
            Card.verify_computer(self.computer, self.num)
            Card.compare(self.player, self.computer)


human_player = Card('Игрок')
computer_player = Card('Компьютер')

game = LotoGame(human_player, computer_player)
game.start()
