from flask import request, abort
from random import choice, randint
from app import app, db
from db_models import *
from time import strftime, gmtime, localtime, time


def get_time_data(timestamp) -> str:
    """
    Returns string of time and date from timestamp formatted data taken from database.
    :param timestamp: 13-charactered timestamp
    :return:
    """
    timestamp = str(timestamp)[:-3]
    time_data = float(timestamp)
    return strftime("%d %b %Y %H:%M:%S", gmtime(time_data))


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
    if 'size' in request.args.keys():       # <HW35> Task 6. 'count' parameter renamed to 'size'
        try:
            count = int(request.args['size'])       # <HW35> Task 6. 'count' parameter renamed to 'size'
        except ValueError:
            return abort(400, 'Wrong parameters data')
    else:
        return 0
    if count <= 0:
        return abort(400, "Parameter can't be less than 1")
    return count


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


# <HW35> Task 8. Create new record in DB
def post_user() -> bool:
    """
    Creates new row in database table 'Users' from HTML form.
    Returns True if all data available and False if not enough data entered
    :return:
    """
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    try:
        year = int(request.form.get('year'))
    except ValueError:
        year = 0
    age = 2023 - year
    print(first_name, last_name, year)
    if not first_name or not last_name:
        return False
    user = Users(
        first_name=first_name,
        last_name=last_name,
        age=age
    )
    db.session.add(user)
    db.session.commit()
    return True


# <HW35> Task 8. Create new record in DB
def post_book() -> bool:
    """
    Creates new row in database table 'Books' from HTML form.
    Returns True if all data available and False if not enough data entered
    :return:
    """
    title = request.form.get('title')
    author = request.form.get('author')
    year = request.form.get('year')
    price = request.form.get('price')
    publisher_id = randint(1, 5)

    book = Books(
        title=title,
        author=author,
        year=year,
        price=price,
        publishing_house_id=publisher_id
    )
    db.session.add(book)
    db.session.commit()
    return True


# <HW35> Task 8. Create new record in DB
def post_purchase() -> bool:
    """
    Creates new row in database table 'Purchases' from HTML form.
    Returns True if all data available and False if not enough data entered
    :return:
    """
    user_id = request.form.get('user_id')
    book_id = request.form.get('book_id')
    u_valid = db.session.execute(db.select(Users).where(Users.id == user_id)).scalar()
    b_valid = db.session.execute(db.select(Books).where(Books.id == book_id)).scalar()
    print(u_valid, b_valid)
    if not u_valid or not b_valid:
        return False
    purchase = Purchases(
        user_id=user_id,
        book_id=book_id
    )
    db.session.add(purchase)
    db.session.commit()
    return True
