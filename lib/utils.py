import random
import time
from .config import WORD_MAX_LENGTH, DEFINITION_MAX_LENGTH, SEE_ALSO_MAX_LENGTH, AVATAR_LIST, SUBTITLE_LIST


def hold_on(base, maxdelta):

    ourdelay = base + random.random() * maxdelta
    time.sleep(ourdelay)


def generate_random_string(length, charset):

    return ''.join(random.choice(charset) for i in range(length))


def is_word(text):

    return len(text) <= WORD_MAX_LENGTH


def is_word_class(text):

    return text in ['noun', 'verb', 'adjective', 'whoknows']


def is_definition(text):

    return len(text) <= DEFINITION_MAX_LENGTH


def is_see_also(text):

    return len(text) <= SEE_ALSO_MAX_LENGTH


def is_avatar(text):

    return text in AVATAR_LIST


def validate_inputs(form_word, form_word_class, form_definition, form_see_also, form_avatar):

    status = True

    if not is_word(form_word):
        print('failed word validation - value is', form_word)
        status = False

    if not is_word_class(form_word_class):
        print('failed word class validation - value is', form_word_class)
        status = False

    if not is_definition(form_definition):
        print('failed definition validation - value is', form_definition)
        status = False

    if not is_see_also(form_see_also):
        print('failed see_also validation - value is', form_see_also)
        status = False

    if not is_avatar(form_avatar):
        print('failed avatar validation - value is', form_avatar)
        status = False

    return status


def get_random_subtitle():

    subtitles = SUBTITLE_LIST

    index = random.randint(0, len(subtitles) - 1)

    return subtitles[index]
