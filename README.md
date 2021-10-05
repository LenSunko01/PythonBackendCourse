# PythonBackendCourse

Contains project implemented for Pythond Backend Development course.

## Initial set-up
There are some files that have to be generated before the project is run.

This command will generate counter_pb2.py and counter_pb2_grpc.py inside the project/project/protos directory. Don't forget to replace DIR_PATH with the corresponding path to directory!
```
$ python -m grpc_tools.protoc -I DIR_PATH/project/project/protos/ --python_out=DIR_PATH/project/project/protos --grpc_python_out=DIR_PATH/project/project/protos DIR_PATH/project/project/protos/counter.proto
```

This command will generate counter_pb2.py and counter_pb2_grpc.py inside the project/outer/servers directory. Don't forget to replace DIR_PATH with the corresponding path to directory!
```
$ python -m grpc_tools.protoc -I DIR_PATH/project/outer/servers —python_out=DIR_PATH/project/outer/servers —grpc_python_out=DIR_PATH/project/outer/servers DIR_PATH/project/outer/servers/counter.proto
```
After running these commands you might get "ModuleNotFoundError: No module named 'counter_pb2'" error. This can be fixed by replacing "import counter_pb2 as counter__pb2" to "import protos.counter_pb2 as counter__pb2" in protos/counter_pb2_grpc.py file.
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
See "Load testing.pdf" file in docs directory.

## GraphQL
Endpoints are available in http://127.0.0.1:8000/graphql. \
See "GraphQL.pdf" file in docs directory.
