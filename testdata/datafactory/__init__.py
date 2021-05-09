from dataclasses import dataclass
from dataclasses_jsonschema import JsonSchemaMixin


@dataclass()
class Model(JsonSchemaMixin):

    @staticmethod
    def parse(data: dict, type_of_model: type):
        return type_of_model.from_dict(data)


