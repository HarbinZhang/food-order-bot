
init:
	export FLASK_APP=hello.py | bash

run:
	docker run -p 5000:5000 food-order-bot:latest

rund:
	docker run -p 5000:5000 -d food-order-bot:latest

stop:
	docker stop $(docker ps -aq)