#---------------------------------막대그래프---------------------------------#
# import pandas as pd
# import matplotlib.pyplot as plt


# from matplotlib import font_manager, rc
# plt.rc('font', family = 'NanumBarunGothic')

# plt.style.use('ggplot')
# plt.rcParams['axes.unicode_minus'] = False

# df = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0513_pandas_1\\남북한발전전력량3.xlsx', engine = 'openpyxl')
# df = df.loc[6 : 9]
# df.drop('전력량 (억kWh)', axis = 'columns', inplace = True)
# df.set_index('발전 전력별', inplace = True)
# df = df.T

# df = df.rename(columns = {'합계': '총발전량'})
# df['총발전량 - 1년'] = df['총발전량'].shift(1)
# df['증감률'] = ((df['총발전량'] / df['총발전량 - 1년']) - 1) * 100

# ax1 = df[['수력', '화력']].plot(kind = 'bar', figsize = (20, 20), width = 0.7, stacked = True)
# ax2 = ax1.twinx()
# ax2.plot(df.index, df['증감률'], ls = '--', marker = 'o', markersize = 20, color = 'red', label = '전년대비 증감률(%)')

# ax1.set_ylim(0, 500)
# ax2.set_ylim(-50, 50)

# ax1.set_xlabel('연도', size = 20)
# ax1.set_ylabel('발전량 (억kWh)')
# ax2.set_ylabel('전년대비 증감률 (%)')

# plt.title('북한 전력 발전량 (2004 - 2023)', size = 30)
# ax1.legend(loc = 'upper left')

# plt.show()
#-----------------------------------------------------------------

#-------------------------히스토그램------------------------------
# from ucimlrepo import fetch_ucirepo

# auto_mpg = fetch_ucirepo(id = 9)

# X = auto_mpg.data.features
# y = auto_mpg.data.targets

# print(X.head())
# print('\n')
# print(y.head())

#----------------------------------------------------------
#---------------------------히스토그램2--------------------

# import pandas as pd
# import matplotlib.pyplot as plt

# plt.style.use('classic')

# y.plot(kind = 'hist', bins = 10, color = 'coral', figsize = (10, 5))

# plt.title('Histogram')
# plt.xlabel('mpg')
# plt.show()

#---------------------------------------------------------------
#---------------------------산점도-----------------------------------

# plt.style.use('default')

#df = pd.concat([X, y], axis = 1)

# df.plot(kind = 'scatter', x = 'weight', y = 'mpg', c = 'coral', s = 10, figsize = (10, 5))
# plt.title('Scatter Plot - mpg vs weight')
# plt.show()

#---------------------버플 차트 만들기----------------------------

# cylinders_size = df.cylinders/df.cylinders.max() * 300

# df.plot(kind = 'scatter', x = 'weight', y = 'mpg', c = 'coral', s = cylinders_size, figsize = (10, 5), alpha = 0.3)
# plt.title('Scatter Plot: mpg-weight-cylinders')
# plt.show()
#---------------------------------------------------------------

#--------------------------그림파일로 저장하기-------------------
# df.plot(kind = 'scatter', x = 'weight', y = 'mpg', marker = '+', cmap = 'viridis', c = cylinders_size, s = 50, figsize = (10, 5), alpha = 0.3)
# plt.title('Scatter Plot: mpg-weight-cylinders')
# plt.savefig('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\scatter.png')
# plt.savefig('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\scatter_transparent.png', transparent = True)
# plt.show()

#----------------------------------------------------------------------

#----------------------------파이차트----------------------------
# df['count'] = 1
# df_origin = df.groupby('origin').sum()
# print(df_origin.head())

# df_origin.index = ['USA', 'EU',' JPN']

# df_origin['count'].plot(kind = 'pie', figsize = (7, 5), autopct = '%1.1f%%', startangle = 10, colors = ['chocolate', 'bisque', 'cadetblue'])
# plt.title('Model Origin', size = 20)
# plt.axis('equal')
# plt.legend(labels = df_origin.index, loc = 'upper right')
# plt.show()
#----------------------------------------------------------------------

#-----------------------------박스플롯-----------------------------
# from matplotlib import rc

# plt.rc('font', family = 'Gulim')

# plt.style.use('seaborn-v0_8-poster')
# plt.rcParams['axes.unicode_minus'] = False

# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)

# ax1.boxplot(x = [df[df['origin'] == 1]['mpg'],
#                  df[df['origin'] == 2]['mpg'],
#                  df[df['origin'] == 3]['mpg']],
#             labels = ['USA', 'EU', 'JAPAN'])
# ax2.boxplot(x = [df[df['origin'] == 1]['mpg'],
#                  df[df['origin'] == 2]['mpg'],
#                  df[df['origin'] == 3]['mpg']],
#             labels = ['USA', 'EU', 'JAPAN'],
#             vert = False)

# ax1.set_title('제조국가별 연비 분포 (수직 박스 플롯)')
# ax2.set_title('제조국가별 연비 분포 (수평 박스 플롯)')

# plt.show()

#----------------------------------------------------------------------

#-------------------회귀선이 있는 산점도----------------------  
import matplotlib.pyplot as plt
import seaborn as sns

titanic = sns.load_dataset('titanic')

# sns.set_style('darkgrid')

# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)

# sns.regplot(x = 'age', y = 'fare', data = titanic, ax = ax1)

# sns.regplot(x = 'age', y = 'fare', data = titanic, ax = ax2, fit_reg = False)

# plt.show()
#----------------------------------------------------------------------
#----------------히스토그램/커널 밀도 그래프------------------
# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)

# sns.distplot(titanic['fare'], ax = ax1)
# sns.kdeplot(x = 'fare', data = titanic, ax = ax2)
# sns.histplot(x = 'fare', data = titanic, ax = ax3)

# ax1.set_title('titanic fare - hist + kde')
# ax2.set_title('titanic fare - kde')
# ax3.set_title('titanic fare - hist')

# plt.show()
#----------------------------------------------------------------

#------------------히트맵----------------------
table = titanic.pivot_table(index = ['sex'], columns = ['class'], aggfunc = 'size')

sns.heatmap(table, annot = True, fmt = 'd', linewidth = 0.5, cmap = 'YlGnBu', cbar = False)

plt.show()
#----------------------------------------------------------------------


