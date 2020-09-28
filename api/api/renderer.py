from django.http import HttpResponseNotFound
from rest_framework import renderers
from common.custom_response import CustomResponse
from rest_framework.views import exception_handler


def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    if response is not None:
        response.data = {'errors': exc.get_full_details()}

    return response


class CustomRenderer(renderers.JSONRenderer):
    """
    Рендерер ответов на запросы клиента.
    """

    media_type = 'application/json'
    format = 'json'
    charset = 'utf-8'

    def render(self, data, accepted_media_type=None, renderer_context=None):

        response = renderer_context.get('response')
        if response is None:
            return HttpResponseNotFound()

        custom_response = CustomResponse(response).to_dict()

        return super().render(
            custom_response,
            accepted_media_type=accepted_media_type,
            renderer_context=renderer_context
        )
