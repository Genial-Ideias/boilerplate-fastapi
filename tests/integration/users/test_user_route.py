from tests.fixtures import get_new_user


def test_list_users_route(test_client):
    session_factory = test_client.app.container.db().session
    with session_factory() as session:
        get_new_user(session)

    response = test_client.get('/users')
    assert response.status_code == 200
    assert len(response.json()) >= 1
