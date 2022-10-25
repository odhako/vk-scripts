debug:
	poetry run python manage.py runserver --noreload

test:
	poetry run python manage.py test

test-v:
	poetry run python manage.py test -v 1

req:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

wsgi:
	poetry run gunicorn vk_scripts.wsgi

push:
	git push heroku main

shell:
	poetry run python manage.py shell_plus

migrations:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

run:
	export DJANGO_SETTINGS_MODULE=vk_scripts.settings
	gunicorn vk_scripts.wsgi

deploy:
	#python manage.py collectstatic
	python manage.py makemigrations
	python manage.py migrate
	export DJANGO_SETTINGS_MODULE=vk_scripts.settings
	gunicorn vk_scripts.wsgi
