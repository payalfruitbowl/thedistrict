import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add hero background image back
import re
# First remove any existing background-image style if it exists
content = re.sub(r'style="background-image:[^"]*"', '', content)
# Now add the background image to #hero
content = content.replace('id="hero"', 'id="hero" style="background-image: url(\'/images/hero_light_bg.png\'); background-size: cover; background-position: center; color: #1A0B13;"')

# Fix the broken thumbnail
# In Oryzo, the thumbnail was video_thumb.webp
# Let's replace whatever is in srcset and src with district_thumbnail.png
content = re.sub(r'srcset="[^"]*thumbnail[^"]*"', 'srcset="/images/district_thumbnail.png"', content)
content = re.sub(r'src="[^"]*thumbnail[^"]*"', 'src="/images/district_thumbnail.png"', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Added hero background and fixed thumbnail path")
