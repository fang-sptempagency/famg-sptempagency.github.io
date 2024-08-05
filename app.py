from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/episode/heji/latest')
def episode():
    return render_template('episode.html')

@app.route('/photos')
def photos():
    return render_template('photos.html')

@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == "__main__":
    app.run(debug=True)