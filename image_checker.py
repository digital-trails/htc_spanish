from pathlib import Path
import json

def process_file(obj):
    if isinstance(obj,dict):
        for k,v in obj.items():
            if k.lower() in ['url','file'] and not Path(f'./src/{v}').exists():
                yield v
            else:
                yield from process_file(v)
    if isinstance(obj,list):
        for o in obj:
            yield from process_file(o)

def process_dir(dir):
    for p in Path(dir).iterdir():

        if(p.is_dir()):
            process_dir(p)
            continue

        with open(p, encoding='utf-8') as f:
            
            bad_links = list(process_file(json.load(f)))

            if bad_links:
                print(p)
                for l in bad_links:
                    print(f'  {l}')

process_dir('./src/flows')