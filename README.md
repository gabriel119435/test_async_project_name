## test_async_project_name
this project is a showcase of sync/async development using django, with tests

#### commands before running app or tests:
```
$ docker run -d -e POSTGRES_PASSWORD=pass -e POSTGRES_USER=user -e POSTGRES_DB=db_name \
--rm --name temp_postgres -p 5432:5432 postgres:15.0-alpine
$ pyenv virtualenv 3.10.6 teste_async_env
$ pyenv activate teste_async_env
$ pip install -r requirements.txt
$ ./manage.py migrate
```

#### to run the app
```
$ ./manage.py fill_db
$ ./manage.py startapp simple_app
```

#### to run the tests
```
$ pytest
```

#### available request examples:
```
$ curl -v -X GET http://localhost:8000/dev/
$ curl -v -X POST http://localhost:8000/dev/ --data '{"name":"a","age":"20", "level":"junior"}'
$ curl -v -X DELETE http://localhost:8000/dev/?id=2
```
