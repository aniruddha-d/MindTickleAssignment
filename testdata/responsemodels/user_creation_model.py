from testdata.datafactory import Model
from dataclasses import dataclass


@dataclass
class UserCreation(Model):
    code: int
    type: str
    message: str


class SuccessResponse(UserCreation):

    def __init__(self, code=200, type='unknown', message='ok'):
        self.code = code
        self.type = type
        self.message = message


class InternalServerErrorResponse(UserCreation):

    def __init__(self, code=500, type='unknown', message='something bad happened'):
        self.code = code
        self.type = type
        self.message = message
