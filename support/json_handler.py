import json


class JSONHandler:

    @staticmethod
    def load_json(path):
        with open(path, "r") as file:
            json_content = json.load(file)
        return json_content

    @staticmethod
    def dump_json(path, data):
        with open(path, "w") as file:
            json.dump(data, file)


class JSONHandler:

    @staticmethod
    def load_json(path):
        with open(path, "r") as file:
            json_content = json.load(file)
        return json_content

    @staticmethod
    def dump_json(path, data):
        with open(path, "w") as file:
            json.dump(data, file)