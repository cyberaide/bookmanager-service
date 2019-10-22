import yaml
from yaml import Loader
import json
from pathlib import Path

## change path if needed
path = Path('.')
## list of yaml files
LoF = list(path.glob('*.yaml'))

## data structure for book of table content
## key(string) -> title
## value(dictionary) -> book table of content
books = {}

## opening all yaml files in the directory
## adding elements to 'books' by making title from metadata
## as keys and table of content from 'BOOK' as values
for f in LoF:
   with open(f, 'r') as stream:
    try:
        data = yaml.load(stream, Loader=Loader)
        temp = data['metadata']
        title = temp['title']
        title = title.replace('\n', "")
        books[title] = data['BOOK']          
    except yaml.YAMLError:
        print(yaml.YAMLError)

## writing dictionary to json files.
for book in books.keys():
    name = book + ".json"
    with open("outputFiles/" + name, 'w+') as output:
        temp = books[book]
        json.dump(temp, output)
