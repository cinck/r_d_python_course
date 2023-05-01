import sys
import re

# Program that reads text from file (specified either as program argument or input),
# finds all emails in it and replaces them with:
#  - '*@*'
#  - 'X*****@*****X'


def find_mails(text: str):
    """
    Returns set of all found e-mails in text
    :param text: any text
    :return: set of email addresses
    """
    mails = re.findall(r"\b[\w+.]+@\w+[\w+.]+\w+\b", text)
    return set(mails)


# <HW15> Task 2
def twostarsbysides(text: str, *args, **kwargs):
    """
    Returns text with all found emails replaced with '*@*'.
    Can receive tuple of specific mails to be found and replaced.
    :param text: any string
    :param mails: any list of e-mail addresses
    :return: modified 'text'
    """
    if args:
        mails = args[0]
    else:
        mails = find_mails(text)

    for mail in mails:
        text = text.replace(mail, "*@*")

    return text


# <HW15> Task 3
def firstlastvisible(text: str, *args, **kwargs):
    """
    Returns text with all found emails replaced with 'X****@*****X',
     where 'X' - first and last letter of e-mail.
    Can receive tuple of specific mails to be found and replaced.
    :param text: any string
    :param mails: any list of e-mail addresses
    :return: modified 'text'
    """

    if args:
        mails = args[0]
    else:
        mails = find_mails(text)

    for m in mails:
        at = m.find("@")
        hiden = m[0].upper()+'*'*(at-1)+"@"+'*'*(len(m)-at+1)+m[-1].upper()
        text = text.replace(m, hiden)

    return text


if __name__ == "__main__":
    if len(sys.argv) > 1:
        print(sys.argv)
        opened = sys.argv[1]                    # <HW15> Takes system argument
    else:
        opened = input("Type file name >> ")    # <HW15> Takes data from input
    try:
        with open(opened, "r") as opened_file:
            text = opened_file.read()
            print(text)
    except FileNotFoundError:
        print("File not found")
    if text:
        mails = find_mails(text)
        print(mails)
        print()
        print("Task 2\n", twostarsbysides(text))
        print()
        print("Task 3\n", firstlastvisible(text, mails))

