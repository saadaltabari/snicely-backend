# Snicely Web application
This is the Python Flask web application that implements the backend system supporting the Snicely Chrome Application.

This application provides two HTTP endpoints:
* Get user history `http://127.0.0.1:5000/history`
* [WIP] Validate user text

### Setup and Installation

This application is delivered using Docker, Docker containers wrap up software and its dependencies into a standardized unit for software development and delivery that includes everything it needs to run.

* Install Docker from the following [link](https://www.docker.com/get-started). 


* Install the application.

```shell script
git clone git@github.com:saadaltabari/snicely-backend.git && cd snicely-backend
```

* Run the application with `docker-compose`.

```shell script
docker-compose -f docker-compose.local.yml up --build
```
The previous command will:

1. Install and run `mongo` database instance and pre-populate the database with data.

2. Setup web application, install all requirements and run the api

The application should now be running on http://127.0.0.1:5000/ . 


### Testing

Execute the following command to run unit tests
```shell
sh test.sh
```
