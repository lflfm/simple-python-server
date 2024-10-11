docker-build:
	docker build -t flask-app .


docker-run:
	docker run -p 5000:5000 flask-app


docker-build-run: docker-build docker-run