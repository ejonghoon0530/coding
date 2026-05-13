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

#plt.plot(sr_one.index, sr_one.values)
#plt.plot(sr_one)

plt.style.use('ggplot')

plt.figure(figsize = (14, 5))

plt.xticks(size = 10,rotation = 'vertical')
plt.plot(sr_one.index, sr_one.values)

plt.title('서울 -> 경기 인구 이동', size = 30)
plt.xlabel('기간', size = 20)
plt.ylabel('이동 인구수', size = 20)

plt.legend(labels = ['서울 -> 경기'], loc = 'best', fontsize = 15)

plt.ylim(50000, 800000)

plt.annotate('',
             xy = (20, 620000),
             xytext = (2, 290000),
             xycoords = 'data',
             arrowprops = dict(arrowstyle = '->', color = 'skyblue', lw = 5))
plt.annotate('',
             xy = (47, 450000),
             xytext = (30, 580000),
             xycoords = 'data',
             arrowprops = dict(arrowstyle = '->', color = 'olive', lw = 5))

plt.annotate('인구 이동 증가 (1970 - 1995)',
             xy = (10, 400000),
             rotation = 24,
             va = 'baseline',
             ha = 'center',
             fontsize = 15)
plt.annotate('인구 이동 감소 (1995 - 2017)',
             xy = (40, 520000),
             rotation = -10,
             va = 'baseline',
             ha = 'center',
             fontsize = 15)
plt.show()

print(plt.style.available)