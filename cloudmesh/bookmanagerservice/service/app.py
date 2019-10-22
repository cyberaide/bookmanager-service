from flask import Flask
from flask import Flask, render_template
from utils.getData import getBooks, getChapters

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    #Get all boooks avaliable
    return render_template("home.html", data = getBooks())

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chapterSelection/<string:book>")
def chapterSelection(book):
    #Get Chapter Information for selected book
    return render_template("ChapterSelection.html", data = getChapters(book))

@app.route("/GenYaml")
def GenYaml():
    return "Generate YAML File & PUSH TO Book Service"



if __name__ == '__main__':
    app.run()
