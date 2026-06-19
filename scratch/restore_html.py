import os

file_path = "index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1st Scroll (Hero)
# Restore the exact layout from Oryzo screenshot: "ORYZO" in the corner, wait...
# In Oryzo, the hero title was "ORYZO", but user said "chnage the name to the district".
content = content.replace('<div id="hero-logo-ref" style="font-size: 15vw; font-weight: 800; line-height: 1; margin: 0; color: #DA1C5C; font-family: sans-serif; letter-spacing: -0.05em; display: flex; align-items: center;">DISTRICT</div>', '<div id="hero-logo-ref">THE DISTRICT</div>')
content = content.replace('id="hero-logo-ref" style="font-size: 15vw; font-weight: 800; line-height: 1; margin: 0; color: #F9C12F; font-family: sans-serif; letter-spacing: -0.05em; display: flex; align-items: center;"', 'id="hero-logo-ref"')

# 2nd Scroll (AI-Pre)
# Original Oryzo: "Oryzo isn't just a coaster."
content = content.replace('<h2>isn’t just <br>a coaster.</h2>', '<h2>isn’t just <br>a color palette.</h2>')

# 3rd Scroll (AI-Header)
# Original Oryzo: "Powered by AI*", "ORYZO-1", "AI FILLS IN THE GAPS. WE SAID HIGH FIVE. IT HEARD SIX."
content = content.replace('Powered by Creativity<sup>*</sup>', 'Powered by AI<sup>*</sup>')
content = content.replace('district-1', 'DISTRICT-1')
content = content.replace('<span>We fill in the gaps.</span><span> You bring the brief.</span><span> We bring the heat.</span>', '<span>AI FILLS IN THE GAPS.</span><span> WE SAID HIGH FIVE.</span><span> IT HEARD SIX.</span>')

# Remove the hero image override so the canvas is fully visible!
if 'style="background-image: url(' in content:
    import re
    content = re.sub(r'style="background-image: url\([^)]+\);?"', '', content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Restored exact HTML text matching the screenshots")
