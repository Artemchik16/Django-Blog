migrate:
	python manage.py makemigrations
	python manage.py migrate

code-format-start:
	isort .
	black .