from datetime import datetime

from flask import (
    Flask,
    request,
    render_template,
    redirect,
    jsonify
)
from flask_cors import CORS, cross_origin

# from decorators import authorize_admin_users_only
from handlers import PerspectiveAPIToxicityHandler
from models import db, UserText
from settings import SETTINGS


# Initialize the application
app = Flask(__name__)
app.config.from_mapping(SETTINGS)
db.init_app(app)
CORS(app)


@app.route('/history', methods=['GET'])
def user_flagged_text_history():
    """
    List User Flagged Text endpoint.
    Get the list of user text that was previously flagged as
    inappropriate language.

    responses:
        200:
            :return: json list of all flagged user text.
        403:
            Permission to view flagged user text list denied.
    """
    user_text_history = UserText.objects.all()
    return render_template('Language_History_Page_Snicely.html',
                           user_text_history=user_text_history)


@app.route('/validate', methods=['POST'])
@cross_origin()
def validate_user_text():
    """
    text validation http
    """
    user_data = request.form
    user_text = user_data.get('text')
    print(f"user text is {user_text}")
    handler = PerspectiveAPIToxicityHandler(user_text=user_text)
    is_toxic, toxic_text = handler.evaluate()
    request_time = datetime.now()

    if is_toxic:
        for text in toxic_text:
            snicely_user_text = UserText()
            snicely_user_text.user_text = text['text']
            snicely_user_text.user_id = "123"# default user_id for now
            snicely_user_text.toxicity_score = text['toxicity_score']
            snicely_user_text.date = request_time
            snicely_user_text.save()

    return {
        'is_toxic': is_toxic,
        'toxic_text': toxic_text
    }


if __name__ == '__main__':
    app.run()
