# Goal

During my internship at Palexpo, I was asked to create a website for exchanging items as a training exercice.
The goal is to extend the life of the items we don't use anymore and make it easy to give them a second life and dimish our carbon footprint.
You can exchange item with another item, lend it or give it.
You can create posts about your item, you have to give :
- the name of the post
- a description
- the state of the item
- a category
- specify the announce type (exchange, donation or loan)
- and a location

You can create an account and send messages to the owner of the item.

# Pre-requesite

- git
- python3
- python3-pip
- django

# Installation

I will assume that you have python, pip and django installed already.

1. Clone the repo

2. Make an virtual environment and activate it.

```python
python3 -m venv .venv
source .venv/bin/activate
```

3. Install the packages : 

``` python
pip install -r requirements.txt
```

4. Run these to apply the database :

```python
cd src
python manage.py makemigrations
python manage.py migrate
```

5. Run the server :

```python
python manage.py runserver
```

# Hardware configuration

This project was made on an iMac (Mid 2011) running MacOS High Sierra (10.13.6)



