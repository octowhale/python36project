通用框架

```python
import requests


def getHtmlText(url):
    try:
        r = requests.get(url, timeout=30)
        # 如果状态码不是200 则应发HTTOError异常
        r.raise_for_status()
        # 设置正确的编码方式
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "Something Wrong!"
```


> request中文文档 http://docs.python-requests.org/zh_CN/latest/user/quickstart.html