from flask import Flask, render_template, request
from flask_misaka import Misaka

from cloudmesh.bookmanagerservice.service.utils.getData import getBooks, getChapters

app = Flask(__name__)
Misaka(app, fenced_code=True, highlight=True)


@app.route('/')
@app.route('/index')
def home():
    #Get all boooks avaliable
    return render_template("home.html", data = getBooks())

@app.route("/about")
def about():
    aboutcontent = ""
    with open('README.md', 'r') as f:
        aboutcontent = f.read()
    return render_template("about.html", text=aboutcontent)


@app.route("/manual")
def manual():
    manualcontent = ""
    with open('paper\\vonLaszewski-bookmanager.md', 'r', encoding="utf8") as f:
        manualcontent = f.read()
    return render_template("about.html", text=manualcontent)


@app.route("/chapterselection/<string:book>")
def chapterselection(book):
    #Get Chapter Information for selected book
    return render_template("chapterselection.html", data=getChapters(book))


@app.route("/genyaml")
def genyaml():

    return "Generate YAML File & PUSH TO Book Service"

@app.route('/receivedata', methods=['GET','POST'])
def receive_data():
    data = request.form.getlist("x[]")
    print(data)
    link = "https://www.yahoo.com"
    return render_template("linktobook.html", data  = link)

if __name__ == '__main__':
    app.run(debug = True)
