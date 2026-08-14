"""Проект FitLife - MVP версия 1.0"""

WATER_PER_KG = 30
ML_IN_L = 1000

# 1. Знакомство
user_name = input('Представьтесь, пожалуйста! ')
while True:
    try:
        user_age = int(
            input('Назовите ваш возраст (только число полных лет) ')
        )
        break
    except ValueError:
        print('Попробуйте еще раз, возраст должен быть числом')


# 2. Сбор данных
while True:
    try:
        user_weight = float(
            input('Введите вес в килограммах, используя точку: 60.75 ')
        )
        break
    except ValueError:
        print('Попробуйте еще раз, нужно ввести число с разделителем-точкой')

while True:
    try:
        user_height = float(
            input('Введите рост в метрах, используя точку: 1.75 ')
        )
        break
    except ValueError:
        print('Попробуйте еще раз, нужно ввести число с разделителем-точкой')


# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
# Формула ИМТ: вес разделить на (рост в квадрате)
bmi = user_weight / (user_height ** 2)

# Подсчет воды: вес * 30 мл
water_needed = (user_weight * WATER_PER_KG) / ML_IN_L

# 4. Вывод красивого результата
print('-' * 40)
print(f"Привет, {user_name}!")
print(f"Ваш возраст - {user_age} лет")
print(f"Ваш ИМТ - {bmi:.1f}")
print(f"Вам нужно пить {water_needed:.1f} л воды")
print('-' * 40)

print("Расчет окончен. Будьте здоровы!")
