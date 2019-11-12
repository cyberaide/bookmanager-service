import yaml
from yaml import Loader
import json
from pathlib import Path
import requests
import ruamel.yaml
from ruamel.yaml import YAML
import re
from pprint import pprint
import os

class Converter(object):

    def __init__(self):

        self.toc = None
        self.book_title_string = None
        self.source = None
        self.book = {}
        #self.destination = None

    def convert(self, source):
        """
        converts a single file
        """

        source = source
        #self.destination = destionation
        with open(f, 'r') as stream:

            try:
                data = yaml.load(stream, yaml.FullLoader)
                metadata = data['metadata']
                github = data['github']
                gitHeaders = github.keys()

                self.book_title_string = metadata['title'].replace('\n', "")
                self.toc = data['BOOK']

                self.toc = str(self.toc)

                for item in gitHeaders:
                    phrase = "{github." + item + "}"
                    self.toc = self.toc.replace(phrase, github[item])
                self.toc = eval(self.toc)
                data1 = []
                links = self.unpack(self.toc)
                for link in links:
                    r = requests.get(link)
                    previous = None
                    for line in r.text.splitlines():
                        if len(line) == 0:
                            break;
                        if line[0] == '#':
                            title = line.split(" ", 1)
                            newTitle = title[1].split(" ")
                            newTempTitle = ""
                            for item in newTitle:
                                if item.isalpha():
                                    newTempTitle += item + " "
                            data1.append({link: newTempTitle})

                        elif line[0] in ["=", '-', "^", "~"]:
                            line = previous
                            title = line.split(" ", 1)
                            if len(title) < 2:
                                data1.append({link: newTempTitle})
                                break;
                            else:
                                newTitle = title[1].split(" ")
                                newTempTitle = ""
                                for item in newTitle:
                                    if item.isalpha():
                                        newTempTitle += item + " "
                                data1.append({link: newTempTitle})
                                break;
                        previous = line
                self.toc = str(self.toc)
                for item in data1:
                    for key in item.keys():
                        if key in self.toc:
                            c = str(item)
                            self.toc = self.toc.replace(key, c)

                self.toc = self.toc.replace(", '{", ",{")
                self.toc = self.toc.replace("}',", "},")
                self.toc = self.toc.replace("}']}", "}]}")
                self.toc = self.toc.replace(": ['{", ": [{")


                self.toc = eval(self.toc)
                self.book[self.book_title_string] = self.toc
            except yaml.YAMLError:
                print(yaml.YAMLError)

    def unpack(self, content):
        nList = []
        for item in content:
            if isinstance(item, dict):
                nList += (self.unpack(list(item.values())[0]))
            else:
                nList.append(item)
        return nList

    def getBook(self):
        return self.book

    def fetch(self, url):

        request = requests.get(url)
        content = request.text.split('\n')

        return content[0]

## change path if needed
os.chdir('..')
os.chdir('..')
os.chdir('books')
path = Path('.')
## list of yaml files
LoF = list(path.glob('*.yaml'))

for f in LoF:
   source = f
   #destination = f.replace('.yaml', '.json')
   i = Converter()
   Converter.convert(i, source)
   print(i.getBook())

