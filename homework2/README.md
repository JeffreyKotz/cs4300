## project structure
```
cs4300/
|-- homework2/
|   |-- README.md
|   |-- requirements.txt
|   |-- movie_theater_booking/
|   |   |-- manage.py
|   |   |-- db.sqlite3
|   |   |-- bookings/
|   |   |-- movie_theater_booking/
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

## Setup

#### Requirements

Python 3.12.3

### Step 1. Create Virtual Environment
```
python3 -m venv venv_name --system-site-packages
```

### Step 2. Activate Virtual Environment
```
source venv_name/bin/activate
```

### Step 3. Install Dependencies From requirements.txt
From cs4300/homework2/ run pip install on the requirements file to install all required dependencies inside.
```
pip install -r requirements.txt
```

## How To Run Application

From cs4300/homework2/movie_theater_booking

```
python manage.py runserver 0.0.0.0:3000
```

## How to use API
Access the API through the following end points

Api end points are:
```
/api/movies/
/api/seat/
/api/bookings/
```
