from flask import Flask, request, redirect, jsonify

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
    return jsonify(UserText.objects.all())


if __name__ == '__main__':
    app.run()
