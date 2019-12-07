import pickle
import json
import oyaml as yaml
from collections import OrderedDict
from pathlib import Path
import sys
import re

p = Path('.') / 'cloudmesh' / 'bookmanagerservice' / 'service'
sys.path.append(str(p.absolute()))
from nested_lookup import get_all_keys
import getdata


def yamlGenerator(bookTitle, bookData):
    bks = getdata.getBooks(onlybooks=True)
    tstbk = bookTitle
    bkinfo = getdata.getBooks(onlybooks=False, filename=bks[tstbk])

    # All Data
    mainData = bkinfo[tstbk]['data']
    links = bkinfo[tstbk]['links']
    metadata = bkinfo[tstbk]['metadata']
    data = pickle.load(open(bookData, "rb"))

    final = {}
    for d in data:
        if d['parent'] == '#':
            final[d['id']] = d['children']

    temp = {}
    temp2 = {}

    for keys, values in final.items():
        lst = rec(data, values)
        temp[keys] = lst

    keyList = get_all_keys(temp)
    idList = unpack(temp)
    temp = str(temp)
    for item in idList:
        for i in range(len(mainData)):
            t = mainData[i]
            if item == t['id']:
                temp = temp.replace(item, links[i])

    for item in keyList:
        if '/' in item:
            tempItem = item.split("/")
            temp = temp.replace(item, tempItem[-1])

    temp = eval(temp)

    temp2['metadata'] = metadata
    temp2['BOOK'] = [temp]
    temp2 = temp2

    mystr = yaml.dump(yaml.load(json.dumps(temp2), Loader=yaml.SafeLoader), default_flow_style=False)
    mystr = re.sub(r'([\n])  ([A-Z])', r'\n- \2', mystr)

    # print(mystr)
    bookTitle = metadata['title']
    with open('books/nai_test.yaml', 'w+') as f:
        f.write(mystr)


def rec(data, vals):
    lst2 = []
    for v in vals:
        lst = []
        for d in data:
            if d['parent'] == v:
                lst.append(d['id'])
        if len(lst) > 0:
            g = rec(data, lst)
            lst2.append(({v: g}))
        else:
            lst2.append(v)
    return lst2


# convert names in temp to links
def unpack(content):
    nList = []
    for k, v in content.items():
        for value in v:
            if isinstance(value, dict):
                nList += (unpack(value))
            else:
                nList.append(value)
    return nList

