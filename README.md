# Oauth_JS_Django

This App demonstrates use of Django Oauth with Vanilla JS

## Brief Overview

This app uses django rest framework in the backend and Vanilla JS in the frontend. The purpose was to demonstrate how django can be used to create API's and a non django frontend can consume these APIs. The primary challenge faced was navigating through `CORS` errors. 

## Oauth Flow

Front end initiates the authenticate request to the provider. The provider sends the code back to the frontned. The front end sends this code to the backend. The backend verifies this code, generates access code, finds required details and sends the data back to the frontend

## Folder Structure

There are two folders in the project

1. Frontend
2. Backend

Frontend has two HTML and two JS files. The files handle initiating the Oauth flow and showing response from Backend.

Backend authenticates user, saves it to database and returns authentication tokens. The tokens ought to be passed in every subsequent request to identify the user. 

## Installation

Requirements for the project can be found in `requirements.txt`


