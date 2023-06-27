# cars_api

A simple example of using Fast API in Python.

## Preconditions:

- Python 3

## Run local

### Install dependencies

```
pip install -r requirements.txt
```

### Run server

```
uvicorn app.main:app --reload
```

### Run test

```
pytest app/test.py
```

## Run with docker

### Run server

```
docker-compose up -d --build
```

### Run test

```
docker-compose exec app pytest test/test.py
```

## API documentation (provided by Swagger UI)

```
http://127.0.0.1:8000/docs
```

### Run server

```
docker-compose exec db psql --username=fastapi --dbname=fastapi_dev
```

## Best Practices 

* [PEP8](https://peps.python.org/pep-0008/)
* [Black](https://pypi.org/project/black/)
* [Zen of Python](https://peps.python.org/pep-0020/)
* [Solid Principles](https://www.freecodecamp.org/news/solid-principles-explained-in-plain-english/)
* [Commit Etiquettes](https://gist.github.com/robertpainsi/b632364184e70900af4ab688decf6f53)
* [Bash alias](https://www.geeksforgeeks.org/bash-scripting-working-of-alias/)
* [Structuring repo](https://docs.python-guide.org/writing/structure/)
