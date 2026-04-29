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

import pandas as pd

exam_data = {'이름' : ['서준', '우현', '인아'],
             '수학' : [90, 80, 70],
             '영어' : [98, 89, 95],
             '음악' : [85, 95, 100],
             '체육' : [100, 90, 90]}
df = pd.DataFrame(exam_data)
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

print(df.iloc[: : 2]) #0부터 전체행까지 2열간격으로

print(df.iloc[0 : 3 : 2]) #0행부터 3 - 1 행까지 2열간격으로

print(df.iloc[ : : -1]) #0행부터 전체행까지 -1 (역순으로)
