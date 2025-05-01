import requests
import time
from fake_useragent import UserAgent

url="https://www.gobritanya.com/student-residences/london"

session = requests.Session()

headers = {
    "User-Agent": UserAgent().random,
    "Accept-Language": "en-US,en;q=0.9",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
    "Referer": 'https://www.gogle.com/',
}

time.sleep(2)
r = session.get(url)
# print(r.text)
with open("file.html", "w") as f:
    f.write(r.text)