"""A module to translate from english to french and vice versa"""
from deep_translator import MyMemoryTranslator

frTranslator = MyMemoryTranslator(source='english', target='french')
enTranslator = MyMemoryTranslator('french', 'english')

def english_to_french(text):
    """Method to translate from english to french"""
    return frTranslator.translate(text)

def french_to_english(text):
    """Method to translate from french to english"""
    return enTranslator.translate(text)

