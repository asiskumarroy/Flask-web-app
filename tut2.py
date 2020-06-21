from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/about')
def about():
    var='asis'
    return render_template("about.html", name=var)

@app.route('/boot')
def bootstrp():
    return render_template("boot.html")

app.run(debug=True)
