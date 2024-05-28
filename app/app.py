# import os
from flask import Flask, render_template, request ,abort
from weather_api import Weather, WeatherError


# def create_app():
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/city', methods=['GET', 'POST'])
def get_data():
    weather_instance = Weather()

    if request.method == 'POST':
        city = request.form['city']
        if city.replace(" ", "") == "" or any(char.isdigit() for char in city):
            return render_template('index.html', error_data="Input must include letters"), 400
        try:
            weather_data = weather_instance.get_week_weather_data(city)
            return render_template('index.html', weather_data=weather_data)
        except WeatherError as error:
            status_code = error.args[0]
            abort(status_code)

    return render_template('index.html')


@app.errorhandler(400)
def bad_request(error):
    return render_template('index.html', error_data="City/Country dont exist"), 400


@app.errorhandler(404)
def not_found(error):
    return render_template('error_page.html', description=str(error)), 404


@app.errorhandler(500)
def internal_server_error(error):
    return render_template('error_page.html', description=str(error)), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0')

