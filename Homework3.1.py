import requests
from bs4 import BeautifulSoup
def build_url(city_coding, year=None, month=None):
    BASE = 'http://www.tianqihoubao.com/aqi/'
    city_base_url = BASE + '{}.html'
    city_date_base_url = BASE + '{}-{}{}.html'
    if year is not None and month is not None:
        month = str(month) if month >= 10 else '0' + str(month)
        return city_date_base_url.format(city_coding, year, month)
    else:
        return city_base_url.format(city_coding)
def parse(url, city_name):
    response = requests.get(url)
    if response.ok:
        html = response.text
        soup = BeautifulSoup(html)
        data_table = soup.table
        content = data_table.contents
        result = []
        for index, c in enumerate(content[1::2]):
            if index == 0:
                result.append(tuple(['城市'] + c.text.split()))
            else:
                result.append(tuple([city_name] + c.text.split()))
        return result

    else:
        if response.status_code == 403:
            print('403 Forbidden! 抓取太快你被拉黑啦~')
data_all=[parse(build_url('hangzhou',2019,i+1),'hangzhou') for i in range(12)]
print(data_all)