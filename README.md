# Goal

During my internship at Palexpo, I was asked to create a website for exchanging items as a training exercice.
The goal is to extend the life of the items we don't use anymore and make it easy to give them a second life and dimish our carbon footprint.
You can exchange item with another item, loan it or give it.
You can create posts about your item, you have to give :
- the name of the post
- a description
- the state of the item
- a category
- and a location

You can create an account and send messages to the owner of the item.

# Installation

I will assume that you have python, pip and django installed already.

Clone the repo
```bash
git clone https://github.com/ArianDervishaj/projet-pal.git
```

Make an virtual environment and activate it.

```python
python3 -m venv .venv
source .venv/bin/activate
```

Then you can install the packages : 

``` python
pip install -r requirement.txt
```

Then run these to apply the database :

```python
python manage.py makemigrations
python manage.py migrate
```

Then you can run the server :

```python
python manage.py runserver
```



