import requests
import time
import os
import urllib.request
from bs4 import BeautifulSoup
url='https://data.beijing.gov.cn/cms/web/APIInterface/dataDoc.jsp?contentID='

def getid():
    i=52742
    s=[]
    for i in range(52740,52751):
        i+=1
        print(i)
        # try:
        url1=url+str(i)
        r = requests.get(url1)
        # 进入网站
        r.raise_for_status()
        # 专门与异常打交道的方法，能够判断返回的Response类型状态是不是200。如果是200，他将表示返回的内容是正确的，
        # 如果不是200，他就会产生一个HttpError的异常。
        r.encoding = r.apparent_encoding
        # 把修改响应头的编码为 request 分析后认为可能性最大的编码
        # print(r.text)
        soup = BeautifulSoup(r.text, 'html.parser')
        # 定义soup，便于信息网站抽取

        t=[]
        for item in soup.find_all('table',class_='content-tab'):
            soup2=item.tbody
            # print(soup2)
            for i in soup2.find_all('td'):
                t.append(i.string)
            print(t)
            s.append(t[-1])
            # time.sleep(5)
        # except:
        #     continue
    print(s)

def getjson():
    id = 3047073376
    import urllib.request as request
    import json
    url1 = 'http://data.beijing.gov.cn:80/cms/web/APIInterface/userApply.jsp'

    id = str(id)
    url = url1 + '?' + 'id=' + id + '&key=1623308840788'
    url = str(url)
    # headers = {'User-Agent': 'User-Agent:Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'}
    print(url)
    # dt=request.Request(url)
    graph_output = request.urlopen(url).read()
    print(graph_output.decode())
    json1 = json.loads(graph_output.decode())
    print(json1['error_code'])

def getfile():
    url1 = 'http://data.beijing.gov.cn:80/docs/2021-04/20210411013431622049.zip'
    # 可尝试id 30440
    import urllib.request  # url request
    import os
    import requests  # dirs

    url = "https://data.beijing.gov.cn"
    s = requests.session()
    # 登录
    response = s.post(url, data={"txtUsr_id": "00000001", "txtPassword": "mima"})

    import time
def download(Directory):
    # for i in range(0,40000):

    headers = {'User-Agent',
               'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/64.0.3282.186 Safari/537.36'}
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]

    url = str(url1)
    i = '1.zip'

    filename = os.path.join(Directory, i)
    print('正在下载', filename)
    urllib.request.urlretrieve(url, filename)
    print('成功')

download(r'C:\Users\GYHfresh\Desktop\中国移动')
