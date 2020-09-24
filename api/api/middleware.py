from rest_framework.exceptions import NotFound
from django.http import JsonResponse, HttpResponseNotFound
from common.custom_response import CustomResponse


class CustomMiddleware:
    """
    Промежуточный слой для отлова исключений, и вывода ошибок.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        try:
            response = self.process_response(request, response)
        except NotFound as e:
            return self.process_exception(request, e)
        return response

    def process_response(self, request, response):
        if isinstance(response, HttpResponseNotFound):
            raise NotFound(detail='Not Found', code=404)

        return response

    def process_exception(self, request, exception):
        response = self.get_response(request)

        # Костыль для работы вывода ошибок в HTML.
        if 'text/html' in request.headers.get('accept') or '*/*' in request.headers.get('accept'):
            return response

        custom_response = CustomResponse(response, exception).to_dict()

        return JsonResponse(custom_response, status=response.status_code)
