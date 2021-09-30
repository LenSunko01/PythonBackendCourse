# PythonBackendCourse

Contains project implemented for Pythond Backend Development course.

## Launching tests

Integration tests are located in tests/integration_tests.\
Unit tests are located in tests/unit_tests.

To run all integration tests use the following command in the terminal:
```
$ ./manage.py test notes/tests/integration_tests
```

To run all unit tests use the following command in the terminal:
```
$ ./manage.py test notes/tests/unit_tests
```

To run all e2e tests use the following command in the terminal:
```
$ ./manage.py test notes/tests/e2e_tests
```

To run particular test file use commands:
```
$ ./manage.py test notes.tests.integration_tests.test_services
$ ./manage.py test notes.tests.unit_tests.test_services
```
To run particular test method specify the test class and method name, e.g.:
```
$ ./manage.py test notes.tests.unit_tests.test_services.ServicesTest.test_getAllNotes
```
## Load testing
See "Load testing.pdf" file in project/docs directory.

## GraphQL
Endpoints are available in http://127.0.0.1:8000/graphql. \
See "GraphQL.pdf" file in project/docs directory.
