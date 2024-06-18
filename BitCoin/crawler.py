import os
import requests
import json
from datetime import datetime
import urllib.parse

def save_data_to_file(data, file_name):
    try:
        # 确保目录存在
        os.makedirs(os.path.dirname(file_name), exist_ok=True)
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)
        print(f"Data saved to {file_name}")
    except Exception as e:
        print(f"Failed to save data to {file_name}: {e}")

# 创建data目录
os.makedirs('data', exist_ok=True)

# 定义基础URL
base_url = "https://www.binance.com/bapi/composite/v2/friendly/pgc/content/queryByHashtag"
hashtag = "%23BitCoin"

# 先解码 变人话
decoded_hashtag = urllib.parse.unquote(hashtag)

# 去掉开头的# 这里是人话
tag_name = decoded_hashtag[1:]

params_template = "?hashtag={}&pageIndex={}&pageSize=20&orderBy=LATEST"

# 定义请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "TE": "Trailers"
}

# 初始化存储数据的字典
response_data = {
    "code": "000000",
    "message": None,
    "messageDetail": None,
    "data": {
        "hashtag": None,
        "feedData": []
    }
}

# 遍历页数
for page_index in range(1, 3):
    url = base_url + params_template.format(hashtag, page_index)
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # 抛出异常，如果响应状态码不为200
        data = response.json()
        
        # 将hashtag信息保存到response_data
        if page_index == 1:
            response_data["data"]["hashtag"] = data.get("data", {}).get("hashtag", {})

        # 获取feedData
        feed_data = data.get("data", {}).get("feedData", [])
        
        # 将feedData内容添加到response_data中
        response_data["data"]["feedData"].extend(feed_data)

    except requests.RequestException as e:
        print(f"Failed to retrieve data from page {page_index}: {e}")
        # 更新错误信息
        response_data["code"] = "000001"
        response_data["message"] = "Failed to retrieve data"
        response_data["messageDetail"] = f"Failed to retrieve data from page {page_index}: {str(e)}"

# 生成当前时间的字符串
current_time_str = datetime.now().strftime("%Y%m%d%H%M%S")

# 生成文件名
file_name = f"data/{tag_name}/catch_{current_time_str}.json"

# 保存到文件
save_data_to_file(response_data, file_name)
