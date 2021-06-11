from tests.fixtures import get_new_user


def test_list_user_route(test_client):
    session_factory = test_client.app.container.db().session
    with session_factory() as session:
        get_new_user(session)

    response = test_client.get('/users/')
    assert response.status_code == 200
    assert len(response.json()) >= 1


def test_create_user_route(test_client):
    json_data = {
        "name": "Leonardo Freitas",
        "email": "leofreitas@email.com",
        "password": "12345678"
    }

    response = test_client.post('/users/',  headers={"X-Token": "coneofsilence"}, json=json_data)
    assert response.status_code == 200
    assert response.json().get('name') == json_data['name']
    assert response.json().get('email') == json_data['email']


def testdetail_user_route(test_client):
    session_factory = test_client.app.container.db().session
    with session_factory() as session:
        user = get_new_user(session)

        response = test_client.get(f'/users/{user.id}/')
        assert response.status_code == 200
        assert response.json().get('name') == user.name
        assert response.json().get('email') == user.email
