# BlogicProject-backend
Backend for **BlogicProject** done with **Django** framework.
- [BlogicProject-backend](#blogicproject-backend)
  - [Prerequisites](#prerequisites)
  - [Install dependencies](#install-dependencies)
  - [Start local server](#start-local-server)
- [Docs](#docs)
  - [Database](#database)
    - [Database scheme](#database-scheme)
    - [Managing the database](#managing-the-database)
  - [API](#api)
    - [Access token](#access-token)
    - [Klients](#klients)
    - [Klient](#klient)
    - [Poradces](#poradces)
    - [Poradce](#poradce)
    - [Smlouvas](#smlouvas)
    - [Smlouva](#smlouva)
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
![](https://imgur.com/kx5G41E.png)

### Managing the database
To manage **values** in the database it is recommended to use the **Django admin panel** that can be accessed on http://127.0.0.1:8000/admin.

Altering **tables** should be done in the [models.py](../blogic/api/models.py) file.

## API
API is done with django REST framework. It handles HTTP calls from the front-end on the database. It currently handles calls for **Klient**, **Poradce**, **Smlouva** and **user authentication**.   Default API route is http://127.0.0.1:8000/
### Access token
To get data from database through the **API** you first need to get an **access token**. Access token can be extracted from **JSON Web Token** that the server returns if you send it valid credentials. Access token is valid for **1 day**.  

**Request**  
`POST` /api/token

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

### Klients
Gets all available klients.

**Request**  
`GET` /klient/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getAllClients(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/klient/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "id": 1,
        "jmeno": "Grant",
        "prijmeni": "Wolf",
        "email": "example@example.com",
        "tel_cislo": "756461611",
        "rod_cislo": "850125/4420",
        "vek": 37
    },
    {
        "id": 2,
        "jmeno": "Keisha",
        "prijmeni": "Diaz",
        "email": "example3@example.com",
        "tel_cislo": "756465156",
        "rod_cislo": "900125/8123",
        "vek": 32
    }
]
```

### Klient
Gets klient data for the specified klient ID.

**Request**  
`GET` /klient/{id}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getClient(id: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/klient/' + id, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "id": 1,
    "jmeno": "Grant",
    "prijmeni": "Wolf",
    "email": "example@example.com",
    "tel_cislo": "756461611",
    "rod_cislo": "850125/4420",
    "vek": 37
}
```

### Poradces
Gets all available poradces.

**Request**  
`GET` /poradce/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getAllPoradces(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/poradce/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "id": 1,
        "jmeno": "Ethel",
        "prijmeni": "Conrad",
        "email": "example2@example.com",
        "tel_cislo": "756186456",
        "rod_cislo": "820318/8123",
        "vek": 40
    },
    {
        "id": 2,
        "jmeno": "Shane",
        "prijmeni": "Mclaughlin",
        "email": "example44@example.com",
        "tel_cislo": "756189165",
        "rod_cislo": "930125/5786",
        "vek": 29
    }
]
```

### Poradce
Gets poradce data for the specified poradce ID.

**Request**  
`GET` /poradce/{id}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getPoradce(id: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/poradce/' + id, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "id": 1,
    "jmeno": "Ethel",
    "prijmeni": "Conrad",
    "email": "example2@example.com",
    "tel_cislo": "756186456",
    "rod_cislo": "820318/8123",
    "vek": 40
}
```

### Smlouvas
Gets all available smlouvas.

**Request**  
`GET` /smlouva/

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getAllSmlouvas(): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/smlouva/', 
    {headers: httpHeaders});
  }
```

Example response:
```json
[
    {
        "ev_cislo": "0215651614",
        "instituce": "CSOB",
        "klient": 1,
        "spravce": 1,
        "dat_uzavreni": "2023-01-02",
        "dat_platnosti": "2023-01-02",
        "dat_ukonceni": "2023-01-03"
    },
    {
        "ev_cislo": "0231354189",
        "instituce": "AEGON",
        "klient": 2,
        "spravce": 1,
        "dat_uzavreni": "2023-01-03",
        "dat_platnosti": "2023-01-03",
        "dat_ukonceni": "2023-01-04"
    }
]
```

### Smlouva
Gets smlouva data for the specified smlouva ev_cislo.

**Request**  
`GET` /smlouva/{ev_cislo}

Example request in Angular:
```ts
import { HttpClient, HttpHeaders } from '@angular/common/http'

constructor(private http: HttpClient) { }

baseurl = "http://127.0.0.1:8000/";

getSmlouva(ev_cislo: number): Observable<any>{
    const httpHeaders = new HttpHeaders({
      'Content-type': 'application/json',
      'Authorization': 'Bearer ' + ACCESS_TOKEN
    })

    return this.http.get(this.baseurl + '/smlouva/' + ev_cislo, 
    {headers: httpHeaders});
  }
```

Example response:
```json
{
    "ev_cislo": "0215651614",
    "instituce": "CSOB",
    "klient": 1,
    "spravce": 1,
    "dat_uzavreni": "2023-01-02",
    "dat_platnosti": "2023-01-02",
    "dat_ukonceni": "2023-01-03"
}
```