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
SECRET_KEY=AnyValueYouWant
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


## Environment

This application was built on vim and Pycharm 2020.1 (Community Edition), running Ubuntu Linux:
```sh
Linux Inspiron 5.3.0-46-generic #38~18.04.1-Ubuntu SMP Tue Mar 31 04:17:56 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
```






