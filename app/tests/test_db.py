from datetime import datetime
from models import UserText


user_id = "xyz2"
text= "Hi there, testing"
text_create_date=datetime.now()
toxicity_score=0.1


def test_saving_user_text():
    user_text_obj = UserText(
        user_id=user_id,
        user_text=text,
        date=text_create_date,
        toxicity_score=toxicity_score
    )
    user_text_obj.save()
    assert UserText.objects.count() == 1


def test_retrieving_user_text():
    user_text_obj = UserText.objects(
        user_id=user_id,
        user_text=text,
        date=text_create_date,
        toxicity_score=toxicity_score
    ).first()
    assert user_text_obj.user_id ==  user_id
    assert user_text_obj.user_text == text