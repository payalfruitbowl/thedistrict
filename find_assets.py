import re
import sys

def search_assets(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            content = f.read()
            
        urls = re.findall(r'\"[^\"]+\.(?:glb|splat|webp|png|mp4|webm|wasm)\"', content)
        print("Found urls:")
        for url in urls[:50]:
            print(url)
    except Exception as e:
        print(e)

search_assets('hoisted.js')
