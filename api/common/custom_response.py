class CustomResponse:
    """
    Кастомный ответ на запросы клиента.
    """

    status: int = 200
    result: bool = False
    addition: dict = dict()
    description: dict = dict()

    def __init__(self, response, exception=None):
        self.status = response.status_code
        self.result = True if response.status_code < 399 else False
        self.addition = response.data if response.status_code < 399 else {}
        self.description = {}
        if exception:
            self.description = {'errors': {'message': exception.detail, 'code': exception.default_code}}
        elif response.status_code > 399:
            self.description = {'errors': response.data}

    def to_dict(self):
        return self.__dict__
