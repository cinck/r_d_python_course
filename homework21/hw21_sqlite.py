import sqlite3 as sqli


def execute_queries(que: list):
    for q in que:
        print(q)
        cursor.execute(q)
        db_connect.commit()


def get_queries(file_path: str):
    try:
        with open(file_path) as file:
            queries = file.read()
    except FileNotFoundError:
        print("No such file")
        queries = []
    finally:
        if not queries:
            return []

        while "\n" in queries or "  " in queries:
            queries = queries.replace("\n", " ").replace("  ", " ")
        queries = queries.split(";")
        print(queries)
        res = []
        for q in queries:
            res.append(q.strip())
        print(res)
        return res


if __name__ == "__main__":
    db_connect = sqli.connect("hw21_db.sqlite")
    cursor = db_connect.cursor()
    exec_queries = get_queries("queries")
    execute_queries(exec_queries)
