from flask import redirect, session
from app import app

app.secret_key = b"secret_key"


def start_session(name: str):
    session['name'] = name
    return session['name']


def verify_session():
    if not session['name']:
        return None
    return session['name']


@app.route('/logout')
def end_session():
    session['name'] = None
    return redirect('/login')