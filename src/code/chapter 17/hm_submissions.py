import requests
from operator import itemgetter

# 执行API调用并存储相应
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code："+r.status_code)

# 处理有关每篇文章的信息
submisssion_ids = r.json()
submisssion_dicts = []
for submisssion_id in submisssion_ids[:30]:
    # 对于每篇文章都执行一次API调用
    url = ('https://hacker-news.firebaseio.com/v0/item/'+str(submisssion_id)+'.json')
    submisssion_r = requests.get(url)
    print(submisssion_r.status_code)
    response_dict = submisssion_r.json()

    submisssion_dict = {
        'title':response_dict['title'],
        'link':'http://news.ycombinator.com/item?id='+str(submisssion_id),
        'comments':response_dict.get('descendants', 0)
    }
    submisssion_dicts.append(submisssion_dict)

submisssion_dicts = sorted(submisssion_dicts, key=itemgetter('comments'), reverse=True)

for submisssion_dict in submisssion_dicts:
    print('\nTitle:', submisssion_dict['title'])
    print('Discussion Link:', submisssion_dict['link'])
    print('Comments:', submisssion_dict['comments'])
    print('1111')









