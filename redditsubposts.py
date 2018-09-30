import requests
import time
from notify_run import Notify

class Posts:

    def __init__(self, subreddit, sort_mthd,**kwargs):
        self.subreddit=str(subreddit)
        self.sort_mthd = str(sort_mthd)
        self.link = 'https://www.reddit.com/r/{}/{}.json'.format(subreddit,sort_mthd)
        self.search_args = kwargs.get('search_args',None)
        if self.search_args!=None and type(self.search_args)!=type(dict()):
            raise Exception('search_args is type '+str(type(self.search_args)) + '. Expected dict.')
        self.header_args = kwargs.get('header_args',None)

    def retrieve_posts(self, **status):
        data = self.search_args
        header = {'User-agent':self.header_args}
        r=requests.get(self.link, data=data, headers = header)
        self.r = r
        r_status = r.status_code
        if self.header_args == None and r_status ==429:
            raise Exception('429 Error, please specify a user in init statement using header_args = \'User\'')
        if status.get('type',None)=='status':
            return r.status_code, r
        if status.get('type',None)=='json':
            return r.json()
        if status.get('type',None)=='post':
            return r.json()['data']['children']
        return r

    def a_post(self,r):
        return r.json()['data']['children']

class PostInfo:

    def __init__(self,post_json, **kwarg):
        number = kwarg.get('number',0)
        self.title = post_json[number]['data']['title']
        self.score = post_json[number]['data']['score']
        self.age = post_json[number]['data']['created']
        self.age_m = int((time.time()-self.age+8*3600)//60)
        self.permalink = 'http://www.reddit.com'+post_json[number]['data']['permalink']

    def PostInfo_other(self,other,**kwarg):
        number = kwarg.get('number',0)
        return post_json[number]['data']['{}'.format(other)]

    def build_post(self, **kwarg):
        width = kwarg.get('width',100)
        title_cut = self.title
        temp_len = len(str(self.age_m)+str(self.score)+'   minutes ago. Score: ')
        l_width = width-temp_len
        if len(self.title)>l_width-5:
            title_cut=self.title[:l_width-8]+'...'
        print()
        print(str(title_cut).ljust(width-temp_len) + (('Score: {} | {} minutes ago.').format(self.score,self.age_m)).rjust(1))
        print('-'*width)
        return



if __name__ == '__main__':

    search1=Posts('MemeEconomy','new',search_args={'limit':100,'count':10},header_args='User1')

    search1_retrieve = search1.retrieve_posts(type='post')
    for i in range(15):
        posty=PostInfo(search1_retrieve,number=i)
        if int(posty.age_m)>30:
            break
        posty.build_post(width=70)
