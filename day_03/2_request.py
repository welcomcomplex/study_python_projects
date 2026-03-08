import requests

res = requests.get('http://api.tianapi.com/guonei/?key=APIKey&num=10')
if res.status_code == 200:
    data = res.json()
    for news in data['newslist']:
        print(news['title'])
        print(news['url'])
        print('-' * 60)
