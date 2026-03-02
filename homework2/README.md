# Project Structure
```
cs4300/
|-- homework2/
|   |-- README.md
|   |-- requirements.txt
|   |-- movie_theater_booking/
|   |   |-- manage.py
|   |   |-- db.sqlite3
|   |   |-- bookings/
|   |   |   |-- templates/bookings/
|   |   |-- movie_theater_booking/
|   |   |-- tests/
|   |   |   |-- features/
|   |   |   |-- steps/
|   |   |   |   |-- pageobjects/
```

### ../cs4300/homework2/
Inside of the cs4300/homework2 directory, there are 2 files `README.md` and `requirements.txt` and a subdirectory for the main project implementation `movie_theater_booking`.

- **README.md**: describing the structure, setup, and instructions to run application
- **requirements.txt**: specifying the required python packages for this program
- **movie_theater_booking**: directory containing the main project implementation

### ../movie_theater_booking/
Contains the main implementation of the application and the database.

- **manage.py**: script used to manage and run the application
- **db.sqlite3**: database used by the website
- **movie_theater_booking**: sub directory containing website configuration
- **bookings**: bookings directory application defining models, views, and tests used by the website

### ../movie_theater_booking/bookings/
The main application where a majority of the funcionality is defined along with styling and pages

- **templates/bookings**: directory where html templates used by application are defined
- **urls.py**: defines the urls which views can be access through
- **tests.py**: defines integration and unit tests for the application and api
- **views.py**: defines viewsets used by application
- **models.py**: defines the main models used by application
- **serializers.py**: defines the serializers used to convert model instances to JSON

### ../movie_theater_booking/tests/
The Tests directory defines the behave tests, where the features are defined in the Gherkin formate in the features subdirectory, and the tests are implemented in the steps directory

# Setup

### Requirements

Python 3.12.3

## Step 1. Create Virtual Environment
```
python3 -m venv venv_name --system-site-packages
```

## Step 2. Activate Virtual Environment
```
source venv_name/bin/activate
```

## Step 3. Install Dependencies From requirements.txt
From `cs4300/homework2/movie_theater_booking` run pip install on the requirements file to install all required dependencies inside.
```
pip install -r requirements.txt
```

# How To Run Application

From `cs4300/homework2/movie_theater_booking`

```
python3 manage.py runserver 0.0.0.0:3000
python -m gunicorn movie_theater_booking.asgi:application -k uvicorn.workers.UvicornWorker --bind 0.0.0.0:3000
```

# How to Run Tests
From `cs4300/homework/movie_theater_booking`

To execute integration and unit tests run
```
python3 manage.py test
```

To execute behave tests
```
python3 manage.py behave
```

# How to use API
Access the API through the following end points

Api end points are:
```
/api/movies/
/api/seat/
/api/bookings/
```
