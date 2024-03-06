# Car import example


## Setup

Create a virtual environment:

If not yet installed, install with pip:

`pip install virtualenv`

Create the virtual environment:

`virtualenv venv --python=python3.12`


Activate the virtual environment:

Windows:
`venv\Scripts\activate`

UNIX:

`source venv/bin/activate`
`. venv/bin/activate`

With virtualen environment activated:

Install the required modules:

`pip install -r requirements.txt`


Run the tests

`pytest tests.py -v`


