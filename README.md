# PythonBackendCourse

Contains project implemented for Pythond Backend Development course.

## Launching tests

Integration tests are located in tests/test_views.py.\
Unit tests are located in tests/test_services.py.

To run all the tests use the following command in the terminal:
```
$ ./manage.py test notes/tests/
```

To run particular test file use commands:
```
$ ./manage.py test notes.tests.test_views
$ ./manage.py test notes.tests.test_services
```
To run particular test method specify the test class and method name, e.g.:
```
$ ./manage.py test notes.tests.test_services.ServicesTest.test_getAllNotes
```