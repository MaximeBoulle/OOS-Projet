# Project - OO Systems Development

## Subject

The subject is free but rules are imposed:
- code at least two services communicating (one using the REST architecture, the
other the RPC architecture).
- Each service must have its own database (more than one type of database is
desirable : SQL, NoSQL…).
- Respect the rules given in the following project (to be adapted according to the
programming language): https://github.com/charroux/JavaCodingRules
- The services must be documented according to the Open API specification
(Swagger). Show screen shots in the Readme page oy your repository.
- Explain your project in the Readme page.
- The Rest service must be accessible via curl (give the list of the requests in the
Readme of your repository), or via a Javascript program (noted as a bonus) (give
screen shots in the Readme page) (separate the services from the Javascript)


## Firstly 

1. Create a virtual environment
```bash
python -m venv .venv
.venv\Scripts\Activate.ps1
```
2. Install the requirements
```bash
pip install -r requirements.txt
```
3. Create the database "library" on PostgreSQL
4. Configure the database PostgreSQL in the file database.py (services\REST\app\data\database.py)
```
DATABASE_URL = "dbname='library' user='postgres' password='admin' host='localhost'"
```


##  REST API - Library

- **FastAPI** : Framework for REST API in python
- **PostgreSQL** : Relational database for the library
- **Unittest**: Python's built-in unit testing framework.

### To start the REST server from the root
```bash
fastapi dev services/REST/app/main.py  
```


###   Get the list of books
```bash
curl http://127.0.0.1:8000/books/
```

###   Get a book by the ID

```bash
curl http://127.0.0.1:8000/books/{book_id}
```

###  OpenAPI definition (Swagger)
```bash
http://127.0.0.1:8000/docs
```

###  TEST REST
```bash
python -m unittest discover -s services/REST/tests"
```



# gRPC

This service communicates with REST API to get database information through REST API

### How I compiled the proto file
```bash
python -m grpc_tools.protoc -I./proto --python_out=./generated --grpc_python_out=./generated ./proto/books.proto
```

### To start the gRCP server from the root
```bash
pip install -r requirements.txt

python services/gRPC/grpc_server.py
```

### gRPC Service Endpoints

1. Get a book by ID (method: GetBook): The gRPC service makes a request to the REST API to fetch a book's details by its ID.
   
2. Get all books (method: GetAllBooks): This method retrieves the list of all books from the REST API.

