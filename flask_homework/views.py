from flask import abort, request, redirect, render_template, session
from app import app
from opfuncs import *
from sessioninfo import *
from contextdata import *


# <HW33> Task 1. Function '-GET/users'
@app.get('/users/')     # Doesn't work without / in the end ('/users'). Why?
def get_users():
    """
    Returns HTML code with list of random amount of random names.
    :return:
    """
    context = ContextIndex(title='Users')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    count = get_count()     # <HW33> Task 7. /users and /books return requested amount of items by 'count' parameter

    usernames = {}
    for i in range(count):
        usernames[i+1] = get_random_name()

    context.update('block_title', 'Users')
    context.update('usernames', usernames)

    return render_template('users/users.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW33> Task 2. Function '-GET/users' + url-parameter
@app.get('/users/<int:user_id>')
def get_user(user_id):
    """
    Returns HTML with random user if even user_id parameter passed, otherwise aborts with 404 fault.
    :param user_id:
    :return:
    """
    context = ContextIndex(title='Users')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    if user_id % 2 != 0:
        abort(404, 'Not found')
    elif user_id:
        u_name = {user_id: get_random_name()}
        context.update('block_title', 'User')
        context.update('usernames', u_name)

        return render_template('users/users.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW33> Task 1. Function '-GET/books'
@app.get('/books/')
def get_books():
    """
    Returns HTML lis of random quantity of random book names.
    :return:
    """
    context = ContextIndex(title='Books')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    count = get_count()     # <HW33> Task 7. /users and /books return requested amount of items by 'count' parameter
    book_list = []
    for i in range(count):
        book_list.append(get_random_book())
    context.update('block_title', 'Books')
    context.update('book_list', book_list)

    return render_template('books/books.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW33> Task 2. Function '-GET/books' + url-parameter
@app.get('/books/<string:title>')
def get_book(title: str):
    """
    Returns HTML with capitalized parameter 'title'
    :param title:
    :return:
    """

    context = ContextIndex(title='Books')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    book_list = [title.capitalize()]
    context.update('title', 'Books')
    context.update('block_title', 'Selected book')
    context.update('book_list', book_list)

    return render_template('books/books.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW33> Task 3. Function '-GET/params'
@app.get('/params')
def get_params():
    """
    Returns HTML table of request parameters.
    :return:
    """

    context = ContextIndex(title='Parameters')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    context.update('block_title', 'Accepted arguments')
    context.update('args', request.args)

    return render_template('params/params.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW33> Task 4. Function GET, POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET method returns HTML form for login
    POST method redirects to '/users' if login data verified successfully or aborts with error code 400.
    :return:
    """
    context = ContextInit()       # <HW34> Task 3. Check for username in session
    if context.user_name:
        return redirect('/')
    if request.method == 'GET':
        context.update('title', 'Login')
        context.update('block_title', 'Login')
        return render_template('login/login.html', **context.data), 200     # <HW34> Task 1. Template and context

    elif request.method == 'POST':
        user_name = request.form.get('name')
        password = request.form.get('password')
        if not user_name or not password:
            abort(400, 'No data entered')
        validation = validate_login(user_name, password)    # <HW33> Task 8. Login validation.
        if validation['status']:
            start_session(user_name)     # <HW34> Task 2. Adding username to session
            return redirect('/users')
        else:
            abort(400, validation['description'])


@app.route('/errors/<int:code>')
def get_custom_error(code):
    """
    Returns errors 404 and 500
    :param code:
    :return:
    """
    if code == 500:
        return abort(500)
    else:
        return abort(404)


# <HW33> Task 6. Function '-GET/'
@app.get('/')
def get_root_page():
    """
    Returns HTML with links to other pages: '/login', '/users', '/books', '/params', '/errors'
    :return:
    """
    context = ContextIndex('Homepage')
    welcome_text = 'Welcome to homepage!'
    if not context.user_name:
        welcome_text = 'Welcome! Please login!'
    context.update('welcome_text', welcome_text)

    return render_template('index.html', **context.data)     # <HW34> Task 1. Template and context
