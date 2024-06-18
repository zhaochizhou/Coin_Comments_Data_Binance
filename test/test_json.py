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
json_file = "catch_20240618030846.json"
get_content_and_date(json_file)
