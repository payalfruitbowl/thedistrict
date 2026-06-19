import urllib.request
import re

url = "https://www.meshy.ai/3d-models/make-3d-prush-v2-019eda6c-3365-7f5e-9828-a2017b77b74a?utm_medium=referral-program&utm_source=meshy&utm_content=HHXD5H&share_type=3d-models"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    links = re.findall(r'https?://[^\s"\'<>]+?\.glb', html)
    print("Found GLB links:", links)
except Exception as e:
    print("Error:", e)
