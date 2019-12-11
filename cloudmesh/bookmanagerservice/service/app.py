import sys
from os.path import dirname
import pickle
import subprocess
sys.path.append(dirname(__file__))

from flask import Flask, render_template, request, jsonify
from flask_misaka import Misaka
import json
import getdata
from pprint import pprint
from generateYAML import yamlGenerator


app = Flask(__name__)
Misaka(app, fenced_code=True, highlight=True)
bks = getdata.getBooks(onlybooks=True)



@app.route('/')
@app.route('/index')
def home():
    # Get all boooks avaliable
    return render_template("home2.html", data=list(bks.keys()))


@app.route("/about")
def about():
    aboutcontent = ""
    with open('README.md', 'r') as f:
        aboutcontent = f.read()
    return render_template("about.html", text=aboutcontent)


@app.route("/manual")
def manual():
    manualcontent = ""
    with open('paper/vonLaszewski-bookmanager.md', 'r', encoding="utf8") as f:
        manualcontent = f.read()
    return render_template("about.html", text=manualcontent)


@app.route("/chapterselection/<string:book>")
def chapterselection(book):
    bkinfo = getdata.getBooks(onlybooks = False, filename = bks[book])
    toc = bkinfo[book]
    #print("\nThe Metadata is\n")
    #pprint(toc['metadata'])
    return render_template("chapterselection2.html", files=[toc,str(book)])


@app.route("/genyaml")
def genyaml():
    return "Generate YAML File & PUSH TO Book Service"


@app.route('/receivedata', methods=['GET', 'POST'])
def receive_data():
    data = request.form.getlist("x[]")
    bktit = request.form.getlist("y")
    for i in range(0,len(data)):
        data[i] = json.loads(data[i])
        #print(data[i], file=sys.stderr)
    #print(data)
    #print(bktit)
    flnm = yamlGenerator(bktit[0], data)
    subprocess.run('bookmanager /opt/project/bookmanager-service/books/booksgenerated/nai_test.yaml get', shell = True)
    #link = r"/opt/project/bookmangager-service/dest/" +  flnm +
    return render_template("linktobook.html", data=link)


if __name__ == '__main__':
    app.run(debug=True)
