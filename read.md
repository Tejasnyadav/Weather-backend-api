# Weather-Backend API

This repository contains the code for a simple Flask-based backend API that retrieves weather forecast data based on user input location.

## Setup Instructions

1. Clone this repository.
2. Install Flask by running `pip install Flask`.
3. Replace 'YOUR_API_KEY' in `app.py` with your OpenWeatherMap API key.
4. Run the Flask app using `python app.py`.

## API Documentation

### Endpoints

- `/weather`
    - Method: GET
    - Parameters: `city`
    - Example Usage: `http://localhost:5000/weather?city=London`

### Postman Workspace
Find the Postman workspace [here](https://web.postman.co/workspace/bfa9bed4-5d5f-4c60-88ef-d600590350cf/documentation/31416772-70e29ce5-5da8-4801-8f2c-1299b7569a35).

For detailed API endpoint testing and documentation, refer to the Postman workspace.

