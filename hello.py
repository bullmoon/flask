from flask import Flask, render_template
app = Flask(__name__)

menu = ["Install", "First app", "Feedback"]
@app.route("/")
def index():
    return render_template('index.html', title='About Flask', menu=menu)

@app.route("/about")
def about():
    return render_template('about.html', title='About site')

if __name__ == "__main__":
    app.run(debug=True)