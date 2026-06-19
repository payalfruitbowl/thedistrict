import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Hide canvas again to avoid ghost coaster
content = content.replace('style="opacity: 1;"', 'style="opacity: 0 !important;"')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Canvas hidden")
