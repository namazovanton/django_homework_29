import pytest


@pytest.fixture
@pytest.mark.django_db
def access_token(client, django_user_model):
    # username = "Anton"
    # password = "LamborghiniHennessy30101998"
    django_user_model.objects.create_user(username="Anton", password="LamborghiniHennessy30101998", role='admin')
    response = client.post("/user/token/", {"username": "Anton",
                                            "password": "LamborghiniHennessy30101998"})
    print(response)
    print(response)
    print(response)
    print(response)
    print(response)

    result = response.data.get("access")

    return result


@pytest.fixture
@pytest.mark.django_db
def user_with_access_token(client, django_user_model):
    username = "Anton"
    password = "LamborghiniHennessy30101998"
    test_user = django_user_model.objects.create_user(username=username, password=password, role='admin')
    response = client.post("/user/token/", data={"username": username, "password": password})
    return test_user, response.data.get("access")
