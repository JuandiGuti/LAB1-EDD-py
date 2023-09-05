import json
class Person:
    def __init__(self, name, dpi, datebirth, address):
        self.name = name
        self.dpi = dpi
        self.datebirth = datebirth
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, DPI: {self.dpi}, Date of Birth: {self.datebirth}, Address: {self.address}"

    @classmethod
    def from_json(cls, json_str):
        data = json.loads(json_str)
        return cls(data["name"], data["dpi"], data["datebirth"], data["address"])