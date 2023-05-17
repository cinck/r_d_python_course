# <HW19> Task 3
class MyStr(str):
    """
     Redefines __str__ method.
     Returns upper case string.
    """
    def __str__(self, *args, **kwargs):
        return super().__str__().upper()


if __name__ == "__main__":
    mystr = MyStr("hi there. nice to meet you!")
    print(mystr)
