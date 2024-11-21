from  modeltranslation.translator import translator, TranslationOptions
from .models import AboutModel

class NewsTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

translator.register(AboutModel, NewsTranslationOptions)