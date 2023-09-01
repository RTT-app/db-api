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
	@docker stop mongo-ctnr mongo-express-ctnr db-api-tcc
	@docker rm -f mongo-ctnr mongo-express-ctnr db-api-tcc
	@docker rmi mongo:latest mongo-express:latest db-api-tcc:latest
	@echo 'docker-down'

clean: docker-down
	@echo "removing recursively: *.py[cod]"
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rm -rf '{}' +
	find . -type d -name ".pytest_cache" -exec rm -rf '{}' +
	find . -type d -name "*.egg-info" -exec rm -rf '{}' +
	rm -rf $(VENV) .pybuilder
	@echo "\033[31mNow, run the \`exit\` command to close the shell session created by poetry!\033[0m"
