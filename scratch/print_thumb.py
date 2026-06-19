import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

match = re.search(r'<picture id="video-overlay-thumb">.*?</picture>', html, re.DOTALL)
if match:
    print(match.group())
else:
    print("No match")
