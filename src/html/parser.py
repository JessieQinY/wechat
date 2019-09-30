from lxml import etree

import requests


class HtmlError(Exception):
    pass


class HtmlParser:
    def __init__(self, url):
        resp = requests.get(url)
        if not str(resp.status_code).startswith('2'):
            raise HtmlError
        self.text = resp.text
        self.tree = etree.HTML(self.text)

    def find_element_by_xpath(self, xpath):
        return self.tree.xpath(xpath)


if __name__ == '__main__':
    temp = 'https://github.com/ruanyf/weekly'
    te = HtmlParser(temp)
    ele = te.find_element_by_xpath('//article/p[3]/a[1]/@href')
    print(ele)
