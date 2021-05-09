"""
This module contains the models for creating the Persons
"""

from utilities.randomizer import Randomize
from dataclasses import dataclass, field
from typing import List
from testdata.datafactory import Model

from pprint import pprint


@dataclass
class UserModel(Model):
    id: int = field(default_factory=Randomize().random_long_integer)
    username: str = field(default_factory=Randomize().random_username)
    firstName: str = field(default_factory=Randomize().random_first_name)
    lastName: str = field(default_factory=Randomize().random_last_name)
    email: str = field(default_factory=Randomize().random_email_id)
    password: str = field(default_factory=Randomize().random_password)
    phone: str = field(default_factory=Randomize().random_phone_number_without_country_code)
    userStatus: int = field(default_factory=Randomize().random_integer_from_length)


@dataclass
class ModelUserList:
    users: List[UserModel]


if __name__ == '__main__':
    p1 = UserModel()
    p2 = UserModel()
    print(p1)
    print(p2)
    pprint(UserModel.json_schema())

    p1.firstName = 102
    print(p1.firstName)
    # from dataclasses import asdict
    # print(asdict(p1))
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
