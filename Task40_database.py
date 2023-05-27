# Задача 40: Работать с файлом california_housing_train.csv, который находится в папке
# sample_data. Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)

import pandas as pd

df = pd.read_csv('C:\Python-GB\seminar01\california_housing_train.csv')

print(f'Ср. стоимость дома, где population до 500: {df.loc[df.population <= 500].median_house_value.mean()}')


# Задача 42: Узнать какая максимальная households в зоне минимального значения population

print(f'Макс. households при мин. population: {df.loc[df.population < df.population.quantile(.15)].households.max()}')