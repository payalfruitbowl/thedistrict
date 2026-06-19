import re

with open('index.html', encoding='utf-8') as f:
    html = f.read()

# Find any img tag with alt="Video thumbnail"
matches = re.finditer(r'<img[^>]*alt="Video thumbnail"[^>]*>', html, re.IGNORECASE)
for m in matches:
    print(m.group())

# Find any source or img tags around it
import bs4
soup = bs4.BeautifulSoup(html, 'html.parser')
for img in soup.find_all('img', alt="Video thumbnail"):
    print("Found img:")
    print(img.parent.prettify())
