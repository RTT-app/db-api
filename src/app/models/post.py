from mongoengine import Document, StringField, IntField

class Post(Document):
    title = StringField(required=True)
    self_text = StringField(required=True)
    comment = StringField(required=True)
    score = IntField(required=True)

    def __init__(self, title, self_text, comment, score):
        pass