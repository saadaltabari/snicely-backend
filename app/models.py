from datetime import datetime

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
    date = db.DateTimeField()

    @property
    def formatted_tox_score(self):
        return f"{int(self.toxicity_score * 100)} %"

    @property
    def formatted_date(self):
        dt = datetime.fromisoformat(self.date)
        return dt.strftime("%m/%d/%Y, %H:%M:%S")
