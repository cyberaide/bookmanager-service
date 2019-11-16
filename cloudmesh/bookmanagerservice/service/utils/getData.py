from cloudmesh.bookmanagerservice.converter import Converter
from pathlib import Path
import os

def getBooks():
    path = Path(os.getcwd() + '/books')
    LoF = list(path.glob('*.yaml'))

    lst = []
    for f in LoF:
        lst.append(Converter.gettitle(Converter(), f))


    random_list = ['Book1', 'Book2', 'Book3', 'Book4', 'Book5', 'Book6', 'Book7', 'Book8']

    return lst

def getChapters(bk):
    chapters = {'Chapter1' : ['Section 1', 'Section 2', 'Section 3 ', 'Section 4','Section 5']
              , 'Chapter2' : ['Section 1', 'Section 2', 'Section 3 ']
              ,'Chapter3' : ['Section 1', 'Section 2']
              ,'Chapter4' : ['Section 1', 'Section 2', 'Section 3 ', 'Section 4','Section 5','Section 6','Section 7']
                }
    return chapters