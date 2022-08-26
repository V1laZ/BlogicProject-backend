# BlogicProject-backend
Backend for **BlogicProject** done with **Django** framework.   
Frontend can be found [here](https://github.com/V1laZ/BlogicProject-frontend)

## Table of Contents
- [BlogicProject-backend](#blogicproject-backend)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Install dependencies](#install-dependencies)
  - [Start local server](#start-local-server)
- [Docs](#docs)
  - [Database](#database)
    - [Database scheme](#database-scheme)
    - [Managing the database](#managing-the-database)
  - [API](#api)
    - [Access token](#access-token)
    - [Clients](#clients)
    - [Client](#client)
    - [Advisors](#advisors)
    - [Advisor](#advisor)
    - [Contracts](#contracts)
    - [Contract](#contract)
## Prerequisites
- [Python 3](https://www.python.org/downloads/)
- [pipenv](https://pypi.org/project/pipenv/)
## Install dependencies
- Activate virtual environment in the project folder
```
pipenv shell
```
- Install dependencies
```
pipenv install
```
## Start local server
- Activate virtual environment in the project folder
```
pipenv shell
```
- Run the server
```
python manage.py runserver
```
- Server should be running at http://127.0.0.1:8000/

# Docs

## Database
Database is built with **Django** framework and is running on **SQLite** database engine. It comes with some pre-stored values as well as an admin account. Admin account can be accessed via these credentials:
- **Username**: vilaz
- **Password**: 316Tnl40&r3r
### Database scheme
![](https://imgur.com/6ugb6O4.png)

### Managing the database
To manage **values** in the database it is recommended to use the **Django admin panel** that can be accessed on http://127.0.0.1:8000/admin.

Altering **tables** should be done in the [models.py](/blogic/api/models.py) file.

## API
API is done with django REST framework. It handles HTTP calls from the front-end on the database. It currently handles calls for **Client**, **Advisor**, **Contract** and **user authentication**.   Default API route is http://127.0.0.1:8000/api
### Access token
To get data from database through the **API** you first need to get an **access token**. Access token can be extracted from **JSON Web Token** that the server returns if you send it valid credentials. Access token is valid for **1 day**.  

**Request**  
`POST` /token/

Example request in Angular:
```ts
import { HttpClient} from '@angular/common/http';

constructor(private http: HttpClient) { }

get_token(username: string, password: string) { 
  this.http.post('http://127.0.0.1:8000/api/token', {username, password}).subscribe({
      next: (data) => console.log(data),
      error: (error) => console.log(error)
    });
}
```

Example response:
```json
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY2MTMzODkyNiwiaWF0IjoxNjYxMjUyNTI2LCJqdGkiOiI3ZWZmYTk1MTM1MDU0N2VjOTU0NTYxYTY1OGNjYjdhNiIsInVzZXJfaWQiOiJ2aWxhejIifQ.7e5dlR1WyAcmTzrBszSaXC8uUWODjba-LW2DvT7r3lA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjYxMzM4OTI2LCJpYXQiOjE2NjEyNTI1MjYsImp0aSI6ImJlMDllNzA4MjllNDRlMTk4Y2U2MWUzOTg1ZWU1NzNhIiwidXNlcl9pZCI6InZpbGF6MiJ9.ilhiwSkKOIfiNCPWpjLTqqkZUouDyVDu89hesA8FN_s"
}
```

### Clients
Gets all available clients.

**Request**  
`GET` /clients/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getAllClients(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/clients/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "id": 1,
        "first_name": "Grant",
        "last_name": "Wolf",
        "email": "example@example.com",
        "phone": "756461611",
        "PIN": "850125/4420",
        "age": 37
    },
    {
        "id": 2,
        "first_name": "Keisha",
        "last_name": "Diaz",
        "email": "example3@example.com",
        "phone": "756465156",
        "PIN": "900125/8123",
        "age": 32
    }
]
```

### Client
Gets klient data for the specified client ID.

**Request**  
`GET` /clients/{id}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getClient(id: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/clients/' + id, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "id": 1,
    "first_name": "Grant",
    "last_name": "Wolf",
    "email": "example@example.com",
    "phone": "756461611",
    "PIN": "850125/4420",
    "age": 37
}
```

### Advisors
Gets all available advisors.

**Request**  
`GET` /advisors/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getAllAdvisors(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/advisors/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "id": 1,
        "first_name": "Ethel",
        "last_name": "Conrad",
        "email": "example2@example.com",
        "phone": "756186456",
        "PIN": "820318/8123",
        "vek": 40
    },
    {
        "id": 2,
        "first_name": "Shane",
        "last_name": "Mclaughlin",
        "email": "example44@example.com",
        "phone": "756189165",
        "PIN": "930125/5786",
        "age": 29
    }
]
```

### Advisor
Gets advisor data for the specified advisor ID.

**Request**  
`GET` /advisors/{id}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getAdvisor(id: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/advisors/' + id, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "id": 1,
    "first_name": "Ethel",
    "last_name": "Conrad",
    "email": "example2@example.com",
    "phone": "756186456",
    "PIN": "820318/8123",
    "age": 40
}
```

### Contracts
Gets all available contracts.

**Request**  
`GET` /contracts/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getAllContracts(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/contracts/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "reg_num": "0215651614",
        "institution": "CSOB",
        "client": 1,
        "manager": 1,
        "date_close": "2023-01-02",
        "date_valid": "2023-01-02",
        "date_end": "2023-01-03"
    },
    {
        "reg_num": "0231354189",
        "institution": "AEGON",
        "client": 1,
        "manager": 2,
        "date_close": "2023-01-03",
        "date_valid": "2023-01-03",
        "date_end": "2023-01-04"
    }
]
```

### Contract
Gets contract data for the specified contract reg_num.

**Request**  
`GET` /contracts/{reg_num}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/api";

getContract(ev_cislo: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/contracts/' + ev_cislo, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "reg_num": "0215651614",
    "institution": "CSOB",
    "client": 1,
    "manager": 1,
    "date_close": "2023-01-02",
    "date_valid": "2023-01-02",
    "date_end": "2023-01-03"
}
```
