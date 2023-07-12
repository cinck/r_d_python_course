import os
from dotenv import load_dotenv
from flask import redirect, session
from app import app

load_dotenv()

app.secret_key = os.getenv('SECRET_KEY')


# <HW34> Task 2. Adding username to session
def start_session(name: str):
    session['name'] = name
    return session['name']


def verify_session():
    if not session['name']:
        return None
    return session['name']


# <HW34> Task 4. /logout endpoint
@app.route('/logout')
def end_session():
    session['name'] = None
    return redirect('/login')