FROM python:3.10-alpine

WORKDIR /dbapi/

COPY /src /dbapi/src
COPY pyproject.toml pyproject.toml
COPY .env .env

RUN pip install --upgrade pip && pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install

ENTRYPOINT ["python3"]
CMD ["src/main.py"]