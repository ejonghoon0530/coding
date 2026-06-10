# import seaborn as sns

# titanic = sns.load_dataset('titanic')
# df = titanic.loc[:, ['age', 'fare']]
# df['ten'] = 10

def add_10(n):
    return n + 10
def add_two_obj(a, b):
    return a + b

# sr1 = df['age'].apply(add_10)
# print(sr1.head())
# print('\n')

# sr2 = df['age'].apply(add_two_obj, b = 10)
# print(sr2.head())
# print('\n')

# sr3 = df['age'].apply(lambda x: add_10(x))
# print(sr3.head())

# print(df.head())
# print('\n')

# df_map = df.applymap(add_10)
# print(df_map.head())

# import seaborn as sns

# titanic = sns.load_dataset('titanic')
# df = titanic.loc[:, ['age', 'fare']]
# print(df.head())
# print('\n')

# def missing_value(x):
#     return x.isnull()
# result = df.apply(missing_value, axis = 0)
# print(result.head())
# print('\n')
# print(type(result))

# print(df.head())
# print('\n')

# def min_max(x):
#     return x.max() - x.min()

# result = df.apply(min_max)
# print(result)
# print('\n')
# print(type(result))

# df['add'] = df.apply(lambda x: add_two_obj(x['age'], x['fare']), axis = 1)
# print(df.head())

# def missing_value(x):
#     return x.isnull().sum()
# def missing_count(x):
#     return missing_value(x).sum()
# def total_number_missing(x):
#     return missing_count(x).sum()

# result_df = df.pipe(missing_value)
# print(result_df.head())
# print(type(result_df))


# result_series = df.pipe(missing_count)
# print(result_series)
# print(type(result_series))

# result_value = df.pipe(total_number_missing)
# print(result_value)
# print(type(result_value))

# import pandas as pd

# df = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0609_pandas\\6장\\주가데이터.xlsx')
# # print(df.head(), '\n')
# # print(df.dtypes, '\n')

# dates = df['일자'].str.split('/')
# # print(dates.head(), '\n')

# df['연'] = dates.str[0].get(0)
# df['월'] = dates.str[1].get(0)
# df['일'] = dates.str[2].get(0)
# print(df.head())

# import seaborn as sns

# titanic = sns.load_dataset('titanic')

# mask1 = (titanic.age >= 10) & (titanic.age < 20)
# df_teenage = titanic.loc[mask1, :]
# # print(df_teenage)

# mask2 = (titanic.age < 10) & (titanic.sex == 'female')
# df_female_under10 = titanic.loc[mask2,:]
# # print(df_female_under10.head())

# mask3 = (titanic.age < 10) | (titanic.age >= 60)
# df_under10_morethan60 = titanic.loc[mask3, ['age', 'sex', 'alone']]
# print(df_under10_morethan60.head())


# import pandas as pd
# import seaborn as sns

# titanic = sns.load_dataset('titanic')

# pd.set_option('display.max_columns', 10)

# mask3 = titanic['sibsp'] == 3
# mask4 = titanic['sibsp'] == 4
# mask5 = titanic['sibsp'] == 5

# df_boolean = titanic[mask3 | mask4 | mask5]
# # print(df_boolean.head())

# isin_fillter = titanic['sibsp'].isin([3, 4, 5])
# df_isin = titanic[isin_fillter]
# print(df_isin.head())


import pandas as pd

# df1 = pd.DataFrame({'a' : ['a0', 'a1', 'a2', 'a3'],
#                     'b' : ['b0', 'b1', 'b2', 'b3'],
#                     'c' : ['c0', 'c1', 'c2', 'c3']},
#                    index = [0, 1, 2, 3])
# df2 = pd.DataFrame({'a' : ['a2', 'a3', 'a4', 'a5'],
#                     'b' : ['b2', 'b3', 'b4', 'b5'],
#                     'c' : ['c2', 'c3', 'c4', 'c5'],
#                     'd' : ['d2', 'd3', 'd4', 'd5']},
#                    index = [2, 3, 4, 5])

# print(df1, '\n')
# print(df2, '\n')

# result1 = pd.concat([df1, df2])
# print(result1, '\n')

# result2 = pd.concat([df1, df2], ignore_index = True)
# print(result2, '\n')

# result3 = pd.concat([df1, df2], axis = 1)
# print(result3, '\n')

# result3_in = pd.concat([df1, df2], axis = 1, join = 'inner')
# print(result3_in, '\n')

# sr1 = pd.Series(['e0', 'e1', 'e2', 'e3'], name = 'e')
# sr2 = pd.Series(['f0', 'f1', 'f2'], name = 'f', index = [3, 4, 5])
# sr3 = pd.Series(['g0', 'g1', 'g2', 'g3'], name = 'g')

# result4 = pd.concat([df1, sr1], axis = 1)
# # print(result4, '\n')

# result5 = pd.concat([df1, sr2], axis = 1, sort = True)
# # print(result5, '\n')

# result6 = pd.concat([df1, sr3], axis = 1)
# # print(result6, '\n')

# result7 = pd.concat([sr1, sr3], axis = 0)
# print(result7, '\n')

# pd.set_option('display.max_columns', 10)
# pd.set_option('display.max_colwidth', 20)
# pd.set_option('display.unicode.east_asian_width', True)

# df1 = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0609_pandas\\6장\\stock-price.xlsx', index_col = 'id', engine = 'openpyxl')
# df2 = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0609_pandas\\6장\\stock-valuation.xlsx', index_col = 'id', engine = 'openpyxl')

# print(df1)
# print('\n')
# print(df2)

# merge_inner = pd.merge(df1, df2)
# print(merge_inner)

# merge_outer = pd.merge(df1, df2, how = 'outer', on = 'id')
# print(merge_outer)

# merge_left = pd.merge(df1, df2, how = 'left', left_on = 'stock_name', right_on = 'name')
# print(merge_left)

# price = df1[df1['price'] < 50000]
# print(price.head())
# print('\n')

# value = pd.merge(price, df2)
# print(value)

# pd.set_option('display.max_columns', 10)
# pd.set_option('display.max_colwidth', 20)
# pd.set_option('display.unicode.east_asian_width', True)

# df3 = df1.join(df2)
# # print(df3)

# df4 = df1.join(df2, how = 'inner')
# print(df4)

import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]

# print('승객 수:', len(df))
# print(df.head())
# print('\n')

grouped = df.groupby('class')
# print(grouped)

# for key, group in grouped:
#     print('* key :', key)
#     print('* number :', len(group))
#     print(group.head())
#     print('\n')

average = grouped[['age', 'fare', 'survived']].mean()
# print(average)

group3 = grouped.get_group('Third')
# print(group3.head())

grouped_two = df.groupby(['class', 'sex'])

# for key, group in grouped_two:
#     print('* key :', key)
#     print('* number :', len(group))
#     print(group.head())
#     print('\n')

average_two = grouped_two.mean()
# print(average_two)
# print('\n')
# print(type(average_two))

group3f = grouped_two.get_group(('Third', 'female'))
# print(group3f.head())

grouped = df.groupby(['class'])
std_all = grouped[['age', 'fare', 'survived']].std()
# print(std_all)
# print('\n')
# print(type(std_all))
# print('\n')

# std_fare = grouped.fare.std()
# print(std_fare)
# print('\n')
# print(type(std_fare))

def min_max(x):
    return x.max() - x.min()
agg_minmax = grouped[['age', 'fare', 'survived']].agg(min_max)
# print(agg_minmax.head())

agg_all = grouped.agg(['min', 'max'])
# print(agg_all.head())
# print('\n')

# agg_sep = grouped.agg({'fare' : ['min', 'max'], 'age': 'mean'})
# print(agg_sep.head())

age_mean = grouped.age.mean()
# print(age_mean)
# print('\n')

# age_std = grouped.age.std()
# print(age_std)
# print('\n')

# for key, group in grouped.age:
#     group_zsore = (group - age_mean.loc[key]) / age_std.loc[key]
#     print('* origin :', key)
#     print(group_zsore.head())
#     print('\n')
    
    
def z_score(x):
    return (x - x.mean()) / x.std()

age_zscore = grouped.age.transform(z_score)
# print(age_zscore.loc[[1, 9, 0]])
# print('\n')
# print(len(age_zscore))
# print(age_zscore.loc[0:9])
# print('\n')
# print(type(age_zscore))

grouped_filter = grouped.filter(lambda x: len(x) >= 200)
# print(grouped_filter.head())
# print('\n')
# print(type(grouped_filter))

age_filter = grouped.filter(lambda x: x.age.mean() < 30)
# print(age_filter.head())
# print('\n')
# print(type(age_filter))

agg_grouped = grouped.apply(lambda x: x.describe())
# print(agg_grouped)

age_zscore = grouped.age.apply(z_score)
# print(age_zscore.head())

age_filter = grouped.apply(lambda x: x.age.mean() < 30)
# print(age_filter)
# print('\n')
# for x in age_filter.index:
#     if age_filter[x] == True:
#         age_filter_df = grouped.get_group(x)
#         print(age_filter_df.head())
#         print('\n')

grouped = df.groupby(['class', 'sex'])

gdf = grouped.mean()
# print(gdf)
# print('\n')
# print(type(gdf))

# print(gdf.loc[('First', 'female')])
# print('\n')
# print(gdf.xs('male', level = 'sex'))

df = titanic.loc[:, ['age', 'sex', 'class', 'fare', 'survived']]
# print(df.head())
# print('\n')

pdf1 = pd.pivot_table(df, index = 'class', columns = 'sex', values = 'age', aggfunc = 'mean')
# print(pdf1.head())

pdf2 = pd.pivot_table(df, index = 'class', columns = 'sex', values = 'survived', aggfunc = ['mean', 'sum'])
# print(pdf2.head())

pdf3 = pd.pivot_table(df, index = ['class', 'sex'], columns = 'survived', values = ['age', 'fare'], aggfunc = ['mean', 'max'])
# print(pdf3.head())

# print(pdf3.index)
# print(pdf3.columns)

# print(pdf3.xs('First'))

# print(pdf3.xs(('First', 'female')))

print(pdf3.head())

# print(pdf3.xs('male', level = 'sex'))

# print(pdf3.xs(('Second', 'male'), level = [0, 'sex']))
# print(pdf3.xs(('Second', 'male'), level = [0, 1]))

# print(pdf3.xs('mean', axis = 1))

# print(pdf3.xs(('mean', 'age'), axis = 1))

print(pdf3.xs(1, level = 'survived', axis = 1))

print(pdf3.xs(('max', 'fare', 0), level = [0, 1, 2], axis = 1))