# Work at Olist

## Project Description

This project is built on Python Language and Django Rest Framework as a way to provide an API in order to save data for authors and their respective books.

## Instalation and test instructions

To run this project it's necessary to have python >= 3.6 installed and follow the steps below:

#### Install the virtual environment:
```sh
$ sudo apt install virtualenv
```

In order to create the virtual environment, it's necessary to run:

```sh
$ virtualenv --python=python3.6 .my_env
```

and then, activate it:

```sh
$ source .my_env/bin/activate
```

### Install the requirements

Once the virtual environment is activated, it's necessary to run the requirements:

```sh
$ pip install -r requirements.txt
```

### .env settings file

It's necessary to create a .env file at the root directory with the following entry:	
```sh
SECRET_KEY=AnythingYouWant
```

### Migrate the database

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

### Start the server

Now it's possible to start the server by running:

```sh
$ python manage.py runserver
```

## Testing

To run the tests:

```sh
$ python manage.py test
```

## EndPoint Examples

This application is deployed on 

```sh
https://library-testapi.herokuapp.com/
```

### Author's endpoints

In order to get the list of authors, it's necessary to do a GET action on:

```sh
https://library-testapi.herokuapp.com/v1/authors/
```

Output:

```sh

[
    {
        "id": 1,
        "name": "Luciano Ramalho"
    },
    {
        "id": 2,
        "name": "Osvaldo Santana Neto"
    },
    {
        "id": 3,
        "name": "David Beazley"
    },
    {
        "id": 4,
        "name": "Chetan Giridhar"
    },
    {
        "id": 5,
        "name": "Brian K. Jones"
    },
    {
        "id": 6,
        "name": "J.K Rowling"
    },
    {
        "id": 7,
        "name": "Luciano Ramalho"
    },
    {
        "id": 8,
        "name": "Osvaldo Santana Neto"
    },
    {
        "id": 9,
        "name": "David Beazley"
    },
    {
        "id": 10,
        "name": "Chetan Giridhar"
    },
    {
        "id": 11,
        "name": "Brian K. Jones"
    },
    {
        "id": 12,
        "name": "J.K Rowling"
    },
    {
        "id": 13,
        "name": "Aurelio Marinho Jargas"
    },
    {
        "id": 14,
        "name": "Danilo Gazzoli"
    },
    {
        "id": 15,
        "name": "Danilo Gazzoli Resende"
    }
]
``` 

```sh
Status: 200 OK
```

If you want to retrieve only one author:

```sh
https://library-testapi.herokuapp.com/v1/authors/{Author id}
Example:
https://library-testapi.herokuapp.com/v1/authors/1
```

Output:

``` sh
{
    "id": 1,
    "name": "Luciano Ramalho"
}
```

```sh
Status: 200 OK
```


if you wanna add an author, it's necessary a POST action on:

``` sh
https://library-testapi.herokuapp.com/v1/authors/

``` 

with the Json content:

``` sh
{"name" : "Agatha Cristie"}

```

Output:

``` sh
{
    "id": 16,
    "name": "Agatha Cristie"
}

```

```sh
Status: 201 Created

```


### Books's endpoints

If you want to get the list of books, do a GET action on:


```sh
https://library-testapi.herokuapp.com/v1/books/
```

Output:
```sh
[
    {
        "id": 2,
        "authors": [
            {
                "id": 2,
                "name": "Osvaldo Santana Neto"
            },
            {
                "id": 3,
                "name": "David Beazley"
            },
            {
                "id": 7,
                "name": "Luciano Ramalho"
            }
        ],
        "name": "Expressões regulares",
        "edition": 2,
        "publication_year": 2019
    },
    {
        "id": 3,
        "authors": [
            {
                "id": 1,
                "name": "Luciano Ramalho"
            },
            {
                "id": 2,
                "name": "Osvaldo Santana Neto"
            }
        ],
        "name": "TDD com python",
        "edition": 2,
        "publication_year": 2019
    },
    {
        "id": 4,
        "authors": [
            {
                "id": 1,
                "name": "Luciano Ramalho"
            },
            {
                "id": 2,
                "name": "Osvaldo Santana Neto"
            }
        ],
        "name": "TDD com python 3",
        "edition": 2,
        "publication_year": 2019
    }
]

```

```sh
Status: 200 OK
```

In order to retrieve only one book:

```sh
https://library-testapi.herokuapp.com/v1/books/{book id}

Example:

https://library-testapi.herokuapp.com/v1/books/3

```

Output:

```sh
{
    "id": 3,
    "authors": [
        {
            "id": 1,
            "name": "Luciano Ramalho"
        },
        {
            "id": 2,
            "name": "Osvaldo Santana Neto"
        }
    ],
    "name": "TDD com python",
    "edition": 2,
    "publication_year": 2019
}

```

```sh
Status: 200 OK
```

In order to add a book, it's necessary to do a POST action on:

```sh
https://library-testapi.herokuapp.com/v1/books/
```

with the Json Content:
```sh
{
 "name": "Mistério no Caribe",
 "edition": "1",
 "publication_year": 1964,
 "authors": [16]
            
}
```

Output:

```sh
{
    "id": 5,
    "name": "Mistério no Caribe",
    "edition": 1,
    "publication_year": 1964,
    "authors": [
        16
    ]
}
```

```sh
Status: 201 Created
```

If it's necessary to update a any field, then send a PATH action to:


```sh
https://library-testapi.herokuapp.com/v1/books/{Book id}/
Example:
https://library-testapi.herokuapp.com/v1/books/5/
```

with the Json content that must be updated:

```sh
{
 "edition": "2"
}
```

Output:

```sh
{
    "id": 5,
    "name": "Mistério no Caribe",
    "edition": 2,
    "publication_year": 1964,
    "authors": [
        16
    ]
}
```
```sh
Status: 200 OK
```


And, finally, if it's necessary to be delete, send a DELETE action to:

```sh
https://library-testapi.herokuapp.com/v1/books/{Book id}/
Example:
https://library-testapi.herokuapp.com/v1/books/5/
```

```sh
Status: 204: no Content
```


## Environment

This application was built on vim and Pycharm 2020.1 (Community Edition), running Ubuntu Linux:
```sh
Linux Inspiron 5.3.0-46-generic #38~18.04.1-Ubuntu SMP Tue Mar 31 04:17:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```






