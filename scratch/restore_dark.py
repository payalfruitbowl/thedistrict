import os

file_path = "index.css"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace the specific variables I hacked earlier
content = content.replace("--color-white: #DA1C5C;", "--color-white: #FFE7D1;")
content = content.replace("--color-white-transparent: #DA1C5C00;", "--color-white-transparent: #FFE7D100;")
content = content.replace("--color-black: #FFE7D1;", "--color-black: #1A0B13;")
content = content.replace("--color-black-transparent: #FFE7D100;", "--color-black-transparent: #1A0B1300;")

# Remove the #ai specific hacks since the whole site will be beautifully dark-plum 
content = content.replace("background-color: #0D0D0D;", "/* removed */")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored global dark theme without blacks")
