import os
import re
import shutil

brain_dir = r"C:\Users\payal\.gemini\antigravity\brain\a618ccb7-95de-447c-85a3-a9b2fd5bf2a9"
dest_dir = r"C:\Users\payal\.gemini\antigravity\scratch\the-district-design\images"

# Find the generated image
img_path = None
for f in os.listdir(brain_dir):
    if f.startswith("hero_clean_bg") and f.endswith(".png"):
        img_path = os.path.join(brain_dir, f)
        break

if img_path:
    dest_path = os.path.join(dest_dir, "hero_clean_bg.png")
    shutil.copy2(img_path, dest_path)
    print("Copied image to", dest_path)

# Update index.html
html_path = r"C:\Users\payal\.gemini\antigravity\scratch\the-district-design\index.html"
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Replace background image and add cache busting
html = re.sub(r'style="background-image:[^"]*"', '', html)
html = html.replace('id="hero"', 'id="hero" style="background-image: url(\'/images/hero_clean_bg.png?v=3\'); background-size: cover; background-position: center; color: #1A0B13;"')

# Cache bust css
html = html.replace('href="/index.css"', 'href="/index.css?v=4"')

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html")

# Remove gradient border from index.css
css_path = r"C:\Users\payal\.gemini\antigravity\scratch\the-district-design\index.css"
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Remove the #ai custom styles that we added in fix_css.py
css = re.sub(r'#ai \.section__inner \{[^}]*\}\s*#ai \.section__inner::after \{[^}]*\}', '', css)

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)
print("Removed gradient border from index.css")

