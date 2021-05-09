"""
This module contains the models for creating the Persons
"""

from utilities.randomizer import Randomize
from dataclasses import dataclass, field, asdict
import random
from typing import List
from testdata.datafactory import Model
from pprint import pprint
from dataclasses_jsonschema import JsonSchemaMixin

def get_random_pet_category():
    pets_category = {
        1: "Dog",
        2: "Cat",
        3: "Fish",
        4: "Mice",
        5: "Rabbit"
    }
    key = random.choice(list(pets_category.keys()))
    return Category(key, pets_category[key])


def get_availability_status():
    status = ["available", "pending", "sold"]
    return random.choice(status)


def create_tags(number=Randomize().random_short_integer(0, 5)):
    lst = []
    for _ in range(number):
        lst.append(Tag(Randomize().random_long_integer(), Randomize().random_words()))
    return lst


@dataclass
class Category(JsonSchemaMixin):
    id: int
    name: str


@dataclass
class Tag(JsonSchemaMixin):
    id: int = field(default_factory=Randomize().random_long_integer)
    name: str = field(default_factory=Randomize().random_words)


# @dataclass
# class Tags(JsonSchemaMixin):
#     tags: List[Tag]
#

@dataclass
class ModelPet(Model):
    tags: List[Tag] = field(default_factory=create_tags)
    id: int = field(default_factory=Randomize().random_long_integer)
    category: Category = field(default_factory=get_random_pet_category)
    name: str = field(default_factory=Randomize().random_first_name)
    photoUrls: List[str] = field(default_factory=Randomize().random_urls)
    status: str = field(default_factory=get_availability_status)


if __name__ == '__main__':
    p = ModelPet()
    print(p)

    pprint(ModelPet.json_schema())

'''
 {
  "id": 0,
  "category": {
    "id": 0,
    "name": "string"
  },
  "name": "doggie",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 0,
      "name": "string"
    }
  ],
  "status": "available"
}
'''
