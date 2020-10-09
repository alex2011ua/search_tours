
from flask import Flask,  render_template, request
from data import *

app = Flask(__name__)



form = '''
    <form class="auth-form" action="/signin" method="POST">
    <div> Имя <input type="text" name="u_name" />  </div>
    <div> Фамилия <input type="text" name="u_surname" /> </div>
    <div> Почта <input type="email" name="u_mail" /> </div>
    <div> Пароль <input type="password" name="u_pass" /> </div>
    <div> Еще раз <input type="password" name="u_pass_again" /> </div>
    <div> <input type="submit" value="Зарегистрироваться" />  </div>
    </form>
'''
@app.route('/signin', methods = ["POST", 'GET'])
def registration():
    name = request.form.get('u_name')
    sur = request.form.get('u_surname')
    mail = request.form.get('u_mail')
    pas_1 = request.form.get('u_pass')
    pas_2 = request.form.get('u_pass_again')
    if pas_1 == pas_2 and mail != None :
        return f"Пользователь {name} {sur} с почтой {mail} зарегистрирован"
    else:
        return form

@app.route('/')
def index():

    return render_template('index.html',
                           title = title,
                           subtitle=subtitle,
                           description=description,
                           departures=departures,
                           tours=tours,

                           )


@app.route('/departures/<departure>/')
def departure(departure):


    return render_template('departure.html', departure=departure,
                           title = title,
                           subtitle = subtitle,
                           description = description,
                           departures = departures,
                           tours = tours,
                           )


@app.route('/tours/<id>/')
def tour(id):
    t = tours[int(id)]
    tour1 = t['departure']
    departure = departures[tour1]
    return render_template('tour.html', id=id,
                           title = title,
                           subtitle=subtitle,
                           description=description,
                           departure=departure,
                           tour=tours[int(id)],
                           departures = departures,
                           )

if __name__ == '__main__':
    app.run()
