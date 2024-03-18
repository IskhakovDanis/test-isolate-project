from requests import Session


class BaseAPI:

    def __init__(self, session: Session, route):
        self.session = session
        self.route = route

    def get(self, *args, **kwargs):
        response = self.session.get(*args, **kwargs)
        return response

    def post(self, *args, **kwargs):
        response = self.session.post(*args, **kwargs)
        return response