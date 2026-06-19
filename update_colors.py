import os

PROJECT = r"C:\Users\payal\.gemini\antigravity\scratch\oryzo-ai"
css_path = os.path.join(PROJECT, "index.css")

with open(css_path, "r", encoding="utf-8") as f:
    css = f.read()

color_replacements = {
    "--color-white: #ffedd7": "--color-white: #e8d5b0",
    "--color-white-transparent: #ffedd700": "--color-white-transparent: #e8d5b000",
    "--color-black: #100904": "--color-black: #121010",
    "--color-black-transparent: #10090400": "--color-black-transparent: #12101000",
    "--color-grey-brown: #6c5f51": "--color-grey-brown: #8a7a6a",
    "--color-green: #445231": "--color-green: #2a3d3d",
    "--color-green-light: #5d6c49": "--color-green-light: #3d5252",
    "--color-green-lightest: #f6e0c6": "--color-green-lightest: #f0e6d6",
    "--color-orange: #dc5000": "--color-orange: #c9943a",
    "--color-brown: #382416": "--color-brown: #3d2b1f",
}

for old, new in color_replacements.items():
    css = css.replace(old, new)

hex_replacements = {
    "#ffedd6": "#e8d5b0",
    "#ffedd7": "#e8d5b0",
    "#FFEDD6": "#e8d5b0",
    "#100904": "#121010",
    "#dc5000": "#c9943a",
    "#445231": "#2a3d3d",
    "#382416": "#3d2b1f",
    "#6c5f51": "#8a7a6a",
    "#4b5c3d": "#1a1714",
    "#201914": "#1a1510",
    "#FDE9CE": "#e8d5b0",
    "#fdfeed": "#ffefd0",
    "#ffbf02": "#d4a053",
    "#e9500e": "#c9943a",
    "#cd197d": "#8b4513",
    "#8c019c": "#5a3a2a",
    "#250187": "#2a1f15",
    "#030310": "#0a0808",
}

for old_hex, new_hex in hex_replacements.items():
    css = css.replace(old_hex, new_hex)

css = css.replace("#ff8c00", "#c9943a")
css = css.replace("#ffa000", "#d4a053")
css = css.replace("#e07010", "#b8862d")
css = css.replace("#e6500a", "#a07828")
css = css.replace("#e6640a", "#b08030")

with open(css_path, "w", encoding="utf-8") as f:
    f.write(css)

print("[OK] Colors updated")
