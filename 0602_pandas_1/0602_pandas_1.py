#-------------------단위환산-----------------------
from ucimlrepo import fetch_ucirepo

# auto_mpg = fetch_ucirepo(id = 9)

# x = auto_mpg.data.features
# y = auto_mpg.data.targets

# mpg_to_kpl = 1.60934 / 3.78541
# y['kpl'] = y * mpg_to_kpl
# print(y.head())
# print('\n')

# y['kpl'] = y['kpl'].round(2)
# print(y.head(3))

#-------------------------------------------
#---------------------자료형변환-----------------------------
import numpy as np
import pandas as pd

#df = pd.read_csv('C:\\Users\\ejong\\Desktop\\coding\\0602_pandas_1\\auto-mpg.csv')

# df['horsepower'] = df['horsepower'].replace('?', np.nan)
# df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
# df['horsepower'] = df['horsepower'].astype('float')

#print(df['horsepower'].dtype)

# print(df['origin'].unique())

# df['origin'].replace({1: 'USA', 2 : 'EU', 3 : 'JPN'}, inplace = True)

# print(df['origin'].unique())
# print(df['origin'].dtype)

#--------------------------origin의 데이터 타입 변경하기-----------------------

# df['origin'] = df['origin'].astype('category')
# print(df['origin'].dtypes)

# df['origin'] = df['origin'].astype('str')
# print(df['origin'].dtypes)

#-------------------------model year의 데이터 타입 변경하기-----------------------
# print(df['model year'].sample(3))
# df['model year'] = df['model year'].astype('category')
# print(df['model year'].sample(3))

#----------------------구간 분할------------------------

# df.columns = ['mpg', 'cylinders', 'displacement', 'horsepower', 'weight', 'acceleration', 'model year', 'origin', 'name']

# df['horsepower'] = df['horsepower'].replace('?', np.nan)
# df.dropna(subset = ['horsepower'], axis = 0, inplace = True)
# df['horsepower'] = df['horsepower'].astype('float')

#count, bin_dividers = np.histogram(df['horsepower'], bins = 3)
# print(bin_dividers)

# bin_names = ['저출력', '보통출력', '고출력']

# df['hp_bins'] = pd.cut(x = df['horsepower'], bins = bin_dividers, labels = bin_names, include_lowest = True)
# print(df[['horsepower', 'hp_bins']].head(15))

#--------------------더미변수--------------------------
# horsepower_dummies = pd.get_dummies(df['hp_bins'], dtype = int)
# print(horsepower_dummies.head(15))
#-------------원핫인코딩------------------------------------
# from sklearn import preprocessing
# label_encoder = preprocessing.LabelEncoder()
# onehot_encoder = preprocessing.OneHotEncoder()

# onehot_laebeled = label_encoder.fit_transform(df['hp_bins'].head(15))
# print(onehot_laebeled)

# onehot_reshaped = onehot_laebeled.reshape(len(onehot_laebeled), 1)
# print(onehot_reshaped)
# print(type(onehot_reshaped))

# onehot_fitted = onehot_encoder.fit(onehot_reshaped)
# print(onehot_fitted)
# print(type(onehot_fitted))

#---------------------------정규화-------------------------

# print(df.horsepower.describe())
# print('\n')

# df.horsepower = df.horsepower / abs(df.horsepower).max()

# print(df.horsepower.head())
# print('\n')
# print(df.horsepower.describe())

#--다른방법

# print(df.horsepower.describe())
# print('\n')

# min_x = df.horsepower - df.horsepower.min()
# min_max = df.horsepower.max() - df.horsepower.min()
# df.horsepower = min_x / min_max

# print(df.horsepower.head())
# print('\n')
# print(df.horsepower.describe())

#---------다른 자료형을 시계열 객체로 변환-------------------------
df = pd.read_csv('C:\\Users\\ejong\\Desktop\\coding\\0602_pandas_1\\stock-data.csv')
# print(df.head())
# print('\n')
# print(df.info())
#---------------문자열을 timestamp로 변환-------------

df['new_Date'] = pd.to_datetime(df['Date'])

# print(df.head())
# print(df.info())
# print(type(df['new_Date'][0]))

#------------다른 자료형을 시계열 객체로 변환-------------
# df.set_index('new_Date', inplace = True)
# df.drop('Date', axis = 1, inplace = True)

# print(df.head())
# print('\n')
# print(df.info())

#-----------------Timestamp를 Period로 변환---------------------
# dates = ['2019-01-01', '2020-03-01', '2021-06-01']
# ts_dates = pd.to_datetime(dates)
# print(ts_dates)
# print('\n')

# pr_day = ts_dates.to_period(freq = 'D')
# print(pr_day)
# pr_month = ts_dates.to_period(freq = 'M')
# print(pr_month)
# pr_year = ts_dates.to_period(freq = 'Y')
# print(pr_year)

#--------------Timestamp 배열---------------------------

# ts_ms = pd.date_range(start = '2019-01-01', end = None, periods = 6, freq = 'MS', tz = 'Asia/Seoul')
# print(ts_ms)

# ts_3m = pd.date_range(start = '2019-01-01', periods = 6, freq = '3ME', tz = 'Asia/Seoul')
# print(ts_3m)

#---------------------period---------------------

# pr_m = pd.period_range(start = '2019-01-01', end = None, periods =  6, freq = 'M')
# print(pr_m)
# pr_h = pd.period_range(start = '2019-01-01', end = None, periods = 3, freq = 'h')
# print(pr_h)
# pr_2h = pd.period_range(start = '2019-01-01', end = None, periods = 3, freq = '2h')
# print(pr_2h)

#-----------------------날짜 데이터 분리---------------------
# print(df.head())
# print('\n')

df['Year'] = df['new_Date'].dt.year
df['Month'] = df['new_Date'].dt.month
df['Day'] = df['new_Date'].dt.day
# print(df.head())

df['Date_yr'] = df['new_Date'].dt.to_period(freq = 'Y')
df['Date_m'] = df['new_Date'].dt.to_period(freq = 'M')
# print(df.head())

# df.set_index('Date_m', inplace = True)
# print(df.head())

df['new_Date'] = pd.to_datetime(df['Date'])
df.set_index('new_Date', inplace = True)

print(df.head())
print('\n')
print(df.index)