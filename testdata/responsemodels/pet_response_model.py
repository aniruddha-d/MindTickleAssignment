from . import Response


class PetNotFoundResponse(Response):

    def __init__(self, code=1, type='error', message='Pet not found'):
        self.code = code
        self.type = type
        self.message = message

