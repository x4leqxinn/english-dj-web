from django.utils import translation

class LanguageMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        language_code = request.session.get('django_language')
        if language_code:
            translation.activate(language_code)
            request.LANGUAGE_CODE = translation.get_language()

        response = self.get_response(request)

        return response