from django.http import HttpResponseNotFound
from rest_framework import renderers

from common.custom_response import CustomResponse


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
