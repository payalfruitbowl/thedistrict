"""
Rebrand to The District Design Project - Neon/Sunset Theme
"""
import os
import re

PROJECT = r"C:\Users\payal\.gemini\antigravity\scratch\the-district-design"

# ═══════════════════════════════════════════
# 1. CSS TRANSFORMATIONS
# ═══════════════════════════════════════════

css_path = os.path.join(PROJECT, "index.css")
with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

# Font: DM Sans everywhere for a modern agency vibe
css = css.replace(
    '@import"https://use.typekit.net/pmn6ngx.css"',
    '@import url("https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;700;900&display=swap")'
)
css = css.replace('--display-font: "halyard-display-variable"', '--display-font: "DM Sans", system-ui, sans-serif')
css = css.replace('--text-font: "halyard-text-variable"', '--text-font: "DM Sans", system-ui, sans-serif')
css = css.replace("font-family:Literata", "font-family:'DM Sans', sans-serif")

# NEON PALETTE REPLACEMENTS
# We'll use a very dark background to let the neon colors pop
# Black/Dark background remains #100904 or we can make it a darker charcoal
color_replacements = {
    "--color-black: #100904": "--color-black: #0D0D0D", # Darker background
    "--color-black-transparent: #10090400": "--color-black-transparent: #0D0D0D00",
    "--color-white: #ffedd7": "--color-white: #F9C12F", # SUN (Yellow/Gold) text/cream
    "--color-white-transparent: #ffedd700": "--color-white-transparent: #F9C12F00",
    "--color-orange: #dc5000": "--color-orange: #DA1C5C", # DRAGONFRUIT (Magenta)
    "--color-green: #445231": "--color-green: #FF5DD4", # SOUR RASPBERRY (Hot Pink)
    "--color-green-light: #5d6c49": "--color-green-light: #FF9846", # SUNSET (Light Orange)
    "--color-green-lightest: #f6e0c6": "--color-green-lightest: #F15A29", # TANGERINE
    "--color-brown: #382416": "--color-brown: #DA1C5C", # DRAGONFRUIT
    "--color-grey-brown: #6c5f51": "--color-grey-brown: #FF9846",
}

for old, new in color_replacements.items():
    css = css.replace(old, new)

# Inline hex replacements in CSS
css = css.replace("#ffedd6", "#F9C12F")
css = css.replace("#ffedd7", "#F9C12F")
css = css.replace("#100904", "#0D0D0D")
css = css.replace("#dc5000", "#DA1C5C")
css = css.replace("#445231", "#FF5DD4")
css = css.replace("#382416", "#DA1C5C")
css = css.replace("#6c5f51", "#FF9846")
css = css.replace("#4b5c3d", "#0D0D0D") # Preloader bg

# Glows: Orange glows -> Magenta/Pink glows
css = css.replace("rgba(220, 80, 0,", "rgba(218, 28, 92,")
css = css.replace("rgba(220,80,0,", "rgba(218,28,92,")
css = css.replace("#ff8c00", "#FF5DD4")
css = css.replace("#ffa000", "#DA1C5C")
css = css.replace("#e07010", "#F15A29")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("[OK] CSS transformed successfully")


# ═══════════════════════════════════════════
# 2. HTML TRANSFORMATIONS
# ═══════════════════════════════════════════

html_path = os.path.join(PROJECT, "index.html")
with open(html_path, "r", encoding="utf-8") as f:
    html = f.read()

# Only safely replace text that is shown to the user.
# Do NOT globally replace "ORYZO" as it breaks the SVG path rendering and JS.
# Instead, target specific text blocks.

def replace_text(old, new):
    global html
    html = html.replace(old, new)

# Meta
replace_text("<title>ORYZO AI</title>", "<title>THE DISTRICT DESIGN PROJECT</title>")
replace_text('content="ORYZO AI"', 'content="THE DISTRICT DESIGN PROJECT"')

# Hero
replace_text("Made for mugs. Built for tables.", "Made for impact. Built for brands.")
replace_text(
    "Designed to lift, insulate, and grip in all the right ways. Oryzo makes the simplest moment feel considered.",
    "The District Design Project is a creative agency crafting vibrant visual identities, high-octane motion graphics, and bold digital experiences."
)

# Avoid replacing the actual SVG inner text or path classes!
# But we can replace the text after the hero logo
replace_text(
    "Designed<br> by Lusion,<br> the award-winning<br> design studio.",
    "Crafted<br> by The District,<br> the boldest<br> design agency."
)
replace_text(
    ">The world's most</span><span> unnecessarily</span><span> sophisticated cork coaster.</span>",
    ">The world's most</span><span> unapologetically</span><span> vibrant design agency.</span>"
)

# AI Section -> Design Services
replace_text("isn't just <br>a coaster.", "isn't just <br>an agency.")
replace_text(
    ">Oryzo isn't just a </span><span>coaster. It's the result </span><span>of unprecedented AI* </span><span>breakthroughs.</span>",
    ">The District isn't just an </span><span>agency. It's the result </span><span>of unparalleled creative </span><span>ambition.</span>"
)
replace_text("Powered by AI<sup>*</sup>", "Powered by Creativity<sup>*</sup>")
replace_text("Try to hover hand", "Explore our portfolio")
replace_text(
    ">AI fills in the gaps.</span><span> We said high five.</span><span> It heard six.</span>",
    ">We fill in the gaps.</span><span> You bring the brief.</span><span> We bring the heat.</span>"
)

# Wearable -> Portfolio
replace_text(">So portable,</span>", ">So vibrant,</span>")
replace_text(">it's wearable</span>", ">it's unforgettable</span>")
replace_text("AI SLOP IDEAS<br>FOR THIS<br>WINTER", "NEON BRAND<br>STRATEGIES<br>FOR WINTER")

replace_text(
    ">Oryzo is taking everyone's jobs...</span><span>and replacing them with AI!</span>",
    ">The District is taking over...</span><span>and replacing boring with bold!</span>"
)

# Features -> Agency Pillars
replace_text("Rise above mediocrity", "Rise above the noise")
replace_text(
    "With a precision-engineered lift (exactly one coaster thick), Oryzo doesn't just hold your mug - it elevates it. Literally. Above every boring surface you've ever known.",
    "With precision-engineered creative, The District doesn't just design your brand - it elevates it. Literally. Above every boring competitor you've ever known."
)
replace_text("Elevate your coffee experience", "Elevate your visual identity")

replace_text("Handles Extremes with Ease", "Handles Any Brief with Ease")
replace_text(
    "From piping-hot mugs to ice-cold drinks - Oryzo stays perfectly stable. Your coffee table already tapped out three sips ago.",
    "From massive rebrands to rapid social campaigns - The District stays perfectly creative. Your competition tapped out three weeks ago."
)
replace_text("Thermodynamic stability", "Creative stability")

replace_text("Perfectly Round, Seriously", "Perfectly Executed, Always")
replace_text(
    "Our engineers recalibrated its circumference with disturbing levels of attention to detail - just because we could.",
    "Our designers recalibrated every pixel with disturbing levels of attention to detail - just because we can."
)

# Encryption -> Join Us
replace_text("Secure communications simplified", "Creative communications amplified")
replace_text("Smart flip <br>encryption", "Smart brand <br>transformation")
replace_text(
    "Write a message. Flip. Instantly secure - until <br>someone flips it back. Genius.",
    "Share a vision. We design it. Instantly vibrant - your <br>audience won't look away. Genius."
)
# Leave value="ORYZO" alone to prevent breaking JS!
replace_text(">Encode Message</span>", ">Transform Brand</span>")
replace_text(">Decode Message</span>", ">Reveal Design</span>")

# Grip -> Impact
replace_text("Precision Grip, Zero Drama", "Precision Design, Zero Drama")
replace_text(
    "Grip-locked Antislip<br>technology",
    "High-Impact Visual<br>technology"
)
replace_text(
    "Micro-textured cork so grippy your drink files <br>a restraining order against gravity. Spills? <br>Consider them politely discouraged.",
    "High-contrast colors so vibrant your eyes file <br>a restraining order against boring. Blending in? <br>Consider it politely discouraged."
)
replace_text("Friction coefficient (est):", "Vibrancy coefficient (est):")

# Sustainability -> Process
replace_text("100% Plant-based", "100% Bold-based")
replace_text("Vegan-friendly", "Future-ready")
replace_text(
    "Pure cork sourced sustainably. <br>Completely vegan - no cows were harmed, <br>but it might be full of \"bull\"sh*t.",
    "Pure design sourced creatively. <br>Completely bold - no rules were followed, <br>but it might be full of \"neon\" vibes."
)

replace_text(
    "Cork oaks are typically first harvested at around 25 years, once the bark is thick enough to remove safely.",
    "Our designers typically deliver initial concepts in around 25 hours, once the brief is fully digested."
)

replace_text(
    "After each harvest, the bark takes about 9 years to regrow, making cork a renewable material.",
    "After each campaign, the brand takes about 9 weeks to fully dominate, making design a powerful tool."
)

replace_text(
    'No compute. No tokens. So you can say "please" and "thank you" as much as you want, guilt free.',
    "No templates. No boring colors. So you can be as bold and loud as you want, guilt free."
)

# Testimonials
replace_text("People all around the world love Oryzo", "Brands all around the world love The District")
replace_text("Do not take our word for it, see what people say after living with Oryzo.", "Don't take our word for it, see what clients say after working with The District.")

# Only update visible SVGs if needed, but we'll use a regex for hex codes
html = html.replace('#ffedd6', '#F9C12F')
html = html.replace('#FFEDD6', '#F9C12F')
html = html.replace('#ffedd7', '#F9C12F')
html = html.replace('#FFEDD7', '#F9C12F')
html = html.replace('#FDE9CE', '#F9C12F')
html = html.replace('#dc5000', '#DA1C5C')
html = html.replace('#DC5000', '#DA1C5C')
html = html.replace('#445231', '#FF5DD4')
html = html.replace('#5d6c49', '#FF9846')
html = html.replace('#382416', '#DA1C5C')
html = html.replace('#100904', '#0D0D0D')

# Change ONLY specific text nodes that say ORYZO to THE DISTRICT without breaking HTML tags
# We use regex to replace ORYZO when it's surrounded by > and <
html = re.sub(r'>ORYZO<', '>THE DISTRICT<', html)
html = re.sub(r'>ORYZO-1</h4>', '>DISTRICT-1</h4>', html)
html = re.sub(r'>ORYZO-1</div>', '>DISTRICT-1</div>', html)
html = re.sub(r'>ORYZO Pro</span>', '>District Pro</span>', html)
html = re.sub(r'>ORYZO Pro Max</span>', '>District Pro Max</span>', html)
html = re.sub(r'>ORYZO Pro</h4>', '>District Pro</h4>', html)
html = re.sub(r'>ORYZO Pro Max</h4>', '>District Pro Max</h4>', html)
html = re.sub(r'>ORYZO Pro</button>', '>District Pro</button>', html)
html = re.sub(r'>ORYZO Pro Max</button>', '>District Pro Max</button>', html)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("[OK] HTML transformed successfully")
