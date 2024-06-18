# 币安评论记录数据集 Binance Comments Record Dataset

## 调用 Call

**from jsdelivr**
``` bash

https://

```

## 位置 Location

`Coin_Comments_Data_Binance/{币种}/data/catch_{日期}.json`

## json结构  Json Structure

```json
{
    "code": "000000",
    "message": null,
    "messageDetail": null,
    "data": [
        {
            "id": ...,
            "content": ...,
            "date": ...,
            "..." : ...,
        },
        ...
    ]
}

```

### python解析示例 Python Parsing Example

```python
import json

def get_content_and_date(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
            feed_data = data.get("data", [])
            for item in feed_data:
                content = item.get("content")
                date = item.get("date")
                if content and date:
                    print(f"Content: {content}")
                    print(f"Date: {date}")
                    print()
                else:
                    print("Content or Date not found for an item.")
    except Exception as e:
        print(f"Failed to read JSON file {json_file}: {e}")

# 测试示例
json_file = "{date}.json"
get_content_and_date(json_file)

```

## 注意 Attention !

本仓库内的.py(python).sh.md为后缀的文件遵照MIT协议。

The .py(python).sh(shell).md(markdown) files in this library are under the MIT agreement.

本仓库内存储.txt / .json 文件中内容是爬取到的，这些内容仅供学习交流，严禁用于商业用途。


The content in the .txt and .json file stored in this library is obtained from crawler. Contents in such file are only provided for learning and communication, and are strictly prohibited for commercial use.

如果我们的爬取行为侵犯到了您的合法权益，请使用能代表您机构或个人的官方的电子邮件联系 zhaochizhou@outlook.com

If our crawling behavior infringes upon your legitimate rights and interests, please use the official email representing your organization or individual to contact zhaochizhou@outlook.com

