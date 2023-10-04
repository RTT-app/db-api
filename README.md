# MongoDB CRUD API

This repository contains the source code for a CRUD (Create, Read, Update, Delete) API for MongoDB. The API is built using Python, and both the API server and the MongoDB database are containerized using Docker. Additionally, Mongo Express is included for database management and is also containerized. To automate the setup and teardown of the application, a Makefile is provided. To run the application, you'll need to create a `.env` file containing the necessary environment variables for connecting to the MongoDB instance.

## Features

- **CRUD Operations:** The API supports Create, Read, Update, and Delete operations on MongoDB documents.

- **Dockerized:** The entire application, including the API server, MongoDB, and Mongo Express, can be easily run in Docker containers.

- **Database Management:** Mongo Express is included to provide a web-based interface for managing the MongoDB database.

- **Automated Setup:** The Makefile automates the process of starting and stopping the Docker containers.

## Getting Started

### Prerequisites

Before running the application, make sure you have the following prerequisites installed:

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)
- Python 3.10 (for API development)
- MongoDB credentials (DB_NAME, DB_HOST, DB_PORT, DB_USERNAME, DB_PASSWORD) for connecting to the MongoDB instance.

The mongo DB environment variables mean, respectively:

```
DB_NAME --------> The name of the Data base.
DB_HOST --------> The host of the Data base.
DB_PORT --------> The port to access the Data base.
DB_USERNAME ----> The admin username used to access the Data Base.
DB_PASSWORD ----> The admin password used to access the Data Base.
```
### Running the Application

1. Clone this repository to your local machine:

```bash
$ git clone https://github.com/RTT-app/db-api.git
$ cd db-api
```
To run the API, run this command:

```bash
$ make run
```

Run the command below to clear all the files in the docker container from the application modules environment.

Run make command to stop containers and clean all files from the app:
```bash
$ make clean
```


Te swagger doc will be available at [localhost:5001/apidoc/swagger](http://localhost:5001/apidoc/swagger). You can access the API endpoints for data extraction and transformation. To access Mongo Express use [localhost:8081](http://localhost:8081) to manage the database.

### API Endpoints (fix endpoints)
- `/add-post` (POST): Persist a reddit comment in the MongoDB.
- `/get-post/<string:comment>` (GET): Return a specific comment from MongoDB.
- `/get-posts` (GET): List all comments in the MongoDB collection.
- `/delete-posts/<string:comment>` (DELETE): Delete an existing comment.
- `/delete-posts` (DELETE): Delete all comments from MongoDB.

### Customization

You can customize the API routes and data models in the `api/controllers` directory to fit your specific application needs.
