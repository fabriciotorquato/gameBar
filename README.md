
## Getting started
2. Navigate into the diretory ```[cd gameBar]```
3. Source the virtual environment ```[pipenv shell]```
4. Install the dependencies ```[pipenv install]```
5. Navigate into the frontend directory ```[cd frontend]```
5. Install the dependencies ```[yarn install]```

## Run the application
1. ```[pipenv shell]```
2. ```[cd backend]```
3. ```[python manage.py makemigrations && python manage.py migrate && python manage.py runserver]```

1. ```[cd frontend]```
2. ```[yarn install]```
3. ```[yarn start]```
4. [localhost:3000] (http://localhost:3000))

## Test in backend
1. cd backend
2. pipenv shell
3. coverage run --source='.' manage.py test gameBar
4. coverage report -m

## Test in frontend
1. cd frontend
2. yarn start
3. yarn run e2e