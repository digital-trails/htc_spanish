import json
from pathlib import Path

files = ['eod', 'instructions', 'disclaimer', 'what_is_anxiety']

files = files[1:]

for file in files:

    with open(f'./src/scripts/{file}.json', encoding='utf-8') as f:
        obj = json.load(f)

    page_index = 1

    if 'pages' in obj:
        obj = {'page_groups': [obj]}

    for page_group in obj['page_groups']:
        props = page_group.copy()
        props.pop('pages')
        for page in page_group['pages']:
            props.update(page)
            props.pop('elements')
            page_obj = {
                **props,
                'blocks': {
                    'type': 'VerticalLayout',
                    'elements':page['elements']
                }
            }

            directory = Path(f"./src/scripts/pages/{file}")
            directory.mkdir(parents=True, exist_ok=True)
            with open(directory / f"{page_index}.json", "w+", encoding='utf-8') as f:
                json.dump(page_obj, f, indent=4, ensure_ascii=False)
            page_index+=1