import os

file_path = "index.css"

with open(file_path, "r") as f:
    content = f.read()

# Add styles for the #ai dark section and glow
glow_css = """
#ai .section__inner {
    background-color: #0D0D0D;
    color: #fff;
    transition: background-color 0.5s ease;
}

#ai .section__inner::after {
    content: '';
    position: absolute;
    inset: 0;
    pointer-events: none;
    z-index: 100;
    box-shadow: inset 0 0 100px 30px rgba(255, 93, 212, 0.4), inset 0 0 200px 80px rgba(241, 90, 41, 0.3), inset 0 0 300px 120px rgba(249, 193, 47, 0.1);
    border: 5px solid rgba(255, 93, 212, 0.3);
    border-radius: 30px;
    opacity: 1;
}

#ai h1, #ai h2, #ai h3, #ai h4, #ai .body1, #ai .sub1, #ai .sub2 {
    color: #fff;
}
#ai #ai-tagline {
    color: #F15A29; /* Tangerine for the ORYZO-1 replacement */
}
"""

if "box-shadow: inset 0 0 100px 30px" not in content:
    content += glow_css

with open(file_path, "w") as f:
    f.write(content)

print("Updated index.css")
