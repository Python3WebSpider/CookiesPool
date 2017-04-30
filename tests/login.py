import requests
from bs4 import BeautifulSoup

cookies = {
    'SSOLoginState': '1493555070',
    'SCF': 'ArrMd41qtHmW87eTIsI-sT1IjDG8oncB9A0HbSmyDw1FwO5sbI_j6_ZellQQ07ZjTXTIBrM3Y_tpKym39f1tYWs.',
    'SUB': '_2A250AacuDeRhGeRG6FIX9ybIzDiIHXVXDclmrDV6PUJbktBeLVfCkW18FWjD8r3ddYXy2abmqSauclujaw..',
    '_T_WM': '5e9c698a350ddeba1c5d77e1958af21b', 'ALF': '1496147067', 'SUHB': '0G0vWR88D2VokZ',
    'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9W5APD86CuQDllBusA-6OZaq5JpX5o2p5NHD95QE1he7SoMRShMXWs4Dqcjci--fi-zXiK.Xi--fi-iWiKnci--ciKn4iKy2i--Xi-zRi-2Ri--4iKL2iK.4i--Ri-2NiKnf'
}

response = requests.get('http://weibo.cn', cookies=cookies)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    title = soup.title.string
    print(title)
