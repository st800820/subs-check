import yaml
import requests

with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

print("订阅源数量：", len(config.get("sub_urls", [])))
for url in config.get("sub_urls", []):
    print("检查中：", url)
    try:
        r = requests.get(url, timeout=10)
        print("状态码：", r.status_code)
    except Exception as e:
        print("错误：", e)
