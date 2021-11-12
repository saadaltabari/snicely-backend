from flask import (
    Flask,
    request,
    render_template,
    redirect,
    jsonify
)

# from decorators import authorize_admin_users_only
from models import db, UserText
from settings import SETTINGS


# Initialize the application
app = Flask(__name__)
app.config.from_mapping(SETTINGS)
db.init_app(app)


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
def validate_user_text():
    """
    text validation http
    """
    user_data = request.data
    res = perspective_func(user_data)
    return {'toxicity': res['toxicity']}


@app.route('/validate', methods=['POST'])
def store_user_text():
    """
    store user text to database
    """
    user_data = request.form
    sincely_user_text = UserText()
    sincely_user_text.user_text = user_data.get('name')
    sincely_user_text.save()
    res = perspective_func(user_data)
    return {'toxic text': res['toxic_text']}



if __name__ == '__main__':
    app.run()
