from config import AppConfigData
from flask import redirect, session
from app import app

app.secret_key = AppConfigData.SECRET_KEY


# <HW34> Task 2. Adding username to session
def start_session(name: str):
    session['name'] = name
    return session['name']


def verify_session():
    try:
        username = session['name']
    except KeyError:
        return None
    if not session['name']:
        return None
    return username


# <HW34> Task 4. /logout endpoint
@app.route('/logout')
def end_session():
    session['name'] = None
    return redirect('/login')