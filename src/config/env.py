import os
from dotenv import dotenv_values


class Env:

    def __init__(self):
        env_path = os.getcwd()
        self._config = {
            **dotenv_values(f'{env_path}/.env'),
            **os.environ
        }

    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, config):
        self._config = config

    def get_item(self, key: str, default=None):
        return self._config[key] if key in self._config else default


environment: Env = Env()