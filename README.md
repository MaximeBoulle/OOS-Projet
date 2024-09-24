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


##  REST API - Library

- **FastAPI** : Framework for REST API in python
- **PostgreSQL** : Relational database for the library

###   Get the list of books
```bash
curl http://localhost:8080/books/
```

###   Get a book by the ID

```bash
curl http://localhost:8080/books/{book_id}
```

###  OpenAPI definition (Swagger)
```bash
http://127.0.0.1:8000/docs
```

###  TEST REST
```bash
```



# gRPC

- **Python** : 
- **MangoDB** : 


