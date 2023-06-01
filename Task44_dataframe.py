# Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего
# из 1 столбца. Ваша задача перевести его в one hot вид. Сможете ли вы это сделать без
# get_dummies?

import numpy as np
import pandas as pd
import random

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
print(data.head())
print(data.shape)


# one hot without dummies:
data_unitary = pd.DataFrame({'robot': [1 if i == 'robot' else 0 for i in lst],
'human': [1 if j == 'human' else 0 for j in lst]})
print(data_unitary)

# 0 & 1 in one column:
data = pd.DataFrame({'whoAmI':lst})
data['whoAmI'] = np.where(data['whoAmI'].str.contains('human'), 1, 0)
print(data)


# get_dummies True & False:
data = pd.DataFrame({'whoAmI':lst})
print(pd.get_dummies(data, columns=['whoAmI']))


# get_dummies 0 & 1 :
data = pd.DataFrame({'whoAmI':lst})
res = (data.drop(columns='whoAmI').join(data['whoAmI'].str.get_dummies(sep=', ')))
print(res)


# get_dummies Syntax:
pd.get_dummies(data, prefix=None, prefix_sep='_', dummy_na=False, columns=None, sparse=False, drop_first=False, dtype=None)
