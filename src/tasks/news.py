from datetime import datetime
from src.html import HtmlParser


def get_weekly_news():
    return GitNews('/ruanyf/weekly').get_news_url('//article/p[3]/a[1]/@href')


def get_hellogit_news():
    return GitNews('/521xueweihan/HelloGitHub').get_news_url('//table//td[1]/a/@href')


class GitNews:
    host = 'https://github.com'

    def __init__(self, project):

        self.readme = HtmlParser(f'{self.host}{project}/blob/master/README.md')

    def _is_latest(self):
        update_time = self.readme.find_element_by_xpath('//relative-time[1]/@datetime')[0]
        update_time = update_time.replace('T', '-')[:13]
        update_time = datetime.strptime(update_time, '%Y-%m-%d-%H')
        current = datetime.utcnow()
        if (current - update_time).seconds < 60*60:
            return True
        return False

    def get_news_url(self, xpath):
        if self._is_latest():
            endpoint = self.readme.find_element_by_xpath(xpath)[0]
            return f'{self.host}{endpoint}'

