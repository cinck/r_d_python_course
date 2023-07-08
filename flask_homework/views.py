from flask import abort, request, redirect, render_template, session
from app import app
from random import choice, randint
from sessioninfo import *
from contextdata import *


class Context:
    def __init__(self):
        self.data = {}

    def update(self, param: str, value: any):
        self.data[param] = value


# context = Context()


def get_random_name() -> str:
    """
    Returns randomly generated name as 'Name Surname' string
    :return: str
    """
    names = (
        "Aron", "Andrew", "Abby", "Bob", "Bill", "Bertha", "Caren", "Cindy", "Cody", "Dave", "Diana", "David",
        "Daniel", "Ethon", "Emma", "Edna", "Flint", "Fineas", "Fiona", "Ginny", "George", "Gary", "Howard",
        "Helen", "Harry", "Inga", "Irma", "Igor", "John", "Jake", "Jill", "Kevin", "Kelly", "Ken", "Linda",
        "Lester", "Leon", "Mike", "Monica", "Michael", "Nate", "Nataly", "Neil", "Olivia", "Oscar", "Oliver",
        "Peter", "Paula", "Paul", "Roy", "Rita", "Rupert", "Suzan", "Shon", "Sarah", "Tim", "Tracy", "Tom",
        "Usama", "Urii", "Victor", "Valentina", "Vera", "Walter", "William", "Wall", "Yen", "Yulia", "Yan",
        "Zemfira", "Zhanna", "Zoe"
    )

    surnames = (
        "Afron", "Aniston", "Abignale", "Burton", "Button", "Bushemi", "Charles", "Chagginton", "Clinton",
        "Davidoff", "Daniels", "Duda", "Evans", "Edmund", "Evaldas", "Forings", "Firewood", "Finnigan",
        "Gordons", "Gibbs", "Gabings", "Hasbro", "Hobbit", "Horton", "Insbruk", "Igniss", "Ittogh",
        "Jameson", "Jaqueling", "Junior", "Klein", "Konard", "Kingslee", "Lame", "Lovards", "Leonaps",
        "Mitchell", "Mortigan", "Morgan", "Novak", "Nolan", "Neason", "Oddiu", "Opec", "Onward", "Pierce",
        "Palloc", "Postman", "Richmond", "Rolls", "Rally", "Stivenson", "Stupped", "Sinclair", "Tally",
        "Trelony", "Tracer", "Ulrich", "Ubber", "Unicon", "Velasces", "Vinford", "Victoll", "Walles",
        "Willniev", "Waters", "Yangsted", "Yeden", "Yuong", "Zidane", "Zandaya", "Zacher"
    )
    return f"{choice(names)} {choice(surnames)}"


def get_names_list(qty: int):
    names_list = []
    for _ in range(qty):
        names_list.append(get_random_name())
    return names_list


def get_random_book() -> str:
    """
    Returns string with random book description.
    :return:
    """
    books = [
        "1984 by George Orwell, England, (1903-1950)",
        "A Doll's House by Henrik Ibsen, Norway (1828-1906)",
        "A Sentimental Education by Gustave Flaubert, France, (1821-1880)",
        "Absalom, Absalom! by William Faulkner, United States, (1897-1962)",
        "The Adventures of Huckleberry Finn by Mark Twain, United States, (1835-1910)",
        "The Aeneid by Virgil, Italy, (70-19 BC)",
        "Anna Karenina by Leo Tolstoy, Russia, (1828-1910)",
        "Beloved by Toni Morrison, United States, (b. 1931)",
        "Berlin Alexanderplatz by Alfred Doblin, Germany, (1878-1957)",
        "Blindness by Jose Saramago, Portugal, (1922-2010)",
        "The Book of Disquiet by Fernando Pessoa, Portugal, (1888-1935)",
        "The Book of Job, Israel. (600-400 BC)",
        "The Brothers Karamazov by Fyodor M Dostoyevsky, Russia, (1821-1881)",
        "Buddenbrooks by Thomas Mann, Germany, (1875-1955)",
        "Canterbury Tales by Geoffrey Chaucer, England, (1340-1400)",
        "The Castle by Franz Kafka, Bohemia, (1883-1924)",
        "Children of Gebelawi by Naguib Mahfouz, Egypt, (b. 1911)",
        "Collected Fictions by Jorge Luis Borges, Argentina, (1899-1986)",
        "Complete Poems by Giacomo Leopardi, Italy, (1798-1837)",
        "The Complete Stories by Franz Kafka, Bohemia, (1883-1924)",
        "The Complete Tales by Edgar Allan Poe, United States, (1809-1849)",
        "Confessions of Zeno by Italo Svevo, Italy, (1861-1928)",
        "Crime and Punishment by Fyodor M Dostoyevsky, Russia, (1821-1881)",
        "Dead Souls by Nikolai Gogol, Russia, (1809-1852)",
        "The Death of Ivan Ilyich and Other Stories by Leo Tolstoy, Russia, (1828-1910)",
        "Decameron by Giovanni Boccaccio, Italy, (1313-1375)",
        "The Devil to Pay in the Backlands by Joao Guimaraes Rosa, Brazil, (1880-1967)",
        "Diary of a Madman and Other Stories by Lu Xun, China, (1881-1936)",
        "The Divine Comedy by Dante Alighieri, Italy, (1265-1321)",
        "Don Quixote by Miguel de Cervantes Saavedra, Spain, (1547-1616)",
        "Essays by Michel de Montaigne, France, (1533-1592)",
        "Fairy Tales and Stories by Hans Christian Andersen, Denmark, (1805-1875)",
        "Faust by Johann Wolfgang von Goethe, Germany, (1749-1832)",
        "Gargantua and Pantagruel by Francois Rabelais, France, (1495-1553)",
        "Gilgamesh Mesopotamia, (c 1800 BC)",
        "The Golden Notebook by Doris Lessing, England, (b.1919)",
        "Great Expectations by Charles Dickens, England, (1812-1870)",
        "Gulliver's Travels by Jonathan Swift, Ireland, (1667-1745)",
        "Gypsy Ballads by Federico Garcia Lorca, Spain, (1898-1936)",
        "Hamlet by William Shakespeare, England, (1564-1616)",
        "History by Elsa Morante, Italy, (1918-1985)",
        "Hunger by Knut Hamsun, Norway, (1859-1952)",
        "The Idiot by Fyodor M Dostoyevsky, Russia, (1821-1881)",
        "The Iliad by Homer, Greece, (c 700 BC)",
        "Independent People by Halldor K Laxness, Iceland, (1902-1998)",
        "Invisible Man by Ralph Ellison, United States, (1914-1994)",
        "Jacques the Fatalist and His Master by Denis Diderot, France, (1713-1784)",
        "Journey to the End of the Night by Louis-Ferdinand Celine, France, (1894-1961)",
        "King Lear by William Shakespeare, England, (1564-1616)",
        "Leaves of Grass by Walt Whitman, United States, (1819-1892)",
        "The Life and Opinions of Tristram Shandy by Laurence Sterne, Ireland, (1713-1768)",
        "Lolita by Vladimir Nabokov, Russia/United States, (1899-1977)",
        "Love in the Time of Cholera by Gabriel Garcia Marquez, Colombia, (b. 1928)",
        "Madame Bovary by Gustave Flaubert, France, (1821-1880)",
        "The Magic Mountain by Thomas Mann, Germany, (1875-1955)",
        "Mahabharata, India, (c 500 BC)",
        "The Man Without Qualities by Robert Musil, Austria, (1880-1942)",
        "The Mathnawi by Jalal ad-din Rumi, Afghanistan, (1207-1273)",
        "Medea by Euripides, Greece, (c 480-406 BC)",
        "Memoirs of Hadrian by Marguerite Yourcenar, France, (1903-1987)",
        "Metamorphoses by Ovid, Italy, (c 43 BC)",
        "Middlemarch by George Eliot, England, (1819-1880)",
        "Midnight's Children by Salman Rushdie, India/Britain, (b. 1947)",
        "Moby-Dick by Herman Melville, United States, (1819-1891)",
        "Mrs. Dalloway by Virginia Woolf, England, (1882-1941)",
        "Njaals Saga, Iceland, (c 1300)",
        "Nostromo by Joseph Conrad, England,(1857-1924)",
        "The Odyssey by Homer, Greece, (c 700 BC)",
        "Oedipus the King Sophocles, Greece, (496-406 BC)",
        "Old Goriot by Honore de Balzac, France, (1799-1850)",
        "The Old Man and the Sea by Ernest Hemingway, United States, (1899-1961)",
        "One Hundred Years of Solitude by Gabriel Garcia Marquez, Colombia, (b. 1928)",
        "The Orchard by Sheikh Musharrif ud-din Sadi, Iran, (c 1200-1292)",
        "Othello by William Shakespeare, England, (1564-1616)",
        "Pedro Paramo by Juan Rulfo Juan Rulfo, Mexico, (1918-1986)",
        "Pippi Longstocking by Astrid Lindgren, Sweden, (1907-2002)",
        "Poems by Paul Celan, Romania/France, (1920-1970)",
        "The Possessed by Fyodor M Dostoyevsky, Russia, (1821-1881)",
        "Pride and Prejudice by Jane Austen, England, (1775-1817)",
        "The Ramayana by Valmiki, India, (c 300 BC)",
        "The Recognition of Sakuntala by Kalidasa, India, (c. 400)",
        "The Red and the Black by Stendhal, France, (1783-1842)",
        "Remembrance of Things Past by Marcel Proust, France, (1871-1922)",
        "Season of Migration to the North by Tayeb Salih, Sudan, (b. 1929)",
        "Selected Stories by Anton P Chekhov, Russia, (1860-1904)",
        "Sons and Lovers by DH Lawrence, England, (1885-1930)",
        "The Sound and the Fury by William Faulkner, United States, (1897-1962)",
        "The Sound of the Mountain by Yasunari Kawabata, Japan, (1899-1972)",
        "The Stranger by Albert Camus, France, (1913-1960)",
        "The Tale of Genji by Shikibu Murasaki, Japan, (c 1000)",
        "Things Fall Apart by Chinua Achebe, Nigeria, (b. 1930)",
        "Thousand and One Nights, India/Iran/Iraq/Egypt, (700-1500)",
        "The Tin Drum by Gunter Grass, Germany, (b.1927)",
        "To the Lighthouse by Virginia Woolf, England, (1882-1941)",
        "The Trial by Franz Kafka, Bohemia, (1883-1924)",
        "Trilogy: Molloy, Malone Dies, The Unnamable by Samuel Beckett, Ireland, (1906-1989)",
        "Ulysses by James Joyce, Ireland, (1882-1941)",
        "War and Peace by Leo Tolstoy, Russia, (1828-1910)",
        "Wuthering Heights by Emily Brontë, England, (1818-1848)",
        "Zorba the Greek by Nikos Kazantzakis, Greece, (1883-1957)",
    ]
    return f'{choice(books)}'


# <HW33> Task 7. /users and /books return requested amount of items by 'count' parameter
def get_count():
    """
    Extracts 'count' parameter from request, aborts if parameter validation fails
     or returns random number if parameter is not in request.
    :return:
    """
    if 'count' in request.args.keys():
        try:
            count = int(request.args['count'])
        except ValueError:
            return abort(400, 'Wrong parameters data')
    else:
        count = randint(1, 30)
    if not count:
        return abort(400, "Parameter can't be 0")
    return count


# <HW33> Task 1. Function '-GET/users'
@app.get('/users/')     # Doesn't work without / in the end ('/users'). Why?
def get_users():
    """
    Returns HTML code with list of random amount of random names.
    :return:
    """
    context = ContextIndex(title='Users')
    if not context.user_name:
        return redirect('/login')

    count = get_count()     # <HW33> Task 7. /users and /books return requested amount of items by 'count' parameter

    usernames = {}
    for i in range(count):
        usernames[i+1] = get_random_name()

    context.update('block_title', 'Users')
    context.update('usernames', usernames)

    return render_template('users/users.html', **context.data), 200


# <HW33> Task 2. Function '-GET/users' + url-parameter
@app.get('/users/<int:user_id>')
def get_user(user_id):
    """
    Returns HTML with random user if even user_id parameter passed, otherwise aborts with 404 fault.
    :param user_id:
    :return:
    """
    context = ContextIndex(title='Users')
    if not context.user_name:
        return redirect('/login')

    if user_id % 2 != 0:
        abort(404, 'Not found')
    elif user_id:
        u_name = {user_id: get_random_name()}
        context.update('block_title', 'User')
        context.update('usernames', u_name)

        return render_template('users/users.html', **context.data), 200


# <HW33> Task 1. Function '-GET/books'
@app.get('/books/')
def get_books():
    """
    Returns HTML lis of random quantity of random book names.
    :return:
    """
    context = ContextIndex(title='Books')
    if not context.user_name:
        return redirect('/login')

    count = get_count()     # <HW33> Task 7. /users and /books return requested amount of items by 'count' parameter
    book_list = []
    for i in range(count):
        book_list.append(get_random_book())
    context.update('block_title', 'Books:')
    context.update('book_list', book_list)

    return render_template('books/books.html', **context.data), 200


# <HW33> Task 2. Function '-GET/books' + url-parameter
@app.get('/books/<string:title>')
def get_book(title: str):
    """
    Returns HTML with capitalized parameter 'title'
    :param title:
    :return:
    """

    context = ContextIndex(title='Books')
    if not context.user_name:
        return redirect('/login')

    book_list = [title.capitalize()]
    context.update('title', 'Books')
    context.update('block_title', 'Selected book')
    context.update('book_list', book_list)

    return render_template('books/books.html', **context.data), 200


# <HW33> Task 3. Function '-GET/params'
@app.get('/params')
def get_params():
    """
    Returns HTML table of request parameters.
    :return:
    """

    context = ContextIndex(title='Parameters')
    if not context.user_name:
        return redirect('/login')

    context.update('block_title', 'Accepted arguments')
    context.update('args', request.args)

    return render_template('params/params.html', **context.data), 200


# <HW33> Task 8. Login validation.
def validate_login(name: str, password: str) -> dict:
    """
    Returns {'status': bool, 'description': str} dict.
    'status' = FAULT by default and TRUE if all checks passed.
    'description':
    'Invalid name'  - name less than 5 characters;
    'Invalid password' - password less than 8 symbols;
    'Inappropriate password' - there is no upper case and lower case letter and digit in string;
    'Success'- all checks passed when name is 5 or more characters, password is 8 or more characters
    and includes at least one lowercase letter, one upper case letter and one digit.
    :param name:
    :param password:
    :return:
    """
    status = False
    if not name or len(name) < 5:
        description = "Invalid name"
    elif not password or len(password) < 8:
        description = "Invalid password"
    else:
        l_letters = 'qwertyuioplkjhgfdsazxcvbnm'
        u_letters = l_letters.upper()
        nums = '1234567890'
        upper, lower, digits = [], [], []
        for i in password:
            if i in u_letters:
                upper.append(i)
            elif i in l_letters:
                lower.append(i)
            elif i in nums:
                digits.append(i)
        if len(upper) < 1 or len(lower) < 1 or len(digits) < 1:
            description = "Inappropriate password "
        else:
            status = True
            description = "Success"
    return {'status': status, 'description': description}


# <HW33> Task 4. Function GET, POST /login
@app.route('/login', methods=['GET', 'POST'])
def login():
    """
    GET method returns HTML form for login
    POST method redirects to '/users' if login data verified successfully or aborts with error code 400.
    :return:
    """
    context = ContextInit()
    if verify_session():
        redirect('/')
    if request.method == 'GET':
        context.update('title', 'Login')
        context.update('block_title', 'Login')
        return render_template('login/login.html', **context.data), 200

    elif request.method == 'POST':
        user_name = request.form.get('name')
        password = request.form.get('password')
        if not user_name or not password:
            abort(400, 'No data entered')
        validation = validate_login(user_name, password)    # <HW33> Task 8. Login validation.
        if validation['status']:
            start_session(user_name)     # Session added
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
    welcome_text = 'Welcome to homepage page!'
    if not context.user_name:
        welcome_text = 'Welcome! Please login!'
    context.update('welcome_text', welcome_text)

    return render_template('index.html', **context.data)
