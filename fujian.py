import requests

def getpage():
        ##从主页面中爬取分页面
        ##https://data.fujian.gov.cn/oportal/catalog/index?fileFormat=3&openType=1&page=1   无条件开放
        pass


def geturl():
        ##页面原代码中爬出url
        pass


def getfile():
        ##从url爬文件
        url='https://data.fujian.gov.cn/oportal/catalog/download?cataId=8DD20A4E87B94708A1748D9F3045A9F0&cataName=福建省属公立医院质量信息&idInRc=M4BJQ9d3xs/+CyIyGU5AZAPAadYD9RBTjAPi0VNiiHlTjBDKB+lRZfRYbwx9QKgJ'
        ##可以从页面原代码中爬出来
        urlt='https://data.fujian.gov.cn/orcservice/doc?doc_id=2F2EB2DE0CEB4D3BA80FC0590CA8B5D0&signature=7/E0SQA4rnBFbmEVCetKBVOMEMoH6VFl9FhvDH1AqAk='
        ##跳转后的页面，效果一样

        res=requests.get(url)
        print(res)
        res = requests.get(url).content
        print(res.decode('utf-8','ignore'))#解码查看
        with open("E:\项目\中国移动\crawl_ctw\demo\\fujian.csv", "wb") as f:
                f.write(res)

getfile()
