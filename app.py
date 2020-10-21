from flask import Flask,  render_template, request
from data import *

app = Flask(__name__)


@app.route('/')
@app.route('/tours/')
def index():
    description = f"Всего доступно {len(tours)} туров. Воспользуйтесь сортировкой."
    return render_template('index.html',
                           title = title,
                           subtitle=subtitle,
                           description=description,
                           departures=departures,
                           tours=tours,
                           )


@app.route('/departures/<departure>/')
@app.route('/tours/departures/<departure>/')
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

@app.route('/tours/tours/<id>/')
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
