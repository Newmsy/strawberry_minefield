import redditsubposts
from notify_run import Notify
import time
import webbrowser


notify = Notify()
for k in range(12):
    search = redditsubposts.Posts('MemeEconomy','new',search_args={'limit':100,'count':10},header_args='User1')
    retrieve = search.retrieve_posts(type='post')
    for i in range(25):

        posty = redditsubposts.PostInfo(retrieve,number=i)
        if int(posty.age_m)>30:
            break
        print('{} mins, score: {}, {}'.format(posty.age_m,posty.score,posty.title[:25]))
        print('-'*15)

        if int(posty.score)>=(2<*int(posty.age_m))  and int(posty.age_m)<25 and int(posty.age_m)>=10:
            print('Hello {}'.format(posty.title))
            notify.send('{}, score: {}, {} mins'.format(posty.title,posty.score,posty.age_m))
            webbrowser.open(str(posty.permalink))

    for t in range(280):
        time.sleep(0.99)
        print('Seconds Remaining: '+ str(280-t)+'      ',end='\r')
    print('------'+str(k+1)+'------')
