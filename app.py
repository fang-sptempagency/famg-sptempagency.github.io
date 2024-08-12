from flask import Flask, render_template, request
from collections import namedtuple
from datetime import date
app = Flask(__name__, static_folder='./static')

Episode = namedtuple('Episode', ['number', 'title'])
Photo = namedtuple('Photo', ['id', 'date', 'filename'])
photo_list_model=[Photo(id=0, date=date(2019,7,30), filename='20190730-chikazu.png'),
                    Photo(id=1, date=date(2019,7,30), filename='20190730-hejichika.png'),]

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
    photo_list = []
    for photo in photo_list_model:
        print(photo)
        photo_list.append({'id': photo.id,
                           'date': photo.date,
                           'thumbnail': f"static/photos/thumbnail/{photo.filename}"})
    # [Photo(id=0, date=date(2019,7,30), path='static/photos/20190730-chikazu.png',
    #                      thumbnail='static/photos/thumbnail/20190730-chikazu.png'),
    #                 Photo(id=1, date=date(2019,7,30), path='static/photos/20190730-hejichika.png',
    #                       thumbnail='20190730-hejichika.png'),])
    return render_template('photos.html', photo_list=photo_list)

# TODO POSTメソッドでphotoのidを受け渡す
# TODO データベースとの連携
@app.route('/photos/<int:id>')
def photo(id):
    photo={'id':photo_list_model[id].id,
           'date':photo_list_model[id].date,
           'path':f"static/photos/{photo_list_model[id].filename}"}
    
    return render_template('photo.html', photo=photo)

@app.route('/report')
def report():
    return render_template('report.html')


if __name__ == "__main__":
    app.run(debug=True)