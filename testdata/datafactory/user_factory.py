"""
This module contains the models for creating the Persons
"""

from utilities.randomizer import Randomize
from dataclasses import dataclass, field
from typing import List
from testdata.datafactory import Model

from pprint import pprint


@dataclass
class ModelUser(Model):
    id: int = field(default_factory=Randomize().random_long_integer)
    username: str = field(default_factory=Randomize().random_first_name)
    firstName: str = field(default_factory=Randomize().random_first_name)
    lastName: str = field(default_factory=Randomize().random_last_name)
    email: str = field(default_factory=Randomize().random_email_id)
    password: str = field(default_factory=Randomize().random_password)
    phone: str = field(default_factory=Randomize().random_phone_number_without_country_code)
    userStatus: int = field(default_factory=Randomize().random_integer_from_length)


@dataclass
class ModelUserList:
    users: List[ModelUser]


if __name__ == '__main__':
    p1 = ModelUser()
    p2 = ModelUser()
    print(p1)
    print(p2)
    pprint(ModelUser.json_schema())

'''
 [
  {
    "id": 0,
    "username": "string",
    "firstName": "string",
    "lastName": "string",
    "email": "string",
    "password": "string",
    "phone": "string",
    "userStatus": 0
  }
]
'''
