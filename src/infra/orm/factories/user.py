from factory import Factory, Faker

from src.infra.orm.entities import User


class UserFactory(Factory):

    class Meta:
        model = User

    name = Faker('name', locale='pt_BR')
    email = Faker('email')
    password = 'core!001fintech'
    is_active = True
