from src.infra.orm.factories import UserFactory


def get_new_user(session, **kwargs):
    user = UserFactory(**kwargs)
    # db = app.container.db().session
    session.add(user)
    session.commit()
    return user
