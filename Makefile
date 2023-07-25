VENV?=.venv
PYTHON?=$(VENV)/bin/python3
PIP?=$(PYTHON) -m pip

run:
	#@echo "\33[0;32m mongo DB API is Running!\033[0;32m"
	$(PYTHON) bd_interface/src/main.py


docker-up:
	@docker-compose up -d
	@echo 'docker-up'

install-poetry: docker-up
	@if ! command -v poetry &>/dev/null; then \
		echo "Installing poetry..."; \
		pip3 install poetry; \
	fi

venv: install-poetry
	@echo "Creating the venv..."
	@poetry install
	$(PIP) install --upgrade pip
	@echo "Starting the virtual environment..."
	@poetry shell

docker-down:
	@docker stop mongo-ctnr mongo-express-ctnr
	@docker rm -f mongo-ctnr mongo-express-ctnr
	@docker rmi mongo:latest mongo-express:latest
	@echo 'docker-down'

clean: docker-down
	@echo "removing recursively: *.py[cod]"
	find . -type f -name "*.pyc" -exec rm '{}' +
	find . -type d -name "__pycache__" -exec rm -rf '{}' +
	find . -type d -name ".pytest_cache" -exec rm -rf '{}' +
	find . -type d -name "*.egg-info" -exec rm -rf '{}' +
	rm -rf $(VENV) .pybuilder
	@echo "\033[31mNow, run the \`exit\` command to close the shell session created by poetry!\033[0m"