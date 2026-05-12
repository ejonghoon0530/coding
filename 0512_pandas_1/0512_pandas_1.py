from ucimlrepo import fetch_ucirepo

auto_mpg = fetch_ucirepo(id = 9)

X = auto_mpg.data.features
y = auto_mpg.data.targets

print(X.head())
print('\n')
print(y.head())

#----------데이터프래임의 크기를 확인하는 방법----------
print("데이터프래임의 크기를 확인하는 방법\n")
print(X.shape)
print(y.shape)
#----------데이터프래임의 정보를 확인하는 방법----------
print("데이터프래임의 정보를 확인하는 방법\n")
print(X.info())
print(y.info())
#----------데이터프래임의 열의 자료형을 확인하는 방법-----
print("데이터프래임의 열의 자료형을 확인하는 방법\n")
print(X.dtypes)
print('\n')
print(y.dtypes)
#----------데이터프래임의 기술 통계정보 요약------------
print("데이터프래임의 기술 통계정보 요약\n")
print(X.describe())
print('\n')
print(X['horsepower'].describe())
#----------데이터의 개수 확인---------------------------
print("데이터의 개수 확인\n")
print(X.count())
print('\n')
print(type(X.count()))
#---------각 열의 고유값 개수 확인---------------------
print("각 열의 고유값 개수 확인\n")
#unique_values = X['origin'].value_counts()
unique_values = X['horsepower'].value_counts(dropna=True)
print(unique_values)
print('\n')

print(type(unique_values))
#---------평균값--------------------------------------------
print("평균값\n")
print(X.mean())
print('\n')
print(X['horsepower'].mean())
print('\n')
print(X[['horsepower', 'weight']].mean())
#--------중간값--------------------------------------------
print("중간값\n")
print(X.median())
print('\n')
print(X['horsepower'].median())
#--------최대값--------------------------------------------
print("최대값\n")
print(X.max())
print('\n')
print(X['horsepower'].max())
#--------최소값--------------------------------------------
print("최소값\n")
print(X.min())
print('\n')
print(X['horsepower'].min())
