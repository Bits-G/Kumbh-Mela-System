from .translations import TRANSLATIONS


def language_context(request):
    lang = request.session.get('language', 'en')  # default English
    return {
        't': TRANSLATIONS.get(lang, TRANSLATIONS['en']),
        'current_language': lang,
    }