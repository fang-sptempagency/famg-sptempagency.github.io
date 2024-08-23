from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.schema import ForeignKey
from collections import namedtuple
from datetime import date
app = Flask(__name__, static_folder='./static')

# Episode = namedtuple('Episode', ['number', 'title'])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)

class Episode(db.Model):
    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    series = db.Column(db.String(30), nullable=False)
    title = db.Column(db.String(30), nullable=False)
    order = db.Column(db.Integer, nullable=False)
    filename = db.Column(db.String(30), nullable=False) #thumbnail

#class Page(db.model):
#    id = db.Column(db.Integer,  autoincrement=True, primary_key=True)
#    episode_id = db.Column(db.Integer)
#    order = db.Column(db.Integer, nullable=False)
#    posision = db.Column(db.String(1), nullable=False,  server_default="r")  #c(center),l(left),r(right)
#    episode_id = db.Column(db.Integer, ForeignKey("Episode.id", nullable=False)

class Photo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    filename = db.Column(db.String(30), nullable=False)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/episode/<series>/')
def episode_list(series):
    episodes = Episode.query.order_by(Episode.order).filter(Episode.series==series).all() #戸次のエピソードだけ取得する
    episode_list = []
    for episode in episodes:
        episode_list.append({
            'id': episode.id,
            'order': episode.order,
            'title': episode.title,
            'thumbnail':  f"../../static/episode/{series}/thumbnail/{episode.filename}.png",
            'link': f"episode/{series}/{episode.order}",
        })
    return render_template('episode.html',episode_list=episode_list)

@app.route('/episode/<series>/<order>')
def episode(series, order):
    print(f'episode/{series}/{order}.html')
    return render_template(f'episode/{series}/{order}')

@app.route('/photos')
def photos():
# TODO 時間順でサムネイルを並べる
    photos = Photo.query.order_by(Photo.date).all()
    photo_list = []
    for photo in photos:
        photo_list.append({
            'id': photo.id,
            'date': photo.date,
            'thumbnail':  f"static/photos/thumbnail/{photo.filename}"
        })
    return render_template('photos.html', photo_list=photo_list)


@app.route('/photos/<int:id>')
def photo(id):
    photo = Photo.query.get(id)
    photo_info = {
        'id': photo.id,
        'date': photo.date,
        'path':  f"static/photos/{photo.filename}"
    }
    return render_template('photo.html', photo=photo_info)

@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == "__main__":
    app.run(debug=True)