from base.base_api import BaseAPI
from requests import Session
from support.errors import TokenNotFoundError, TokenNotGeneratedError


class Auth(BaseAPI):

    def __init__(self, session: Session, route: str, app_username, app_password):
        super().__init__(session, route)
        self.app_username = app_username
        self.app_password = app_password
        self.headers = {'accept': 'application/json',
                        "Content-Type": "application/x-www-form-urlencoded"}

    def register(self):
        self.post(f"{self.route}/register",
                  json={
                      "username": self.app_username,
                      "email": "admin_2@mail.com",
                      "first_name": "admin_2",
                      "last_name": "admin_2",
                      "password": self.app_password,
                      "role": "admin"
                  },
                  headers={'accept': 'application/json',
                           "Content-Type": "application/json"})

    def generate_token(self):
        response = self.post(f"{self.route}/token",
                             data={
                                 'username': self.app_username,
                                 'password': self.app_password,
                             },
                             headers=self.headers)
        if response.status_code == 200:
            token = response.json().get("access_token")
            if token is None:
                raise TokenNotFoundError
            return token
        else:
            print(self.app_password, self.app_username)
            raise TokenNotGeneratedError(status_code=response.status_code)
