"""
This module contains the models for creating the Persons
"""

from utilities.randomizer import Randomize
from dataclasses import dataclass, field
from typing import List


@dataclass
class ModelUser:
    id: int = field(default_factory=Randomize().random_long_integer)
    username: str = field(default_factory=Randomize().random_first_name)
    firstname: str = username
    lastname: str = field(default_factory=Randomize().random_last_name)

    email: str = field(default_factory=Randomize().random_email_id)

    password:str = field(default_factory=Randomize().random_password)

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
    # pp = ModelPersonList([p1, p2])
    # print(pp)
    #
    # print(asdict(pp)['persons'])


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
