test-run:
	poetry run flask run

flask:
	gunicorn --workers=4 --bind=127.0.0.1:5000 app:app


debug:
	poetry run python manage.py runserver

req:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

wsgi:
	poetry run gunicorn task_manager.wsgi

push:
	git push heroku main
