run-dev:
	python3 app.py
build-dev:
	pip install -r requirements.txt
run-prod:
	uwsgi --http 127.0.0.1:5000 --module app:app
build-docker:
	docker build -t search_string_app:latest .
run-docker:
	docker run -d -p 5000:5000 search_string_app

