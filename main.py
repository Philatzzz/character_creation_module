from random import randint
from graphic_arts.start_game_banner import run_screensaver

DEFAULT_ATTACK = 5
DEFAULT_DEFENCE = 10
DEFAULT_STAMINA = 80


class Character:
    RANGE_VALUE_ATACK = (1, 3)
    RANGE_VALUE_DEFENCE = (1, 5)
    SPECIAL_SKILL = 'Удача'
    SPECIAL_BUFF = 15
    BRIEF_DESC_CHAR_CLASS = 'отважный любитель приключений'

    def __init__(self, name):
        self.name = name

    def attack(self):
        value_atack = DEFAULT_ATTACK + randint(*self.RANGE_VALUE_ATACK)
        return (f'{self.name} нанес противнику урон, равный {value_atack}.')

    def defence(self):
        value_defence = DEFAULT_DEFENCE + randint(*self.RANGE_VALUE_DEFENCE)
        return (f'{self.name} блокировал {value_defence} урона.')

    def special(self):
        return (f'{self.name} применил специальное умение '
                f'"{self.SPECIAL_SKILL} {self.SPECIAL_BUFF}".')

    def __str__(self):
        return f'{self.name} - {self.BRIEF_DESC_CHAR_CLASS}.'


class Warrior(Character):
    BRIEF_DESC_CHAR_CLASS = (' дерзкий воин ближнего боя. '
                             'Сильный, выносливый и отважный')
    RANGE_VALUE_ATTACK = (3, 5)
    RANGE_VALUE_DEFENCE = (5, 10)
    SPECIAL_BUFF = DEFAULT_STAMINA + 25
    SPECIAL_SKILL = 'Выносливость'


class Mage(Character):
    BRIEF_DESC_CHAR_CLASS = (' находчивый воин дальнего боя. '
                             'Обладает высоким интеллектом')
    RANGE_VALUE_ATTACK = (5, 10)
    RANGE_VALUE_DEFENCE = (-2, 2)
    SPECIAL_BUFF = DEFAULT_ATTACK + 40
    SPECIAL_SKILL = 'Атака'


class Healer(Character):
    BRIEF_DESC_CHAR_CLASS = (' могущественный заклинатель. '
                             'Черпает силы из природы, веры и духов')
    RANGE_VALUE_ATTACK = (-3, -1)
    RANGE_VALUE_DEFENCE = (2, 5)
    SPECIAL_BUFF = DEFAULT_DEFENCE + 30
    SPECIAL_SKILL = 'Защита'


def attack(char_name, char_class):
    """Atack enemy"""
    if char_class == 'warrior':
        return (f'{char_name} нанёс урон '
                f'противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name} нанёс урон '
                f'противнику равный {5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name} нанёс урон '
                f'противнику равный {5 + randint(-3, -1)}')
    return None


def defence(char_name, char_class):
    """Defence atack"""
    if char_class == 'warrior':
        return (f'{char_name} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name} блокировал {10 + randint(2, 5)} урона')
    return None


def special(char_name, char_class):
    """Special ability"""
    if char_class == 'warrior':
        return (f'{char_name} применил специальное '
                f'умение «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name} применил специальное '
                f'умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name} применил специальное '
                f'умение «Защита {10 + 30}»')
    return None


def start_training(char_name: str, char_class: Character):
    """Starting training"""
    print('Потренируйся управлять своими навыками.')
    print('Введи одну из команд: attack — чтобы атаковать '
          'противника, defence — чтобы блокировать атаку противника '
          'или special — чтобы использовать свою суперсилу.')
    print('Если не хочешь тренироваться, введи команду skip.')
    commands = {
        'attack': char_class.attack(),
        'defence': char_class.defence(),
        'special': char_class.special()
    }
    cmd = ''
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd in commands:
            print(commands[cmd])
    return 'Тренировка окончена.'


def choice_char_class(char_name: str) -> Character:
    """Choose your class"""
    game_classes = {
        'warrior': Warrior,
        'mage': Mage,
        'healer': Healer
    }
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, '
                           'за которого хочешь играть: '
                           'Воитель — warrior, Маг — mage, Лекарь — healer: ')
        if char_class in game_classes:
            var_game_class: Character = game_classes[char_class](char_name)
            print(var_game_class)
        else:
            print('Вы ввели неверное название класса')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор,'
                               ' или любую другую кнопку,'
                               ' чтобы выбрать другого персонажа ').lower()
    return var_game_class


if __name__ == '__main__':
    run_screensaver()
    print('Приветствую тебя, искатель приключений!')
    print('Прежде чем начать игру...')
    char_name = input('...назови себя: ')
    print(f'Здравствуй, {char_name}! '
          'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
    print('Ты можешь выбрать один из трёх путей силы:')
    print('Воитель, Маг, Лекарь')
    char_class = choice_char_class(char_name)
    print(start_training(char_name, char_class))
