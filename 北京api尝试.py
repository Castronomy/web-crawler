#coding=utf-8
# 1623308840788
#
#
# http://data.beijing.gov.cn/cms/web/APIInterface/userApply.jsp?id="3043980837"&key="1623308840788"

import urllib.request as request


url1='http://data.beijing.gov.cn/cms/web/APIInterface/userApply.jsp'
id=3043980837
id=str(id)
url=url1+'?'+'id='+id+'&key="1623308840788"'
url=str(url)
print(url)
graph_output = request.urlopen(url).read()
print(graph_output.decode())