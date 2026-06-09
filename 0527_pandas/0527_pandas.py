#-----------------누락데이터확인---------------------------
# import seaborn as sns

# df = sns.load_dataset('titanic')
# df.head()
#df.info()

# nan_deck = df['deck'].value_counts(dropna = False)
# print(nan_deck)

# print(df.isnull().sum(axis = 0))

# print(df.head().isnull().sum(axis = 0))

# print(df.head().isnull())

# print(df.head().notnull())
#------------------------------------------------------------
#-----------------------누락데이터 제거----------------------
# missing_df = df.isnull()
# for col in missing_df.columns:
#     missing_count = missing_df[col].value_counts()

#     try:
#         print(col, ': ', missing_count[True])
#     except KeyError:
#         print(col, ': 0')
#열을 삭제하기
# df_thresh = df.dropna(axis = 1, thresh = 500)
# print(df_thresh.columns)
#행을 삭제하기
# df_age = df.dropna(subset = ['age'],   how = 'any', axis = 0)
# print(len(df_age))
#-----------------------------------------------------------
#----------------age의 NaN값 평균값으로 치환하기-----------------------
import seaborn as sns

df = sns.load_dataset('titanic')

# print(df['age'].head(10))
# print('\n')

# mean_age = df['age'].mean(axis = 0)
# df['age'].fillna(mean_age, inplace = True)
# print(df['age'].head(10))

#---------------------------------------------------
#-----------------승선한 도시 이름을 찾아 치환-------------------
# print(df['embark_town'][825:830])
# print('\n')

# most_freq = df['embark_town'].value_counts(dropna = True).idxmax()
# print(most_freq)
# print('\n')

# df['embark_town'].fillna(most_freq, inplace = True)
# print(df['embark_town'][825:830])
#--------------------------------------------
#--------------------바로직전값으로 치환-------------------------
# print(df['age'].head(10))
# print('\n')

# mean_age = df['age'].mean(axis = 0)
# df['age'].fillna(mean_age, inplace = True)
# print(df['age'].head(10))

# print(df['embark_town'][825:830])
# print('\n')

# df['embark_town'].fillna(method = 'ffill', inplace = True)
# print(df['embark_town'][825:830])
#----------------------------------------------------------------
#-----------------행의 중복여부 확인--------------------------------------
import pandas as pd

df = pd.DataFrame({'c1' : ['a', 'a', 'b', 'a', 'b'],
                   'c2' : [1, 1, 1, 2, 2],
                   'c3' : [1, 1, 2, 2, 2]})
print(df)
print('\n')

df_dup = df.duplicated()
# print(df_dup)
# print('\n')

#---------------------------------------------------
#-----------------행의 중복 제거--------------------------------------

df2 = df.drop_duplicates()
print(df2)
print('\n')

#----------------------------------------------------
#------------특정 열에 대한 중복 제거-------------------------------
df3 = df.drop_duplicates(subset = ['c2', 'c3'])
print(df3)