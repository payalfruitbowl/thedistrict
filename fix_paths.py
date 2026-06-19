import re
html = open('index.html', 'r', encoding='utf-8').read()
html = re.sub(r'href="/_astro/index\.[a-zA-Z0-9]+\.css"', 'href="/index.css"', html)
html = re.sub(r'src="/_astro/hoisted\.[a-zA-Z0-9]+\.js"', 'src="/hoisted.js"', html)
open('index.html', 'w', encoding='utf-8').write(html)
print('Fixed HTML paths')
