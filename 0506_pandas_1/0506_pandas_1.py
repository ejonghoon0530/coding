#------------------CSV 파일 읽기----------------------------
# import pandas as pd

# file_path = 'C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\read_csv_sample.csv'
# df1 = pd.read_csv(file_path)
# print(df1)
# print('\n')

# df2 = pd.read_csv(file_path, header = None)
# print(df2)
# print('\n')

# df3 = pd.read_csv(file_path, index_col = None)
# print(df3)
# print('\n')

# df4 = pd.read_csv(file_path, index_col = 'c0')
# print(df4)

#--------------------------------------------------------
#------------------Excel 파일 읽기----------------------------
# import pandas as pd

# df1 = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\남북한발전전력량.xlsx', engine = 'openpyxl')
# df2 = pd.read_excel('C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\남북한발전전력량.xlsx', engine = 'openpyxl', header = None)

# print(df1)
# print('\n')
# print(df2)
#--------------------------------------------------------
#------------------JSON 파일 읽기----------------------------
# import pandas as pd

# df = pd.read_json('C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\read_json_sample.json')
# print(df)
# print('\n')
# print(df.index)

#--------------------------------------------------------
#-------------------HTML 파일 읽기----------------------------
# import pandas as pd

# url = 'C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\sample.html'

# tables = pd.read_html(url)
# print(len(tables))
# print('\n')

# for i in range(len(tables)):
#     print("tables[%s]" % i)
#     print(tables[i])
#     print('\n')

# df = tables[1]

# df.set_index(['name'], inplace = True)
# print(df)

#--------------------------------------------------------
#-------------------WEB에서 가져오기------------------------
# import requests
# from bs4 import BeautifulSoup
# import re
# import pandas as pd

# url = "https://en.wikipedia.org/wiki/List_of_American_exchange-traded-funds"
# resp = requests.get(url)
# soup = BeautifulSoup(resp.text, 'lxml') 

# items = soup.select('div > ul > li')

# pattern = r'^(.*?) \((.*?) \|(.*?)\)'

# data = []

# for item in items:
#     match = re.findall(pattern, item.text)
#     if match:
#         name, market, ticker = match[0]
#         data.append({'Name' : name.strip(), 'Market' : market.strip(), 'Ticker' : ticker.strip()})
# df = pd.DataFrame(data)
# print(df)
#----------------------------------------------------

# import googlemaps
# import pandas as pd

# my_key = "YOUR_GOOGLE_MAPS_API_KEY"

# maps = googlemaps.Client(key = my_key)

# lat = []
# lng = []

# places = ["서울시청", "국립국악원", "해운대해수욕장"]

# i = 0
# for place in places:
#     i = i + 1
#     try:
#         print(i, place)
#         geo_location = maps.geocode(place)[0].get('geometry')
#         lat.append(geo_location['location']['lat'])
#         lng.append(geo_location['location']['lng'])
#     except:
#         lat.append('')
#         lng.append('')
#         print(i)
# df = pd.DataFrame({'위도' : lat, '경도' : lng}, index = places)
# print('\n')
# print(df)

#--------------------------------------------------------
#-------------------CSV 파일로 저장하기------------------------
# import pandas as pd

# data = {'name' : ['Jerry', 'Riah', 'Paul'],
#         'glgol' : ["A", "A+", "B"],
#         'basic' : ["C", "B", "B+"],
#         'c++' : ["B+", "C", "C+"]}

# df = pd.DataFrame(data)
# df.set_index('name', inplace = True)
# print(df)

# df.to_csv("C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\df_sample.csv", encoding = 'utf-8-sig')

#--------------------------------------------------------

#-------------------JSON 파일로 저장하기------------------------
# import pandas as pd

# data = {'name' : ['Jerry', 'Riah', 'Paul'],
#         'glgol' : ["A", "A+", "B"],
#         'basic' : ["C", "B", "B+"],
#         'c++' : ["B+", "C", "C+"]}

# df = pd.DataFrame(data)
# df.set_index('name', inplace = True)
# print(df)

# df.to_json("C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\df_sample.json")
#--------------------------------------------------------

#-------------------Excel 파일로 저장하기------------------------
# import pandas as pd

# data = {'name' : ['Jerry', 'Riah', 'Paul'],
#         'glgol' : ["A", "A+", "B"],
#         'basic' : ["C", "B", "B+"],
#         'c++' : ["B+", "C", "C+"]}

# df = pd.DataFrame(data)
# df.set_index('name', inplace = True)
# print(df)

# df.to_excel("C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\df_sample.xlsx")
#--------------------------------------------------------

#-------------------여려개의 데이터프레임을 하나의 Excel 파일로 저장하기------------------------
import pandas as pd

data1 = {'name' : ['Jerry', 'Riah', 'Paul'],
        'glgol' : ["A", "A+", "B"],
        'basic' : ["C", "B", "B+"],
        'c++' : ["B+", "C", "C+"]}
data2 = {'c0' : [1, 2, 3],
         'c1' : [4, 5, 6],
         'c2' : [7, 8, 9],
         'c3' : [10, 11, 12],
         'c4' : [13, 14, 15]}

df1 = pd.DataFrame(data1)
df1.set_index('name', inplace = True)
print(df1)
print('\n')

df2 = pd.DataFrame(data2)
df2.set_index('c0', inplace = True)
print(df2)

writer = pd.ExcelWriter("C:\\Users\\ejong\\Desktop\\coding\\0506_pandas_1\\df_excelwriter.xlsx")
df1.to_excel(writer, sheet_name = "sheet1")
df2.to_excel(writer, sheet_name = "sheet2")
writer.close()