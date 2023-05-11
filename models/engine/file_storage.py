#!/usr/bin/python3
"""
This program creates a simple flow of serialization/deserialization:
Instance <-> Dictionary <-> JSON string <-> file
Functions and classes:
    class FileStorage:
"""


class FileStorage:
    """serializes instances to a JSON file
    and deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """return __objects"""

        return FileStorage.__objects

    def new(self, obj):
        """adds a new object to __objects dictionary"""

        key = str(obj.__class__.__name__) + '.' + str(obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""

        from json import dump

        file_name = FileStorage.__file_path

        to_json = dict(FileStorage.__objects)
        for k, v in to_json.items():
            to_json[k] = v.to_dict()

        with open(file_name, "w", encoding="UTF-8") as f:
            dump(to_json, f)

    def reload(self):
        """deserializes the JSON file to __objects"""

        from json import load
        from models.base_model import BaseModel
        from models.user import User
        from models.amenity import Amenity
        from models.place import Place
        from models.city import City
        from models.review import Review
        from models.state import State

        file_name = FileStorage.__file_path
        try:
            with open(file_name, "r", encoding="UTF-8") as f:
                from_json = load(f)
                for k, v in from_json.items():
                    if 'BaseModel' in k:
                        from_json[k] = BaseModel(**v)
                    elif 'User' in k:
                        from_json[k] = User(**v)
                    elif 'State' in k:
                        from_json[k] = State(**v)
                    elif 'City' in k:
                        from_json[k] = City(**v)
                    elif 'Amenity' in k:
                        from_json[k] = Amenity(**v)
                    elif 'Place' in k:
                        from_json[k] = Place(**v)
                    elif 'Review' in k:
                        from_json[k] = Review(**v)

                FileStorage.__objects = dict(from_json)
        except FileNotFoundError:
            return
