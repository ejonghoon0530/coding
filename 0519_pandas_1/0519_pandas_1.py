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
# import matplotlib.pyplot as plt
# import seaborn as sns

# titanic = sns.load_dataset('titanic')

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
# table = titanic.pivot_table(index = ['sex'], columns = ['class'], aggfunc = 'size')

# sns.heatmap(table, annot = True, fmt = 'd', linewidth = 0.5, cmap = 'YlGnBu', cbar = False)

# plt.show()
#----------------------------------------------------------------------
#------------------범주형 데이터의 산점도----------------------
# sns.set_style('whitegrid')

# fig = plt.figure(figsize = (15, 50))
# ax1 = fig.add_subplot(1, 2, 1)
# ax2 = fig.add_subplot(1, 2, 2)

# # sns.stripplot(x = 'class', y = 'age', data = titanic, ax = ax1, hue = 'class')
# # sns.swarmplot(x = 'class', y = 'age', data = titanic, ax = ax2, hue = 'class')

# sns.stripplot(x = 'class', y = 'age', data = titanic, ax = ax1, hue = 'sex')
# sns.swarmplot(x = 'class', y = 'age', data = titanic, ax = ax2, hue = 'sex')

# ax1.set_title('Strip plot')
# ax2.set_title('Swarm plot')

# plt.show()
#-----------------------막대그래프----------------------------------
# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)

# sns.barplot(x = 'sex', y = 'survived', data = titanic, ax = ax1)

# sns.barplot(x = 'sex', y = 'survived', hue = 'class', data = titanic, ax = ax2)

# sns.barplot(x = 'sex', y = 'survived', hue = 'class', dodge = False, data = titanic, ax = ax3)

# ax1.set_title('titanic survived - sex')
# ax2.set_title('titanic survived - sex/class')
# ax3.set_title('titanic survived - sex/class(stacked)')

# plt.show()

#-----------------------------------------------------------------------
#------------------------빈도그래프------------------------

# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(1, 3, 1)
# ax2 = fig.add_subplot(1, 3, 2)
# ax3 = fig.add_subplot(1, 3, 3)

# sns.countplot(x = 'class', hue = 'who', palette = 'Set1', data = titanic, ax = ax1)

# sns.countplot(x = 'class', hue = 'who', palette = 'Set2', data = titanic, ax = ax2)

# sns.countplot(x = 'class', hue = 'who', palette = 'Set3', dodge = False, data = titanic, ax = ax3)

# ax1.set_title('titanic class')
# ax2.set_title('titanic class - who')
# ax3.set_title('titanic class - who (stacked)')

# plt.show()

#-----------------------------------------------------------------------
#------------------------박스플롯/바이올린 그래프---------------------

# fig = plt.figure(figsize = (15, 5))
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

# sns.boxplot(x = 'alive', y = 'age', data = titanic, ax = ax1)
# sns.boxplot(x = 'alive', y = 'age', hue = 'sex', data = titanic, ax = ax2)

# sns.violinplot(x = 'alive', y = 'age', data = titanic, ax = ax3)
# sns.violinplot(x = 'alive', y = 'age', hue = 'sex', data = titanic, ax = ax4)

# plt.show()

#-----------------------------------------------------------------------
#------------------------조인트 그래프-----------------------------
# j1 = sns.jointplot(x = 'fare', y = 'age', data = titanic)

# j2 = sns.jointplot(x = 'fare', y = 'age', data = titanic, kind = 'reg')
# j3 = sns.jointplot(x = 'fare', y = 'age', data = titanic, kind = 'hex')
# j4 = sns.jointplot(x = 'fare', y = 'age', data = titanic, kind = 'kde')

# j1.fig.suptitle('titanic fare - scatter', size = 15)
# j2.fig.suptitle('titanic fare - reg', size = 15)
# j3.fig.suptitle('titanic fare - hex', size = 15)
# j4.fig.suptitle('titanic fare - kde', size = 15)

# plt.show()

#------------------------pairplot------------------------

# titanic_pair = titanic[['age', 'pclass', 'fare']]
# g = sns.pairplot(titanic_pair)
# plt.show()

#--------------------------------------------------
#-------------------Folium 라이브러리------------------------

#import folium

# seoul_map = folium.Map(location = [37.55, 126.98], zoom_start = 12)

# seoul_map.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\seoul_map.html')

#-----------------------------------------------------------------
# seoul_map2 = folium.Map(location = [37.55, 126.98], tiles = 'OpenstreetMap', zoom_start = 12)
# seoul_map3 = folium.Map(location = [37.55, 126.98], tiles = 'Cartodb Positron', zoom_start = 10)

# seoul_map2.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\seoul_map2.html')
# seoul_map3.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\seoul_map3.html')    

#----------------------------------------------------------------------
# import pandas as pd
# import folium

# df  = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0513_pandas_1\\서울지역 대학교 위치.xlsx')

# seoul_map = folium.Map(location = [37.55, 126.98], tiles = 'OpenStreetMap', zoom_start = 12)

# # for name, lat, lng in zip(df.학교명, df.위도, df.경도):
# #     folium.Marker([lat, lng], popup = name).add_to(seoul_map)
    
# # seoul_map.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\seoul_map_univ.html')

# for name, lat, lng in zip(df.학교명, df.위도, df.경도):
#     folium.CircleMarker([lat, lng], radius = 10, color = 'brown', fill = True, fill_color = 'coral', fill_opacity = 0.7, popup = name).add_to(seoul_map)
# seoul_map.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\seoul_map_univ2.html')

#----------------------------------------------------------------------
#--------------------지도에 단계구분도 표시하기-----------------------
import json
import pandas as pd
import folium

file_path = 'C:\\Users\\ejong\\Desktop\\coding\\0513_pandas_1\\경기도인구데이터.xlsx'
df = pd.read_excel(file_path, index_col = '구분', engine = 'openpyxl')
df.columns = df.columns.map(str)
geo_path = 'C:\\Users\\ejong\\Desktop\\coding\\0513_pandas_1\\경기도행정구역경계.json'

try:
    geo_data = json.load(open(geo_path, encoding = 'utf-8'))
except:
    geo_data = json.load(open(geo_path, encoding = 'utf-8-sig'))
    
g_map = folium.Map(location = [37.5502, 126.982], tiles = 'OpenStreetMap', zoom_start = 9)

year = '2017'

folium.Choropleth(geo_data = geo_data, data = df[year], columns = [df.index, df[year]], fill_color = 'YlOrRd', fill_opacity = 0.7,
                  line_opacity = 0.3, threshold_scale = [10000, 100000, 300000, 500000, 700000], key_on = 'feature.properties.name',).add_to(g_map)
g_map.save('C:\\Users\\ejong\\Desktop\\coding\\0519_pandas_1\\gyeonggi_population_'+ year + '.html')
#----------------------------------------------------------------------