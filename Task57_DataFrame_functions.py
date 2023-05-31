import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('california_housing_train.csv')

# print(df.head(10))                  # to display first 10 lines (5 lines by default)
# print(df.shape)                     # Посмотреть сколько в нем строк и столбцов
# print(df.describe())                # Общая инфо о данных в таблице
# print(df.dtypes)                    # to display type of values
# print(df.isnull().sum())            # Проверить есть ли в файле пустые значения
# print(df.columns)                   # to display number of columns
    
# print(df[df['median_income'] < 2][['median_house_value']]) # Показать median_house_value где median_income < 2

# print(df[df['housing_median_age'] < 20][['total_bedrooms', 'total_rooms']])

# print(df[['longitude', 'latitude']]) # Показать данные в первых 2 столбцах
# df.iloc[ : , 0:2]                    # Показать данные в первых 2 столбцах

# print(df[(df.housing_median_age < 20) & (df.median_house_value > 70000)])
# Выбрать данные где housing_median_age < 20 и median_house_value > 70000

# print(df.median_house_value.max(), df.median_house_value.min())
# Определить какое максимальное и минимальное значение median_house_value

# print(df.loc[(df.median_income == 3.125), ['median_house_value']].max())
# Показать максимальное median_house_value, где median_income = 3.1250


# Узнать какая максимальная population в зоне минимального значения median_house_value:
# Option 1:
# print(df.loc[df.median_house_value < df.median_house_value.quantile(.15)].population.max())
# Option 2:
# df1 = df.loc[df.median_house_value < df.median_house_value.quantile(.15)]
# print(df1.population.max())
# print(df1)

# print(df.median_house_value.quantile(.25))    # function return values at the given quantile over requested axis

# Graphical representation:

# scatterplot
# sns.scatterplot(data=df, x='households', y='population')
# plt.show()

# linear graphs:
# sns.relplot(x='longitude', y='median_house_value', kind='line', data=df)
# plt.show()

# histplot:
# sns.histplot(data=df, x='housing_median_age')
# plt.show()

# Изобразить гистограмму по median_house_value с оттенком housing_median_age
# sns.histplot(data=df, x='median_house_value', hue='housing_median_age')
# plt.show()

# PairGrid - several relations at once:
# cols = ['longitude', 'latitude', 'housing_median_age', 'population', 'households', 'median_house_value']
# g = sns.PairGrid(df[cols])
# g.map(sns.scatterplot)
# plt.show()
