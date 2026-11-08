# For https://reviseonline.pearson.com/
import json

def extract_urls(obj, urls=None):
    if urls is None:
        urls = []
    
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == 'URL' and isinstance(v, str) and v.startswith('http'):
                urls.append(v)
            else:
                extract_urls(v, urls)
    elif isinstance(obj, list):
        for item in obj:
            extract_urls(item, urls)
            
    return urls

with open('manifest.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

all_urls = extract_urls(data)
print(f"Found {len(all_urls)} URLs!")

print('\n'.join(all_urls))

with open('extracted_urls.txt', 'w', encoding='utf-8') as f:
    f.write('\n'.join(all_urls))
