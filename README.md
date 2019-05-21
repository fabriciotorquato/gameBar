
## Getting started
2. Navigate into the diretory ```[cd gameBar]```
3. Source the virtual environment ```[pipenv shell]```
4. Install the dependencies ```[pipenv install]```
5. Navigate into the frontend directory ```[cd frontend]```
5. Install the dependencies ```[yarn install]```

## Run the application
1. ```[pipenv shell]```
2. ```[cd backend ]```
3. ```[python manage.py makemigrations && python manage.py migrate && python manage.py runserver]```

1. ```[cd frontend]```
2. ```[yarn install ]```
3. ```[yarn start]```
4. [localhost:3000] (http://localhost:3000))

## Test
1. coverage run --source='.' manage.py test gameBar
2. coverage report -m