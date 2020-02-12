from ruamel.yaml import YAML
import requests as rq
import glob
from pathlib import Path
from pprint import pprint


def rec(dat, k=None, idx=None):
    if isinstance(dat, str):
        if str(k) == 'None':
            if idx > 0:
                for x in range(2, 4):
                    temp = dat2[idx - x]
                    if isinstance(temp, dict):
                        k = list(temp.keys())[0]
                        break
                    else:
                        pass
        for git, lk in fullLink.items():
            rep = '{github.' + str(git) + '}'
            dat = dat.replace(rep, lk)
        link = rq.get(dat)
        link.encoding = 'utf-8-sig'
        try:
            link = [line for line in link.text.replace("#", '').split('\n') if
                    line.strip() != ''][0]
        except IndexError:
            link = "Empty"

        if link != "404: Not Found":
            # print({'id': k + link.replace(" ", "_"), 'parent': k, 'text': link})
            lenk = k.split("/")
            if len(lenk) > 0:
                for x in range(len(lenk)):
                    l = len(lenk)
                    id = "/".join(lenk[0:l - x])
                    parent = "/".join(lenk[0:l - x - 1])
                    text = lenk[l - x - 1]
                    if parent == '':
                        parent = "#"
                    tre = {'id': id, 'parent': parent, 'text': text}
                    if tre not in final:
                        final.append(tre)
                        links.append('')
            else:
                if {'id': k, 'parent': '#', 'text': k} not in final:
                    final.append({'id': k, 'parent': '#', 'text': k})
                    links.append('')
            final.append(
                {'id': k + link.replace(" ", "_"), 'parent': k, 'text': link})
            links.append(dat)
        else:
            errors.append(
                {'id': k + link.replace(" ", "_"), 'parent': k, 'text': link,
                 "link": dat})
    elif isinstance(dat, dict):
        for j, value in dat.items():
            if str(k) == 'None':
                rec(value, j)
            else:
                rec(value, str(k) + '/' + j)
    elif isinstance(dat, list):
        ct = 0
        for i in dat:
            ct += 1
            rec(i, k, ct)

    print ("REC",final)
    return final


def get_books(onlybooks=False, filename=""):
    bks = {}
    if onlybooks:
        files = glob.glob("books/*.yaml")
        for f in files:
            tst = YAML(typ='safe')
            dat = tst.load(Path(f))
            title = dat['metadata']['title']
            title = " ".join(title.split("\n"))
            bks[title] = f
        return bks

    else:
        f = filename
        global final
        final = []
        seeds = []
        global links
        links = []
        global errors
        errors = []
        tst = YAML(typ='safe')
        dat = tst.load(Path(f))
        global dat2
        dat2 = dat['BOOK']
        title = dat['metadata']['title']
        title = " ".join(title.split("\n"))
        global fullLink
        pprint(dat)
        fullLink = dat['github']
        pprint(dat2)
        rec(dat2)
        pprint(dat2)

        bks[title] = {'file': f,
                      'data': final,
                      'links': links,
                      'metadata': dat['metadata']}
        # print("The Broken Links Are")
        # pprint(errors)
        return bks
