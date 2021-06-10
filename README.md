## Boilerplate FastAPI - Core

#### Utilizar Python 3.8

### Instalação
- Clonar projeto:
    - ```git clone https://github.com/Genial-Ideias/boilerplate-fastapi.git```

- Criar ambiente virtual
    - ```python -m venv venv```

-  Com ambiente virtual ativado, instalar dependências:
    - ```pip install -r requirements.txt```

- Criar arquivo .env baseado no ```.env.example```
    ```text
    DATABASE_URL=sqlite:///./store.db
    ENVIRONMENT=development
    DEBUG=True
    ```

- rodar projeto:
    - ```python runserver.py```

- rodar testes:
    - ```pytest```

- rodar coverage:
    - ```coverage run -m pytest```
    - ```coverage html```
