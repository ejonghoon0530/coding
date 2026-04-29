# import pandas as pd

# list_data = ['2019-01-02', 3.14, 'ABC', 100, True]
# sr = pd.Series(list_data)

# idx = sr.index
# val = sr.values
# print(idx)
# print('\n')
# print(val)


# import pandas as pd

# tup_data = ('영인', '2010-05-01', '여', True)
# sr = pd.Series(tup_data, index = ['이름', '생년월일', '성별', '학생여부'])
# #sr = pd.Series(tup_data)

# #print(sr)

# #print(sr[0])
# #print(sr['이름'])

# #print(sr[1 : 2])
# print(sr['생년월일' : '성별'])



# import pandas as pd
# dict_data = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}

# df = pd.DataFrame(dict_data)

# print(type(df))
# print('\n')
# print(df)

# import pandas as pd

# df = pd.DataFrame([[15, '남', '덕영중'], [17, '여', '수리중']],
#                   index = ['준서', '예은'],
#                   columns = ['나이', '성별', '학교'])
# # df.index = ['학생1', '학생2']
# # df.columns = ['연령', '남녀', '소속']

# df.rename(columns = {'나이' : '연령', '성별' : '남녀', '학교' : '소속'}, inplace = True)
# df.rename(index = {'준서' : '학생1', '예은' : '학생2'}, inplace = True)

# print(df)
# print('\n')
# print(df.index)
# print('\n')
# print(df.columns)


# import pandas as pd

# exam_data = {'수학' : [90, 80, 70], '영어' : [98, 89, 95],
#              '음악' : [85, 95, 100], '체육' : [100, 90, 90]}

# df = pd.DataFrame(exam_data, index = ['서준', '우현', '인아'])
# print(df)
# print('\n')

# df2 = df[:]
# df2.drop('우현', inplace = True)
# print(df2)
# print('\n')

# df3 = df[:]
# df3.drop(['우현', '인아'], axis = 0, inplace = True)
# print(df3)

# df4 = df.copy()
# df4.drop('수학', axis = 1, inplace = True)
# print(df4)
# print('\n')

# df5 = df.copy()
# df5.drop(['영어', '음악'], axis = 1, inplace = True)
# print(df5)

# label2 = df.loc[['서준', '우현']]
# position2 = df.iloc[[0, 1]]
# print(label2)
# print('\n')
# print(position2)

# label3 = df.loc['서준' : '우현']
# position3 = df.iloc[0 : 1]
# print(label3)
# print('\n')
# print(position3)

# import pandas as pd

# exam_data = {'이름' : ['서준', '우현', '인아'],
#              '수학' : [90, 80, 70],
#              '영어' : [98, 89, 95],
#              '음악' : [85, 95, 100],
#              '체육' : [100, 90, 90]}
# df = pd.DataFrame(exam_data)
# print(df)
# print(type(df))
# print('\n')

# math1 = df['수학']
# print(math1)
# print(type(math1))
# print('\n')

# english = df.영어
# print(english)
# print(type(english))

# music_gym = df [['음악', '체육']]
# print(music_gym)
# print(type(music_gym))
# print('\n')

# math2 = df[['수학']]
# print(math2)
# print(type(math2))

# print(df.iloc[: : 2]) #0부터 전체행까지 2열간격으로

# print(df.iloc[0 : 3 : 2]) #0행부터 3 - 1 행까지 2열간격으로

# print(df.iloc[ : : -1]) #0행부터 전체행까지 -1 (역순으로)

# df.set_index('이름', inplace = True)
# print(df)

# a = df.loc['서준', '음악']
# print(a)
# b = df.iloc[0, 2]
# print(b)

# c = df.loc['서준', ['음악', '체육']]
# print(c)
# d = df.iloc[0, [2, 3]]
# print(d)
# e = df.loc['서준', '음악' : '체육']
# print(e)
# f = df.iloc[0, 2:]
# print(f)

# g = df.loc[['서준', '우현'], ['음악', '체육']]
# print(g)
# h = df.iloc[[0, 1], [2, 3]]
# print(h)
# i = df.loc['서준' : '우현', '음악' : '체육']
# print(i)
# j = df.iloc[0:2, 2:]
# print(j)

# print(df)
# print('\n')

# df.loc[3] = 0
# print(df)
# print('\n')

# df.loc[4] = ['동규', 90, 80, 70, 60]
# print(df)
# print('\n')

# df.loc['행5'] = df.loc[3]
# print(df)

# df.set_index('이름', inplace = True)
# print(df)
# print('\n')

# df.iloc[0, 3] = 80
# print(df)
# print('\n')

# df.loc['서준', '체육'] = 90
# print(df)
# print('\n')

# df.loc['서준', '체육'] = 100
# print(df)

# df.loc['서준', ['음악', '체육']] = 50
# print(df)
# print('\n')

# df.loc['서준', ['음악', '체육']] = 100, 50
# print(df)

# print(df)
# print('\n')

# df = df.transpose()
# print(df)
# print('\n')

# df = df.T
# print(df)

# ndf = df.set_index(['이름'])
# print(ndf)
# print('\n')

# ndf2 = ndf.set_index(['음악'])
# print(ndf2)
# print('\n')

# ndf3 = ndf.set_index(['수학', '음악'])
# print(ndf3)

# import pandas as pd

# dict_data = {'c0' : [1, 2, 3], 'c1' : [4, 5, 6], 'c2' : [7, 8, 9], 'c3' : [10, 11, 12], 'c4' : [13, 14, 15]}

# df = pd.DataFrame(dict_data, index = ['a', 'c', 'b'])
# print(df)
# print('\n')

# new_index = ['r0', 'r1', 'r2', 'r3', 'r4']
# ndf = df.reindex(new_index)
# print(ndf)
# print('\n')

# ndf2 = df.reindex(new_index, fill_value = 0)
# print(ndf2)

# ndf = df.reset_index()
# print(ndf)

# ndf = df.sort_index(ascending = False)
# print(ndf)

# ndf = df.sort_values(by = 'c1', ascending = False)
# print(ndf)

# import pandas as pd
# import numpy as np

# student1 = pd.Series({'국어' : np.nan, '영어' : 80, '수학' : 90})
# student2 = pd.Series({'수학' : 80, '국어' : 90})


# print(student1)
# print('\n')

# percentage = student1 / 100

# print(percentage)
# print('\n')
# print(type(percentage))

# print(student1)
# print('\n')
# print(student2)
# print('\n')

# sr_add = student1.add(student2, fill_value = 0)
# sr_sub = student1.sub(student2, fill_value = 0)
# sr_mul = student1.mul(student2, fill_value = 0)
# sr_div = student1.div(student2, fill_value = 0)

# result = pd.DataFrame([sr_add, sr_sub, sr_mul, sr_div], index = ['덧셈', '뺄셈', '곱셈', '나눗셈'])
# print(result)

import pandas as pd
import seaborn as sns

titanic = sns.load_dataset('titanic')
df = titanic.loc[:, ['age', 'fare']]
print(df.tail())
print('\n')
print(type(df))
print('\n')

addition = df + 10
print(addition.tail())
print('\n')

subtraction = addition - df
print(subtraction.tail())
print('\n')
print(type(subtraction))



