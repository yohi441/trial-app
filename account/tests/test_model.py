import pytest

from django.contrib.auth import get_user_model

User = get_user_model()

@pytest.mark.django_db
def test_create_account():
    user = User.objects.create(email="test@email.com", username="testuser", password="testpassword")

    assert user.email == "test@email.com"
    assert user.username == "testuser"
