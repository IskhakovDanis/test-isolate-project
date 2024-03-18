import os
from support.json_handler import JSONHandler
from dotenv import load_dotenv



class Creds:
    load_dotenv()
    DB_USER = os.environ.get("DB_USER")
    DB_PASS = os.environ.get("DB_PASS")
    DB_HOST = os.environ.get("DB_HOST")
    DB_PORT = os.environ.get("DB_PORT")
    DB_NAME = os.environ.get("DB_NAME")

    DATABASE_CONN_STRING = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Routes:
    BASE_URL = "http://127.0.0.1:8000"
    STORE = f"{BASE_URL}/store"
    PRODUCT = f"{BASE_URL}/product"
    AUTH = f"{BASE_URL}/auth"


class Config:
    ROOT_PATH = os.path.dirname(os.path.realpath(__file__))
    EXPECTED_DATA = os.path.join(ROOT_PATH, "dataset", "data.json")



class ExpectedData:
    STORES = JSONHandler.load_json(Config.EXPECTED_DATA)
    STORE = JSONHandler.load_json(Config.EXPECTED_DATA)[0]


