from flask import abort, request, redirect, render_template, session
from app import app, db
from opfuncs import *
from sessioninfo import *
from contextdata import *
from db_models import *


# <HW35> Task 8. Post methods
@app.post('/users')
def post_users():
    posted = post_user()
    return redirect(f'/users/?post={posted}')


# <HW35> Task 5. Endpoint updated
@app.get('/users/')     # Doesn't work without / in the end ('/users'). Why?
def get_users():
    """
    Returns HTML code with list of random amount of random names.
    :return:
    """
    context = ContextIndex(title='Users')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    count = get_count()     # <HW35> Task 6. /users and /books return requested amount of items by 'size' parameter

    usernames = {}
    users = db.session.execute(db.select(Users)).scalars()
    print(type(users))
    i = 0
    for item in users:
        usernames[item.id] = f'{item.first_name} {item.last_name}, {item.age}'
        i += 1
        if count != 0 and i >= count:
            break
    if count > i:
        usernames[''] = f' = {i} of {i} showed ='

    context.update('block_title', 'Users')
    context.update('usernames', usernames)
    if request.values.get('post') == 'True':
        context.update('posted', 'Record added')
    elif request.values.get('post') == 'False':
        context.update('posted', 'Failed to create')

    return render_template('users/users.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW35> Task 5. Endpoint updated
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

    if user_id == 0:
        abort(404, "ID can't be zero")

    u_data = db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()
    if u_data:
        u_name = {u_data.id: f'{u_data.first_name} {u_data.last_name}, {u_data.age}'}
    else:
        abort(404, 'ID out of range')

    context.update('block_title', 'User')
    context.update('usernames', u_name)

    return render_template('users/users.html', **context.data), 200    # <HW34> Task 1. Template and context


# <HW35> Task 8. Post methods
@app.post('/books')
def post_books():
    posted = post_book()
    return redirect(f'/books/?post={posted}')


# <HW35> Task 5. Endpoint updated
@app.get('/books/')
def get_books():
    """
    Returns HTML lis of random quantity of random book names.
    :return:
    """
    context = ContextIndex(title='Books')
    if not context.user_name:       # <HW34> Task 3. Check for username in session and redirect to /login if not
        return redirect('/login')

    count = get_count()     # <HW35> Task 6. /users and /books return requested amount of items by 'size' parameter

    book_list = []
    books = db.session.execute(db.select(Books)).scalars()

    i = 0
    for item in books:
        b_data = f'{item.title}, {item.author}, {item.year} - price: {item.price} UAH'
        book_list.append(b_data)
        i += 1
        if count != 0 and i >= count:
            break

    context.update('block_title', 'Books')
    context.update('book_list', book_list)
    if request.values.get('post') == 'True':
        context.update('posted', 'Record added')
    elif request.values.get('post') == 'False':
        context.update('posted', 'Failed to create')

    return render_template('books/books.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW35> Task 5. Endpoint updated
@app.get('/books/<int:book_id>')
def get_book_by_id(book_id):
    context = ContextIndex(title='Books')
    if not context.user_name:
        return redirect('/login')

    if book_id <= 0:
        abort(404, "ID can't be less than 1")

    b_data = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    if b_data:
        book = [f'-= {b_data.id} =- {b_data.title}, {b_data.author}, {b_data.year} - price: {b_data.price} UAH']
    else:
        abort(404, 'ID out of range')

    context.update('block_title', 'Books')
    context.update('book_list', book)

    return render_template('books/books.html', **context.data), 200


# <HW35> Task 5. Endpoint updated
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
    context.update('title', 'Book')
    context.update('block_title', 'Selected book')
    context.update('book_list', book_list)

    return render_template('books/books.html', **context.data), 200     # <HW34> Task 1. Template and context


# <HW35> Task 8. Post methods
@app.post('/purchases')
def post_purchases():
    posted = post_purchase()
    return redirect(f'/purchases?post={posted}')


# <HW35> Task 5. Endpoint created
@app.get('/purchases/<int:purchase_id>')
@app.get('/purchases')
def get_purchases(purchase_id: int = 0):
    context = ContextIndex(title='Purchases')
    if not context.user_name:
        return redirect('/login')

    context.update('block_title', 'Purchases')
    if request.values.get('post') == 'True':
        context.update('posted', 'Record added')
    elif request.values.get('post') == 'False':
        context.update('posted', 'Failed to create')

    purchases_list = []

    if purchase_id:             # <HW35> Task 7.
        query = db.select(Purchases).join(Users).join(Books).where(Purchases.id == purchase_id)
        p = db.session.execute(query).scalar()
        if not p:
            abort(404, 'No such item')
        purchase = f"{p.user.first_name} {p.user.last_name} bought '{p.book.title}'"
        context.update('block_title', f'Purchase #{p.id}')
        context.update('purchase', purchase)
    else:
        count = get_count()         # <HW35> Task 6. Requested quantity of records

        purchases = db.session.execute(db.select(Purchases).join(Users).join(Books)).scalars()

        i = 0
        for item in purchases:      # <HW35> Task 7. Detailed purchase info
            p_data = f'''
                #{item.id}# Customer {item.user.first_name} {item.user.last_name}
                 bought book '{item.book.title}', {get_time_data(item.date)}(UTC)
                 '''
            purchases_list.append(p_data)
            i += 1
            if count != 0 and i >= count:
                break
        if count > i:
            purchases_list.append(f'{i} of total {i} items displayed')

        context.update('purchases', purchases_list)

    return render_template('purchases/purchases.html', **context.data), 200


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
