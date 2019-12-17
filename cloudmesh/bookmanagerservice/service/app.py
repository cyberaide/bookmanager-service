import sys
from os.path import dirname
import os
import subprocess

from flask import Flask, render_template, request, jsonify, send_from_directory
from flask_misaka import Misaka
import json
import getdata
from generateYAML import yamlGenerator

sys.path.append(dirname(__file__))

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = '/opt/project/bookmanager-service/dest/'
app.config[
    'BOOKS_FOLDER'] = '/opt/project/bookmanager-service/books/booksgenerated/'
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
    bkinfo = getdata.getBooks(onlybooks=False, filename=bks[book])
    toc = bkinfo[book]
    return render_template("chapterselection2.html", files=[toc, str(book)])


@app.route("/genyaml")
def genyaml():
    return "Generate YAML File & PUSH TO Book Service"


@app.route("/download/<string:flname>")
def download(flname):
    return send_from_directory(directory=app.config['UPLOAD_FOLDER'],
                               filename=flname, as_attachment=True,
                               attachment_filename="book.epub")


@app.route('/receivedata', methods=['GET', 'POST'])
def receive_data():
    data = request.form.getlist("x[]")
    bktit = request.form.getlist("y")
    for i in range(0, len(data)):
        data[i] = json.loads(data[i])
    flnm, hex = yamlGenerator(bktit[0], data)

    # check if hex is in generated books in dest
    gg = app.config['UPLOAD_FOLDER'] + hex + '.epub'
    if os.path.exists(gg):
        print("Found")
    else:
        print('File does not exist')
        subprocess.run(
            "bookmanager " + app.config['BOOKS_FOLDER'] + hex + '.yaml get',
            shell=True)
        st = "dest/" + flnm
        ed = "dest/" + hex + ".epub"
        os.rename(st, ed)

    return render_template('linktobook.html', data=hex + ".epub")


if __name__ == '__main__':
    app.run(debug=True)
