from flask import Flask
from mongoengine import connect
from flask_pydantic_spec import FlaskPydanticSpec
#from flask_cors import CORS

app = Flask(__name__)
spec = FlaskPydanticSpec('mongo-crud')
spec.register(app)
#CORS(app)

connect(
    db='reddit-app-db',
    host='localhost',
    port=27017,
    username='guest',
    password='guest',
)

from app.controllers import post_controller