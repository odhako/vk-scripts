MANAGE := poetry run python manage.py

debug:
	poetry run python manage.py runserver #  --noreload

req:
	poetry export --without-hashes -f requirements.txt -o requirements.txt

wsgi:
	poetry run gunicorn task_manager.wsgi

push:
	git push heroku main

migrate:
	@$(MANAGE) migrate

shell:
	@$(MANAGE) shell_plus
