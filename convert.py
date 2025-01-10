import json
from pathlib import Path

with open('./src/scripts/intro.json', encoding='utf-8') as f:
    obj = json.load(f)

page_index = 1
for page_group in obj['page_groups']:
    title = page_group.get('title',None)
    for page in page_group['pages']:
        page_obj = {
            'title': title,
            'blocks': {
                'type': 'VerticalLayout',
                'elements':page['elements']
            }
        }
        with open(f"./src/scripts/pages/intro/{page_index}.json","w+",encoding='utf-8') as f:
            json.dump(page_obj,f, indent=4, ensure_ascii=False)
        page_index+=1