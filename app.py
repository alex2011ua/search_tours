from flask import Flask,  render_template, request
from data import *
from os import environ


app = Flask(__name__)

TEST_ENV = environ.get('test_in')
@app.route('/')

def index():
    description = f"Всего доступно {len(tours)} туров. Воспользуйтесь сортировкой."
    return render_template('index.html',
                           title = title,
                           subtitle=subtitle,
                           description=description,
                           departures=departures,
                           tours=tours,
                           test=TEST_ENV
                           )


@app.route('/departures/<departure>/')

def departuress(departure):
    tour_is = {}
    for item, tour in tours.items():
        if tour['departure'] == departure:
            tour_is[item] = tour

    description = {'count': len(tour_is),
                   'min_price': min([x["price"] for x in tour_is.values()]),
                   'max_price': max([x["price"] for x in tour_is.values()]),
                   'min_night': min([x["nights"] for x in tour_is.values()]),
                   'max_night': max([x["nights"] for x in tour_is.values()])
                   }
    return render_template('departure.html',
                           departure=departure,
                           title = title,
                           description = description,
                           departures = departures,
                           tours = tour_is,
                           )


@app.route('/tours/<id>/')
def tour(id):
    t = tours[int(id)]
    tour1 = t['departure']
    departure = departures[tour1]
    return render_template('tour.html',
                           id=id,
                           title = title,
                           departure=departure,
                           tour=tours[int(id)],
                           departures = departures,
                           )

if __name__ == '__main__':
    app.run()
