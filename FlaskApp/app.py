from flask import Flask
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def home():
    #Get all boooks avaliable
    random_list = ['Book1', 'Book2', 'Book3', 'Book4','Book5','Book6','Book7','Book8']
    return render_template("home.html", data = random_list)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/chapterSelection/<string:book>")
def chapterSelection(book):
    #Get Chapter Information for selected book
    chapters = {'Chapter1' : ['Section 1', 'Section 2', 'Section 3 ', 'Section 4','Section 5']
              , 'Chapter2' : ['Section 1', 'Section 2', 'Section 3 ']
              ,'Chapter3' : ['Section 1', 'Section 2']
              ,'Chapter4' : ['Section 1', 'Section 2', 'Section 3 ', 'Section 4','Section 5','Section 6']
                }
    return render_template("ChapterSelection.html", data = chapters)

@app.route("/GenYaml")
def GenYaml():
    return "Generate YAML File & PUSH TO Book Service"



if __name__ == '__main__':
    app.run()
