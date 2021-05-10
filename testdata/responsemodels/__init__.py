from testdata.datafactory import Model
from dataclasses import dataclass


@dataclass
class Response(Model):
    code: int
    type: str
    message: str

