# Oauth_JS_Django

This App demonstrates use of Django Oauth with other frameworks

## Brief Overview

This app uses django rest framework in the backend and Vanilla JS/FastAPI in the frontend. The purpose was to demonstrate how django can be used to create API's and a non django frontend can consume these APIs. The primary challenge faced was navigating through `CORS` errors. 

## Oauth Flow

The flow for login goes as follows:

* Front end initiates the authenticate request to the provider.
* The provider seeks permission and then sends a code back to the redirect url previously defined.
* The front end sends this code to the backend. 
* The backend verifies this code and generates access code
* The access code is used to gather user details and store in DB
* A JWT token is generated for the user and sent to the frontend
* This JWT is returned in the header of subsequent requests to verify the user
* After expiry of JWT user is asked to log in again

## Backend structure

The backend runs a django server at port 8000. It has a `Providers` table in database that stores details of each provider. The admin has to manually configure the required client secret,ID etc. Add providers to the table as you add them to the library

Current list of providers:

1. Google
2. Facebook
3. LinkedIn
4. Discord

Handling of each provider is done in the file `providers.py`. Modify this file to add more providers.


## Folder Structure

There are three folders in the project

1. Frontend
2. Frontend Fast API
3. Backend

## Installation

Requirements for the project can be found in `requirements.txt`

You also need to create an .env file to store environment variables. 

The structure of the file should be


```
SECRET_KEY = 
DATABASE = ''
USER = ''
PASSWORD=''
HOST=''
PORT=
DEBUG=0

```

# How to use it in you project

## Pre Configuration

You need to log in to the admin panel of django and add provider details. The name of provider must match the `<provider>` in the URLs.
Configure the redirect_uri of provider such that it redirects to `redirect/<provider>`

## There are 4 main API's you need to call:

1. `login/<provider>`: This will redirect to the login screen of the provider

2. `redirect/<provider>`: This will catch the authorization code in the redirect and get the required details. In case of client side authentication redirect to the frontend, grab the code and then send it to this API.

3. `generate_token/`: Send a post request with user social id and email to generate jwt

4. `validate/`: Validate the jwt. Returns user or exception if invalid   



