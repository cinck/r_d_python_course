class User:

    def __init__(self, name: str):
        self.name = name

    def __eq__(self, other):

        if isinstance(other, User) and self.name.lower() == other.name.lower():
            return True
        else:
            return False


if __name__ == "__main__":
    user1 = User("Sponge Bob")
    user2 = User("sponge bob")
    user3 = User("Sponge_Bob")
    print(user1 == user2)           # True
    print(user1 == user3)           # False
    print(user1 == "Sponge Bob")    # False

