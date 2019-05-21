
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

1. Run this command to start the backend server in the ```[backend]``` directory: ```[python manage.py runserver]``` (You have to run this command while you are sourced into the virtual environment)
2. Run this command to start the frontend development server in the ```[frontend]``` directory: ```[npm install]``` (This will start the frontend on the adddress [localhost:3000](http://localhost:3000))

## Test
1. coverage run --source='.' manage.py test gameBar
2. coverage report -m