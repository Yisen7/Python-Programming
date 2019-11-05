import requests
import json

if __name__ == '__main__':
    # 目标url
    url = "https://www.toutiao.com/api/pc/realtime_news/"
    # 发送请求，获取服务器响应数据
    response = requests.get(url)
    results = response.text
    resultData = json.loads(results)
    # 将标题全部取出， resultData["data"] ---列表[字典]
    for data in resultData["data"]:
        print(data["title"])

