UPPERCASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
LOWERCASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
OTHER_LETTERS = 'áéíóúüàãâäèẽêëìĩîïòõôöùũûñÁÉÍÓÚÜÀÃÂÄÈẼÊËÌĨÎÏÒÕÔÖÙŨÛÑ'
NUMBERS = '0123456789'

LETTERS = UPPERCASE_LETTERS + LOWERCASE_LETTERS + OTHER_LETTERS
WHITELIST_TMP = LOWERCASE_LETTERS + NUMBERS
WHITELIST_CONTENT = LETTERS + NUMBERS

ID_STRING_LENGTH = 12

PYTHON_CMD = '/usr/bin/python3'
RENDER_CMD = '/home/deployment/definitive/definitive.py'
RENDER_OPT_WORD_CLASS = '-c noun'

ERROR_WORD = 'error'
ERROR_WORD_CLASS = 'bummer'
ERROR_DEFINITION = 'action often performed by naughty kids messing up with the inputs.'
ERROR_DEFINITION_CHAT_GPT = 'ChatGPT is not in the mood.'
ERROR_SEE_ALSO = 'oops'
ERROR_AVATAR = 'troll'

DEFAULT_WORD = 'Entropitis'
DEFAULT_DEFINITION = 'A condition defined by the uncontrollable urge to introduce superfluous complexity in systems or processes.'
DEFAULT_SEE_ALSO = 'autokafka'

WORD_MAX_LENGTH = 20
DEFINITION_MAX_LENGTH = 160
SEE_ALSO_MAX_LENGTH = 20

IMG_TEXT_COLOR = "#042c49"
IMG_BORDER_COLOR = IMG_TEXT_COLOR
IMG_TOP_MARGIN = "35"

BASE_DELAY = 0.2
MAX_DELAY_DELTA = 0.2

AVATAR_LIST = ['none', 'grug', 'normand', 'troll', 'lasers', 'lulz', 'randall', 'homer', 'minister']

SUBTITLE_LIST = [ "Home of the fake",
                  "The Ministry of Silly Words",
                  "The missing slide on your presentation",
                  "\"I write my own dictionary\"",
                  "A reliable source of nonsense",
                  "A tsunami of name value pairs",
                  "Little more than this information",
                  "An infinite stream of misunderstandings",
                  "The Niagara falls of controversial semantics",
                  "The authoritative nounserver",
                  "A weapon of mass distraction",
                  "The one stop chop for language matters",
                  "The place were great words RIP",
                  "Meme generator for true intelectuals",
                  "Fast food for thought"
                  ]
