import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the hidden canvas
content = content.replace('style="opacity: 0 !important;"', 'style="opacity: 1;"')

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Unhid canvas in index.html")
