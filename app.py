from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/episode/heji/latest')
def episode():
    return render_template('episode.html')

@app.route('/photo')
def photo():
    return render_template('photo.html')

@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == "__main__":
    app.run(debug=True)