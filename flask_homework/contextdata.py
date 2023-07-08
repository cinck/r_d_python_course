from flask import redirect, session
from app import app
from sessioninfo import *

# <HW34> Task 1. Context for templates.


class ContextInit:
    """
    Parent class (template) for context classes
    """
    def __init__(self):
        self.user_name = verify_session()
        self.data = {'user_name': self.user_name}

    def update(self, var_name: str, value):
        """
        Appends new items to context.
        :param var_name: variable name str()
        :param value: value
        :return:
        """
        self.data[var_name] = value


class ContextBasic(ContextInit):
    """
    Basic context class to generate general templated data
    """

    pages = ['users', 'books', 'params', 'errors', 'hello', 'json', 'html', '']

    def __init__(self):
        super().__init__()
        if self.user_name:       # <HW34> Task 4. Checks for username in session and places 'login' or 'logout' link
            self.pages[-1] = 'logout'
        else:
            self.pages[-1] = 'login'
        self._set_static_values_()

    def _set_static_values_(self):
        self.data['pages'] = self.pages


class ContextIndex(ContextBasic):
    """
    Index context class can be used to accumulate template data for standard content pages
    """
    def __init__(self, title: str):
        super().__init__()

        self.data['title'] = title


