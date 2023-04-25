import pytest
from rest_framework import status

from ads.serializers import AdListSerializer
from tests.factories import AdFactory


@pytest.mark.django_db
def test_ad_create(client, user, category):
    data = {"name": "Мейнкунчик",
            "author": user.username,
            "price": 65,
            "category": category.name}
    expected_data = {"id": 1,
                     "author": user.username,
                     "category": category.name,
                     "name": "Мейнкунчик",
                     "price": 65,
                     "description": None,
                     "is_published": False,
                     "image": None}
    response = client.post("/ads/", data=data)
    assert response.status_code == status.HTTP_201_CREATED
    assert response.data == expected_data
