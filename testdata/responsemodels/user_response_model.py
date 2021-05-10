from . import Response


class SuccessResponse(Response):

    def __init__(self, code=200, type='unknown', message='ok'):
        self.code = code
        self.type = type
        self.message = message


class InternalServerErrorResponse(Response):

    def __init__(self, code=500, type='unknown', message='something bad happened'):
        self.code = code
        self.type = type
        self.message = message
