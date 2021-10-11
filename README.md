# Hyxoul Gallery App

This is an Independent project for Moringa Core Django module, Oct 2021.

## Description

Hyxoul gallery app is a photo gallery web application to showcase beautiful pictures. Users get can view photos uploaded by admin. Users can see photos based on the location, by clicking on the listed locations in the menu. They can also copy the link to a photo to paste at their discretion. They can also search for photos based on the categories.

## Features

- The home page allows users to see various images:
- User can see all images per location they were taken
- Users can also search for images based categories
- Admin can upload images from a django dashboard

## Technologies Used

    - Python 3.8
    - Django MVC framework
    - HTML, CSS and Bootstrap
    - Postgressql
    - Heroku

### Prerequisite

The Hyxoul project requires a prerequisite understanding of the following:

- Django Framework
- Python3.8
- Postgres
- Python virtualenv

## Setup and installation

#### Clone the Repo

#### Activate virtual environment

Activate virtual environment using python3.8 as default handler
`python3.8 -m venv --without-pip virtual && source virtual/bin/activate`

#### Install dependancies

Install dependancies that will create an environment for the app to run `pip install -r requirements.txt`

#### Create the Database

    - psql
    - CREATE DATABASE photos;

#### .env file

Create .env file and paste paste the following filling where appropriate:

    SECRET_KEY = '<Secret_key>'
    DB_NAME = 'gallery'
    DB_USER = '<Username>'
    DB_PASSWORD = '<password>'
    DEBUG = True

#### Run initial Migration

    python3.8 manage.py makemigrations pictures
    python3.8 manage.py migrate

#### Run the app

    python3.8 manage.py runserver
    Open terminal on localhost:8000

## Known bugs

Some of the funcionalities are not working as per now, but i am working on them.

## Contributors

    - Kinoti Gitonga
