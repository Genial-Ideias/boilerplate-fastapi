from src.config.env import Env

def test_env():
    env = Env()

    config = {'TEST': True}
    env.config = config
    assert env.config == env._config
