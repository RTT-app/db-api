from flask import Flask
from mongoengine import connect
from flask_pydantic_spec import FlaskPydanticSpec
from config.config import (
                DB,
                DB_HOST,
                DB_PORT,
                DB_USERNAME,
                DB_PASSWORD,
                MONGO_URI
            )

app = Flask(__name__)
spec = FlaskPydanticSpec('mongo-crud')
spec.register(app)

connect(
    db=DB,
    host=DB_HOST,
    port=int(DB_PORT),
    username=DB_USERNAME,
    password=DB_PASSWORD
)

from app.controllers import post_controller