import sys
from os.path import dirname
import os
import pickle
import subprocess
sys.path.append(dirname(__file__))

from flask import Flask, render_template, request, jsonify, send_from_directory, send_file, Response
from flask_misaka import Misaka
import json
import getdata
from pprint import pprint
from generateYAML import yamlGenerator


app = Flask(__name__)
app.config['DEST'] = "/opt/project/bookmanager-service/dest/"
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
    flnm = yamlGenerator(bktit[0], data)

    subprocess.run('bookmanager /opt/project/bookmanager-service/books/booksgenerated/nai_test.yaml get', shell = True)
    subprocess.run('bookmanager /opt/project/bookmanager-service/books/booksgenerated/nai_test.yaml pdf', shell=True)
    #link = r'/opt/project/bookmanager-service/dest/' +  flnm
    #file = open(link, 'rb')
    #returnfile = file.read()
    #file.close()
    #return Response(returnfile,
    #                mimetype="application/xhtml+xml",
    #                headers={"Content-disposition":
    #                             "attachment; filename=tst.epub"})

    #application/epub+zip
    #print(link)
    #return send_file(app.config['DEST'] +  'book.html', attachment_filename = flnm, as_attachment=True)#mimetype ="application/epub" )
    return send_from_directory(directory = app.config['DEST'], filename = "book.html", as_attachment=True)#, mimetype ="application/epub+zip")
    #return render_template(app.config['DEST'] +  'book.html')


if __name__ == '__main__':
    app.run(debug=True)
