import logging
from random import randrange

logging.basicConfig(filename="Lab_12.log", level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

games = 0
wins = []
loses = []
draws = []
logging.info("Начало работы")
el = ['камень', 'ножницы', 'бумага']
print('Давайте сыграем в камень-ножницы-бумага')
count = 0
logging.info("Запрос количества побед")
goc = int(input('До скольки побед вы хотите сыграть - '))
logging.info(f"Количество побед - {goc}")
while len(wins) < goc:
    print(f'{count + 1} партия')
    logging.info(f"Начало {count + 1} партии")
    pc_choice_int = randrange(1, 4)
    if pc_choice_int == 1:
        pc_choice = 'Камень'
    elif pc_choice_int == 2:
        pc_choice = 'Ножницы'
    elif pc_choice_int == 3:
        pc_choice = 'Бумага'
    logging.info(f"Компьютер загадал - {pc_choice.lower()}")

    logging.info("Запрос хода у пользователя")
    hm_choice = input('Введите ваш ход - ')
    while hm_choice.lower() not in el:
        print('Вы ввели что-то не то')
        logging.error(f"Ошибка!!! Пользователь ввел - {hm_choice}")
        logging.info("Запрос хода у пользователя")
        hm_choice = input('Введите ваш ход - ')
    games += 1
    print(f'Ваш ход - {hm_choice.title()}')
    logging.info(f"Пользователь выбрал - {hm_choice.lower()}")
    print(f'Мой ход - {pc_choice}')
    if (pc_choice.lower() == 'камень' and hm_choice.lower() == 'камень'):
        print('Ничья')
        draws.append(3)
        logging.info("Результат - Ничья")
        count += 1
    elif (pc_choice.lower() == 'ножницы' and hm_choice.lower() == 'ножницы'):
        print('Ничья')
        draws.append(3)
        logging.info("Результат - Ничья")
        count += 1
    elif (pc_choice.lower() == 'бумага' and hm_choice.lower() == 'бумага'):
        print('Ничья')
        draws.append(3)
        logging.info("Результат - Ничья")
        count += 1
    elif (pc_choice.lower() == 'камень' and hm_choice.lower() == 'ножницы'):
        print('Вы проиграли')
        loses.append(2)
        logging.info("Результат - Победа компьютера")
        count += 1
    elif (pc_choice.lower() == 'ножницы' and hm_choice.lower() == 'бумага'):
        print('Вы проиграли')
        loses.append(2)
        logging.info("Результат - Победа компьютера")
        count += 1
    elif (pc_choice.lower() == 'бумага' and hm_choice.lower() == 'камень'):
        print('Вы проиграли')
        loses.append(2)
        logging.info("Результат - Победа компьютера")
        count += 1
    elif (pc_choice.lower() == 'бумага' and hm_choice.lower() == 'ножницы'):
        print('Вы выиграли')
        wins.append(1)
        logging.info("Результат - Победа пользователя")
        count += 1
    elif (pc_choice.lower() == 'ножницы' and hm_choice.lower() == 'камень'):
        print('Вы выиграли')
        wins.append(1)
        logging.info("Результат - Победа пользователя")
        count += 1
    elif (pc_choice.lower() == 'камень' and hm_choice.lower() == 'бумага'):
        print('Вы выиграли')
        wins.append(1)
        logging.info("Результат - Победа пользователя")
        count += 1
    logging.info(f"Конец {games} партии")
if games == 1:
    print(f'Из сыгранной {games} партии: побед ({len(wins)}), поражений ({len(loses)}), ничей ({len(draws)})')
else:
    print(f'Из сыгранных {games} партий: побед ({len(wins)}), поражений ({len(loses)}), ничей ({len(draws)})')
logging.info("")