from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from collections import namedtuple
from datetime import date
app = Flask(__name__, static_folder='./static')

Episode = namedtuple('Episode', ['number', 'title'])
# Photo = namedtuple('Photo', ['id', 'date', 'filename'])
# photo_list_model=[Photo(id=0, date=date(2019,7,30), filename='20190730-chikazu.png'),
#                     Photo(id=1, date=date(2019,7,30), filename='20190730-hejichika.png'),]

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///photos.db'
db = SQLAlchemy(app)

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

@app.route('/episode/heji/')
def episode():
    episode_list=sorted([Episode(number=1,title="OPEN da DOOR(1)"),
                         Episode(number=2,title="OPEN da DOOR(2)"),
                         Episode(number=3,title="Big Dog's Digging LIFE")],reverse=True)

    return render_template('episode.html',episode_list=episode_list)

@app.route('/photos')
def photos():
# TODO データベース内のすべてのサムネイルを検索する
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

# TODO POSTメソッドでphotoのidを受け渡す
# TODO データベースとの連携
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