VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

run: docker-up
	@echo "\33[0;32m mongo DB API is Running!\033[0;32m"

docker-up:
	@docker build -t db-api-tcc .
	@docker-compose up -d
	@echo 'docker-up'

docker-down:
	@docker stop mongo-ctnr mongo-express-ctnr db-api-ctnr
	@docker rm -f mongo-ctnr mongo-express-ctnr db-api-ctnr
	@docker rmi mongo:latest mongo-express:latest db-api-tcc:latest
	@echo 'docker-down'

clean: docker-down
