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
        self.description = exception.detail if exception is not None else {}

    def to_dict(self):
        return self.__dict__
