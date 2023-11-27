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

For detailed API endpoint testing and documentation, refer to the Postman workspace

## Prerequisites
* Python
* Flask
* Request packages
* Postman for testing API endpoints
* API key generated from OpenWeatherMap API

## Brief Procedure
1. Install the required libraries.
2. To run the program we need to generate the API key using the OpenWeatherMap API key.
3. Run the application , once the code is compiled , open the Postman and create a new request to  `http://127.0.0.1:5000/weather` with the `GET` method.
4. Add a query parameter 'city' with the value being the city.
5. For example (city=Bangalore).
6. Once its done , send the request and get the output.To check the accuracy of the Output which contains the weather data by `OpenWeatherMap`

## Detailed explanation
1. Run the Python script using the virtual environment by using idle or VScode.
2. The script contains the base url `http://127.0.0.1:5000`. When you click on this url, you will see 404 error.
3. Now by creating the new Workspace in the Postman worksapce, set the request type to 'GET'.
4. In the URL column enter Enter the URL for your Flask API endpoint i.e, `http://127.0.0.1:5000/weather?`.
5. Click on the "Params" tab. In the "Key" column, enter `location`. In the "Value" column, enter the city for which you want to retrieve the weather information.
6. Click the send button the data will be retrieved in the form of JSON file.

## Screenshots
1.The VScode which contains the code

![Screenshot (8)](https://github.com/Tejasnyadav/Weather-backend-api/assets/150244013/2c4621ab-e356-4d70-bbcc-45afe8550740)

2.Data recieved in json file formate

![Screenshot (7)](https://github.com/Tejasnyadav/Weather-backend-api/assets/150244013/06de079a-4905-40f7-8b6c-3a6637a4d693)

