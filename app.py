from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

API_KEY = '693dfdc789b3a2a73bc6f20c5cb9d437'
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?'

@app.route('/weather', methods=['GET'])
def get_weather():
    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter is missing'}), 400

    params = {'q': city, 'appid': API_KEY, 'units': 'metric'}
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        weather_info = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description']
        }
        return jsonify(weather_info), 200
    else:
        return jsonify({'error': 'Unable to fetch weather data'}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)
