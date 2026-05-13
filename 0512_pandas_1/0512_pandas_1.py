# from ucimlrepo import fetch_ucirepo

# auto_mpg = fetch_ucirepo(id = 9)

# X = auto_mpg.data.features
# y = auto_mpg.data.targets

# print(X.head())
# print('\n')
# print(y.head())

# #----------데이터프래임의 크기를 확인하는 방법----------
# print("데이터프래임의 크기를 확인하는 방법\n")
# print(X.shape)
# print(y.shape)
# #----------데이터프래임의 정보를 확인하는 방법----------
# print("데이터프래임의 정보를 확인하는 방법\n")
# print(X.info())
# print(y.info())
# #----------데이터프래임의 열의 자료형을 확인하는 방법-----
# print("데이터프래임의 열의 자료형을 확인하는 방법\n")
# print(X.dtypes)
# print('\n')
# print(y.dtypes)
# #----------데이터프래임의 기술 통계정보 요약------------
# print("데이터프래임의 기술 통계정보 요약\n")
# print(X.describe())
# print('\n')
# print(X['horsepower'].describe())
# #----------데이터의 개수 확인---------------------------
# print("데이터의 개수 확인\n")
# print(X.count())
# print('\n')
# print(type(X.count()))
# #---------각 열의 고유값 개수 확인---------------------
# print("각 열의 고유값 개수 확인\n")
# #unique_values = X['origin'].value_counts()
# unique_values = X['horsepower'].value_counts(dropna=True)
# print(unique_values)
# print('\n')

# print(type(unique_values))
# #---------평균값--------------------------------------------
# print("평균값\n")
# print(X.mean())
# print('\n')
# print(X['horsepower'].mean())
# print('\n')
# print(X[['horsepower', 'weight']].mean())
# #--------중간값--------------------------------------------
# print("중간값\n")
# print(X.median())
# print('\n')
# print(X['horsepower'].median())
# #--------최대값--------------------------------------------
# print("최대값\n")
# print(X.max())
# print('\n')
# print(X['horsepower'].max())
# #--------최소값--------------------------------------------
# print("최소값\n")
# print(X.min())
# print('\n')
# print(X['horsepower'].min())
# #----------표준편차-------------------------------------------------
# print("표준편차\n")
# print(X.std())
# print('\n')
# print(X['horsepower'].std())
# #----------------상관계수-------------------------------------------------
# print("상관계수\n")
# print(X.corr())
# print('\n')
# print(X[['horsepower', 'weight']].corr())

#------------그래프 시각화-------------------------------
# import pandas as pd
# df = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0512_pandas_1\\남북한 발전 전력량2.xlsx', engine = 'openpyxl')

# df_ns = df.iloc[[0, 1], 1:]
# df_ns.index = ['South', 'North']

# tdf_ns = df_ns.T
# print(tdf_ns.head())
# print('\n')
# tdf_ns.plot()

# #------------------막대그래프-------------------------------
# print('막대그래프\n')
# tdf_ns.plot(kind = 'bar')

# #------------------히스토그램-------------------------------
# print('히스토그램\n')
# tdf_ns.plot(kind = 'hist')

#-------------------------산점도-------------------------------
print('산점도\n')
from ucimlrepo import fetch_ucirepo

auto_mpg = fetch_ucirepo(id = 9)

X = auto_mpg.data.features
y = auto_mpg.data.targets

X.plot(x = 'weight', y = 'horsepower', kind = 'scatter')

#-------------------------박스플롯-------------------------------
print('박스플롯\n')
X[['acceleration', 'horsepower', 'displacement']].plot(kind = 'box')

