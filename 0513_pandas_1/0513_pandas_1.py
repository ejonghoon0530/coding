import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0513_pandas_1\\시도별 전출입 인구수.xlsx', engine = 'openpyxl', header = 0)
    
df = df.ffill()

mask = (df['전출지별'] == '서울특별시') & (df['전입지별'] != '서울특별시')
df_seoul = df[mask]
df_seoul = df_seoul.drop(['전출지별'], axis = 1)
df_seoul = df_seoul.rename({'전입지별' : '전입지'}, axis = 1)
df_seoul.set_index('전입지', inplace = True)

df_seoul.head()

sr_one = df_seoul.loc['경기도']
sr_one.head()

from matplotlib import font_manager, rc
font_path = 'C:\\Windows\\Fonts\\malgun.ttf'
font_name = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font_name)

#------------------------화면 분활하여 그래프 여러개 그리기---------------------------

# fig = plt.figure(figsize = (10, 10))
# ax1 = fig.add_subplot(2, 1, 1)
# ax2 = fig.add_subplot(2, 1, 2)

# ax1.plot(sr_one, 'o', markersize = 10)
# ax2.plot(sr_one, marker = 'o', markerfacecolor = 'green', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 경기')

# ax1.set_ylim(5000, 800000)
# ax2.set_ylim(5000, 800000)

# ax1.set_xticklabels(sr_one.index, rotation = 75)
# ax2.set_xticklabels(sr_one.index, rotation = 75)

# plt.show()
#----------------------------------------------------------------

#------------------------선그래프------------------------
#plt.plot(sr_one.index, sr_one.values)
#plt.plot(sr_one)

# plt.style.use('ggplot')

# plt.figure(figsize = (14, 5))

# plt.xticks(size = 10,rotation = 'vertical')
# plt.plot(sr_one.index, sr_one.values)

# plt.title('서울 -> 경기 인구 이동', size = 30)
# plt.xlabel('기간', size = 20)
# plt.ylabel('이동 인구수', size = 20)

# plt.legend(labels = ['서울 -> 경기'], loc = 'best', fontsize = 15)

# plt.ylim(50000, 800000)

# plt.annotate('',
#              xy = (20, 620000),
#              xytext = (2, 290000),
#              xycoords = 'data',
#              arrowprops = dict(arrowstyle = '->', color = 'skyblue', lw = 5))
# plt.annotate('',
#              xy = (47, 450000),
#              xytext = (30, 580000),
#              xycoords = 'data',
#              arrowprops = dict(arrowstyle = '->', color = 'olive', lw = 5))

# plt.annotate('인구 이동 증가 (1970 - 1995)',
#              xy = (10, 400000),
#              rotation = 24,
#              va = 'baseline',
#              ha = 'center',
#              fontsize = 15)
# plt.annotate('인구 이동 감소 (1995 - 2017)',
#              xy = (40, 520000),
#              rotation = -10,
#              va = 'baseline',
#              ha = 'center',
#              fontsize = 15)
# plt.show()

# print(plt.style.available)
#--------------------------------------------------------------

#---------------------------선그래프 꾸미기1----------------------------
# fig = plt.figure(figsize = (20, 5))
# ax = fig.add_subplot(1, 1, 1)

# ax.plot(sr_one, marker = 'o', markerfacecolor = 'green', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 경기')
# ax.legend(loc = 'best')

# ax.set_ylim(50000, 800000)

# ax.set_title('서울 -> 경기 인구 이동', size = 20)
# ax.set_xlabel('기간', size = 12)
# ax.set_ylabel('이동 인구수', size = 12)
# ax.set_xticklabels(sr_one.index, rotation = 75)

# ax.tick_params(axis = 'x', labelsize = 10)
# ax.tick_params(axis = 'y', labelsize = 10)

# plt.show()

#---------------------------선 그래프 꾸미기2----------------------------
# col_years = list(map(str, range(1970, 2018)))
# df_3 = df_seoul.loc[['충청남도', '경상북도', '강원도'], col_years]

# plt.style.use('ggplot')

# fig = plt.figure(figsize=(20, 5))
# ax = fig.add_subplot(1, 1, 1)

# ax.plot(col_years, df_3.loc['충청남도', :], marker = 'o', markerfacecolor = 'green', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 충남')
# ax.plot(col_years, df_3.loc['경상북도', :], marker = 'o', markerfacecolor = 'blue', markersize = 10, color = 'skyblue', linewidth = 2, label = '서울 -> 경북')
# ax.plot(col_years, df_3.loc['강원도', :], marker = 'o', markerfacecolor = 'red', markersize = 10, color = 'magenta', linewidth = 2, label = '서울 -> 강원')
# ax.legend(loc = 'best')

# ax.set_title('서울 -> 충남, 경북, 강원 인구 이동', size = 20)

# ax.set_xlabel('기간', size = 12)
# ax.set_ylabel('이동 인구수', size = 12)

# ax.set_xticklabels(col_years, rotation = 90)

# ax.tick_params(axis = 'x', labelsize = 10)
# ax.tick_params(axis = 'y', labelsize = 10)

# plt.show()
#--------------------------------------------------------------

#---------------------------선 그래프 꾸미기3----------------------------
# fig = plt.figure(figsize = (20, 5))
# ax = fig.add_subplot(1, 1, 1)

# ax.plot(sr_one, marker = 'o', markerfacecolor = 'green', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 경기')
# ax.legend(loc = 'best')

# ax.set_ylim(50000, 800000)

# ax.set_title('서울 -> 경기 인구 이동', size = 20)
# ax.set_xlabel('기간', size = 12)
# ax.set_ylabel('이동 인구수', size = 12)
# ax.set_xticklabels(sr_one.index, rotation = 75)

# ax.tick_params(axis = 'x', labelsize = 10)
# ax.tick_params(axis = 'y', labelsize = 10)

# plt.show()
#----------------------------------------------------------------

#---------------------------선 그래프 꾸미기4----------------------------
# col_years = list(map(str, range(1970, 2018)))
# df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

# plt.style.use('ggplot')

# fig = plt.figure(figsize=(20, 10))
# ax1 = fig.add_subplot(2, 2, 1)
# ax2 = fig.add_subplot(2, 2, 2)
# ax3 = fig.add_subplot(2, 2, 3)
# ax4 = fig.add_subplot(2, 2, 4)

# ax1.plot(col_years, df_4.loc['충청남도', :], marker = 'o', markerfacecolor = 'green', markersize = 10, color = 'olive', linewidth = 2, label = '서울 -> 충남')
# ax2.plot(col_years, df_4.loc['경상북도', :], marker = 'o', markerfacecolor = 'blue', markersize = 10, color = 'skyblue', linewidth = 2, label = '서울 -> 경북')
# ax3.plot(col_years, df_4.loc['강원도', :], marker = 'o', markerfacecolor = 'red', markersize = 10, color = 'magenta', linewidth = 2, label = '서울 -> 강원')
# ax4.plot(col_years, df_4.loc['전라남도', :], marker = 'o', markerfacecolor = 'orange', markersize = 10, color = 'yellow', linewidth = 2, label = '서울 -> 전남')

# ax1.legend(loc = 'best')
# ax2.legend(loc = 'best')
# ax3.legend(loc = 'best')
# ax4.legend(loc = 'best')

# ax1.set_title('서울 -> 충남 인구 이동', size = 20)
# ax2.set_title('서울 -> 경북 인구 이동', size = 20)
# ax3.set_title('서울 -> 강원 인구 이동', size = 20)
# ax4.set_title('서울 -> 전남 인구 이동', size = 20)

# ax1.set_xticklabels(col_years, rotation = 90)
# ax2.set_xticklabels(col_years, rotation = 90)
# ax3.set_xticklabels(col_years, rotation = 90)
# ax4.set_xticklabels(col_years, rotation = 90)

# plt.show()

#----------------------------------------------------------------

#------------------------------matplotlib에서 사용할 수 있는 색의 종류-------------------------------
# import matplotlib

# colors = {}

# for name, hex in matplotlib.colors.cnames.items():
#     colors[name] = hex
# print(colors)

#----------------------------------------------------------------------

#-----------------------------면적 그래프--------------------------------------
# col_years = list(map(str, range(1970, 2018)))
# df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
# df_4 = df_4.transpose()

# plt.style.use('ggplot')

# df_4.index = df_4.index.map(int)

# df_4.plot(kind = 'area', stacked = True, alpha = 0.2, figsize = (20, 10))

# plt.title('서울 -> 타시도 인구 이동', size = 30)
# plt.ylabel('이동 인구수', size = 20)
# plt.xlabel('기간', size = 20)
# plt.legend(loc = 'best', fontsize = 15)
# plt.show()
#----------------------------------------------------------------------
#------------------------막대그래프-----------------------------------
# col_years = list(map(str, range(2010, 2018)))
# df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]
# df_4 = df_4.transpose()

# df_4.index = df_4.index.map(int)

# df_4.plot(kind = 'bar', figsize = (20, 10), width = 0.7, color = ['orange', 'green', 'skyblue', 'blue'])
# plt.title('서울 -> 타시도 인구 이동', size = 30)
# plt.ylabel('이동 인구수', size = 20)
# plt.xlabel('기간', size = 20)
# plt.ylim(500, 30000)
# plt.legend(loc = 'best', fontsize = 15)
# plt.show()

#----------------------------------------------------------------------

#---------------------------수평막대------------------------
col_years = list(map(str, range(2010, 2018)))
df_4 = df_seoul.loc[['충청남도', '경상북도', '강원도', '전라남도'], col_years]

df_4['합계'] = df_4.sum(axis = 1)

df_total = df_4[['합계']].sort_values(by = '합계', ascending = True)

plt.style.use('ggplot')

df_total.plot(kind = 'barh', color = 'cornflowerblue', width = 0.5, figsize = (10, 5))

plt.title('서울 -> 타시도 인구 이동')
plt.xlabel('이동 인구수')
plt.ylabel('전입지')
plt.show()
#----------------------------------------------------------------------