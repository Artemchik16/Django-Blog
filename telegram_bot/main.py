import requests
import json
from datetime import datetime

url = requests.get('http://127.0.0.1:8000/api/v1/posts/')
posts_deserializer_data = json.loads(url.text)

results = []
# print(deserializer_data)
for post in posts_deserializer_data.get('results'):
    result = {}
    result['tags'] = post.get('tags')
    result['author'] = post.get('created_by').get('username')
    result['title'] = post.get('title')
    result['content'] = post.get('content')
    created_at_str = post.get('created_at')
    result['created_at'] = datetime.fromisoformat(created_at_str).strftime('%Y-%m-%d %H:%M:%S')
    results.append(result)

print(results)