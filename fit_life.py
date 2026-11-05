#  Проект FitLife - MVP версия 1.0
#  Первый проект (с опозданием :())

import io
import sys

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', newline='')

user_name = input(
    'Здравствуйте, уважаемый пользователь. Введите ваше имя: '
).capitalize()

user_age = int(input(
    f'Приятно познакомиться, {user_name}. Введите ваш возраст: '
))

#  Запрашиваем вес и рост
user_weight = float(input('Введите ваш вес: '))
user_height = float(input('Введите ваш рост (в метрах, используя точку): '))
bmi = user_weight / (user_height ** 2)  # Расчет ИМТ


print('Расчитываем норму воды в литрах')

water_ml = user_weight * 30
water_l = water_ml / 1000  # перевод в литры

print('Подготавливаю общий отчет...')
#  Общий отчет

print(f'\nОтчет для пользователя: {user_name} ({user_age} г.)')
print(f'Твой Индекс Массы Тела: {bmi:.1f}')
print(f'Рекомендуемая норма воды: {water_l:.1f} л. в день')
print('\nРасчет окончен. Будьте здоровы!')
