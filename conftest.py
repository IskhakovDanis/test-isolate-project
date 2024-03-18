import time

from base.auth import Auth
from requests import Session
from env_config import Routes
from routes.stores import Stores
from pytest import fixture


########################
# App fixtures
########################


@fixture(scope="session")
def create_session():
    return Session()


@fixture(scope="session")
def bearer_token(create_session):
    auth = Auth(session=create_session,
                route=Routes.AUTH,
                app_username="admin",
                app_password="admin")
    auth.register()
    yield auth.generate_token()


@fixture(scope="function")
def stores_route(create_session, bearer_token):
    yield Stores(create_session, Routes.STORE, bearer_token)
