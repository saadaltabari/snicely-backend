from flask_mongoengine import MongoEngine


db = MongoEngine()


class UserText(db.Document):
    """
    User input text that was flagged
    for inappropriate language
    """
    meta = {'collection': 'usertext'}
    user_id = db.StringField()
    user_text = db.StringField()
    toxicity_score = db.DecimalField()
