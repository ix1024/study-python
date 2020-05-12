import requests
import time
from bs4 import BeautifulSoup


class FetchHtml:
    '''
    获取HTML
    '''
    def __init__(self, url, method='get', data={}, headers={}):
        self.url = url  #URL地址
        self.method = method  #方法
        self.data = data  # post 方法数据
        self.headers = headers  #Headers

    #静态方法，保存文件
    @classmethod
    def saveFile(cls, fileName, content):
        fs = open(fileName, mode='w', encoding='utf-8')
        fs.write(content)
        fs.close()
        return fileName

    #获取指定HTML
    def select(self, query=None):
        if self.method == 'get':
            res = requests.get(self.url)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text)
            if res.status_code >= 300:
                return '错误:' + str(res.status_code)
            else:
                if query != None:
                    return soup.select(query)
                else:
                    return soup
        elif self.method == 'post':
            res = requests.post(self.url, data=self.data, headers=self.headers)
            res.encoding = 'utf-8'
            soup = BeautifulSoup(res.text)
            if res.status_code >= 300:
                return '错误:' + str(res.status_code)
            else:
                if query != None:
                    return soup.select(query)
                else:
                    return soup
        else:
            return '不支持的方法'


def run():
    host = 'https://www.open-open.com'
    for page in range(1, 1):
        content = FetchHtml(host + '/news/qianduan-jishu/?page=' + str(page))
        contentList = content.select('.item.ut-pd10 h2.header a')
        # print(contentList)
        index = 0
        for item in contentList:
            index += 1
            url = host + item.attrs['href']
            # print('第', page, '页 第', index, '条', item.get_text())
            content = FetchHtml(url)
            contentList = content.select('html')
            print(url)
            # print(contentList)
            path = './html/' + str(page) + '-' + str(index) + '.html'
            FetchHtml.saveFile(path, str(contentList[0]))


run()
