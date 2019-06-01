## Insurance APP

[![Maintainability](https://api.codeclimate.com/v1/badges/ddb10332ab0cce466344/maintainability)](https://codeclimate.com/github/gofaniyi/insurance-api/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ddb10332ab0cce466344/test_coverage)](https://codeclimate.com/github/gofaniyi/insurance-api/test_coverage)

An assessement to solve the problems of managing different forms of Insurance

## Problem statement and Objective

Create a simple solution to solve for the rigid system around creating different Insurance risks for 
different customers in different industries.


## Description

The **insurance-app** is the backbone of an application for managing different forms of Insurance risks assets for BriteCore customers. The project is divided into two parts. The Frontend build on **VueJs - Javascript** and the Backend built on **Flask - Python**.


- Key Application features

1. Risk Type Management
2. Creation of Risks
3. User Authentication
4. User Registration


- FrontEnd

The FrontEnd is a VueJs application that I am serving as static pages through the Flask application. For more information on the Frontend development, please read more here


- BackEnd

The api built on Flask Rest API Framework, provides features for registering different forms of Insurance risks. This bothers around being able to set up risk-types with dynamic/custom attributes.

## Development Approach

Making the assumption that a Risk is created under a Risk Type category. Risk Type object have the ability to store 
the custom attributes that will be defined when creating these risks.

- Database Setup & Entity Relationship
The following tables were designed to manage the concept of these solution.
1. Companies
2. Users
3. RiskTypes
4. Attribute
5. Risks
The relationship between these tables is explained in the entity relation diagram below
![alt text](http://prntscr.com/nw7p91)
* Here is a link to the folder that contains the ORM classes for these tables. 
* Here is also a link to the image that shows the entity relationship diagram


## Other aspects of development

- Authentication: 
The authentication workflow works as follows:

1. Client provides email and password, which is sent to the server
2. Server then verifies that email and password are correct and responds with an auth token
3. Client stores the token and sends it along with all subsequent requests to the API
4. Server decodes the token and validates it
5. This cycle repeats until the token expires or is revoked. In the latter case, the server issues a new token.

- User Administration & Account Management

Seeing that different customers will have their accounts provisioned and manage their Risk Types differently. I have also designed the application to manage the Signing up of Users. Although companies are seeded into the database and you
can make your selection while creating your user account.


## Technology Stack - BackEnd

- Flask
- Flask RestPlus
- Marshmallow
- JSON Web Token
- Pytest


###  Setting Up For Local Development

-   Check that python 3 is installed:

    ```
    python --version
    >> Python 3.7.0
    ```

-   Install pipenv:

    ```
    brew install pipenv
    ```

-   Check pipenv is installed:
    ```
    pipenv --version
    >> pipenv, version 2018.10.13
    ```
-   Check that postgres is installed:

    ```
    postgres --version
    >> postgres (PostgreSQL) 10.1
    ```

-   Clone the activo-api repo and cd into it:

    ```
    git clone https://github.com/insurance-app.git
    ```

-   Install dependencies:

    ```
    pipenv install
    ```

-   Install dev dependencies to setup development environment:

    ```
    pipenv install --dev
    ```

-   Make a copy of the .env.sample file and rename it to .env and update the variables accordingly:

    ```
    FLASK_ENV=development # Takes either development, testing, staging or production
    API_BASE_URL_V1=/api/v1 # The base url for version 1 of the API
    FLASK_APP=manage.py
    DATABASE_URI = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_DATABASE_NAME" #Development and production postgres db uri
    TEST_DATABASE_URI = "postgresql://YOUR_DB_USER:YOUR_DB_PASSWORD@YOUR_HOST/YOUR_TEST_DATABASE_NAME"
    JWT_SECRET_KEY="" # Generate your secret key. You can use this code snippet below to generate it
    ```

-   How to generate a Secret Key
    ```
    import os
    secret_key = os.urandom(24)
    print(secret_key)
    ```

-   Activate a virtual environment:

    ```
    pipenv shell
    ```

-   Apply migrations:

    ```
    flask db upgrade
    ```

-   If you'd like to seed initial data to the database:

    ```
    flask seed
    ```

*   Run the application with either commands:

    ```
    flask run
    ```

*   Should you make changes to the database models, run migrations as follows

    -   Migrate database:

        ```
        flask db migrate
        ```

    -   Upgrade to new structure:
        ```
        flask db upgrade
        ```

*   Deactivate the virtual environment once you're done:
    ```
    exit
    ```

## Running tests and generating report

On command line run:

```
pytest
```

To further view the lines not tested or covered if there is any,

An `htmlcov` directory will be created, get the `index.html` file by entering the directory and view it in your browser.


## Deployment to AWS Lambda using Zappa

- Here is a link to the deployed version of the project: 

## Demo

Find below a guide on how to use the app.

## Login Credentials:

email: example@sample.com
password: example1234





I hope you find my concept of solving this problem helpful. :)