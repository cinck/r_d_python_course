from flask import redirect, session
from app import app
from sessioninfo import *


class ContextInit:
    def __init__(self):
        self.user_name = verify_session()
        self.data = {'user_name': self.user_name}

    def update(self, var_name: str, value):
        self.data[var_name] = value


class ContextBasic(ContextInit):

    pages = ['users', 'books', 'params', 'errors', 'hello', 'json', 'html', '']

    def __init__(self):
        super().__init__()
        if self.user_name:
            self.pages[-1] = 'logout'
        else:
            self.pages[-1] = 'login'
        self._set_static_values_()

    def _set_static_values_(self):

        self.data['pages'] = self.pages


class ContextIndex(ContextBasic):

    def __init__(self, title: str):
        super().__init__()

        self.data['title'] = title


