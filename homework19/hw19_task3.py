class MyStr(str):
    def __str__(self, *args, **kwargs):
        return super().__str__().upper()


if __name__ == "__main__":
    mystr = MyStr("hi there. nice to meet you!")
    print(mystr)
