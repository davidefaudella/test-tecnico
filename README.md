# INTRO

The app is composed by backend and frontend.

- The **backend** is a Rest API based on [Flask](https://flask.palletsprojects.com/en/2.0.x/) (Python), with a single POST endpoint that return the receipt details.
- The **frontend** is based on HTML/JS and [Tailwind](https://tailwindcss.com/) as CSS Framework

## TL;DR

- `cd backend` (move to backend)
- `pipenv install --dev` (install dependencies)
- `pipenv run python app.py` (run API server)
- `cd frontend` (move to frontend)
- `npm install` (install dependencies)
- `npm start` (serve the app)

Read below for more details

# BACKEND

## REQUIREMENTS

- [Python >=3.6](https://github.com/pyenv/pyenv)
- [pipenv](https://pipenv.pypa.io/en/latest/)

## INSTALLATION

- `cd backend`
- `pipenv install --dev`

## RUN SERVER (REST API)

- `pipenv run python app.py`

You can use [Postman](https://www.postman.com/downloads/) to test the endpoint:

- [POST] `http://127.0.0.1:5000/api/v1/receipts`

- Payload (`text/plain`):  
  `1 imported bottle of perfume at 27.99`  
  `1 bottle of perfume at 18.99`  
  `1 packet of headache pills at 9.75`  
  `3 box of imported chocolates at 11.25`

## TESTS

- `pipenv run pytest -v`

## TESTS with COVERAGE REPORT

- `pipenv run coverage run -m pytest -v;`  
  `pipenv run coverage report`

## TESTS with TOX

- Install [tox](https://tox.wiki/en/latest/), [tox-pyenv](https://github.com/tox-dev/tox-pyenv), [tox-pipenv](https://github.com/tox-dev/tox-pipenv) outside the virtual env  
  `pip install tox tox-pyenv tox-pipenv`

- Run outside the virtual env to test with  
  Python **3.6, 3.7, 3.8, 3.9, 3.10** (if installed with pyenv):  
   `tox -r`

# FRONTEND

## REQUIREMENTS

- [node](https://nodejs.org/en/)
- [npm](https://www.npmjs.com/package/npm)

## INSTALLATION

- `cd frontend`
- `npm install`

## RUN

- `npm start`
