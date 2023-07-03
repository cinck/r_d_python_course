from flask import abort, request
from app import app
from random import choice, randint


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


@app.get('/users/')
def get_users():
    count = randint(1, 30)
    usernames = []
    for i in range(count):
        usernames.append(f"<h4>{i + 1}. {get_random_name()}</h4>")

    response = f'''
           <div>
           <h1>Users:</h1>
           {"".join(usernames)}
           </div>
           '''
    return response, 200


@app.get('/users/<int:user_id>')
def get_user(user_id):
    if user_id % 2 != 0:
        abort(404, 'Not found')
    elif user_id:
        user_name = get_random_name()
        response = f'<div><h1>User #{user_id}:</h1><h4>{user_name}</h4></div>'
        return response, 200
