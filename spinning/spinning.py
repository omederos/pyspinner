import random
import re
import itertools

char_separator = '|'
char_closing = '}'
char_opening = '{'


def override_params(opening_char='{', closing_char='}', separator_char='|'):
    """
    Override some character settings

    @type opening_char: str
    @param opening_char: Opening character. Default: '{'
    @type closing_char: str
    @param closing_char: Closing character. Default: '}'
    @type separator_char: str
    @param separator_char: Separator char. Default: '|'
    """
    global char_separator, char_opening, char_closing
    char_separator = separator_char
    char_opening = opening_char
    char_closing = closing_char


def unique(text):
    """
    Return an unique text

    @type text: str
    @param text: Text written used spin syntax.
    @return: An unique text

    # Generate an unique sentence
    >>> unique('The {quick|fast} {brown|gray|red} fox jumped over the lazy dog.')
    'The quick red fox jumped over the lazy dog'


    """

    # check if the text is correct
    correct, error = _is_correct(text)
    if not correct:
        raise Exception(error)

    s = []
    _all_unique_texts(text, s)
    return s[0]


def _choices(text, randomized=True):
    """
    Return all the possible choices from the following format: {a|b|c}

    @type text: str
    @param text: Text written used spin syntax

    @type randomized: bool
    @param text: Specifies if the choices will be given in random order or not.

    @return: A generator that yields all the possible choices
    """
    if text:
        # regex pattern that will be used for splitting
        pattern = r'{0}|{1}|{2}'.format(
            re.escape(char_opening),
            re.escape(char_closing),
            re.escape(char_separator)
        )

        choices = [x for x in re.split(pattern, text) if x]
        if randomized:
            random.shuffle(choices)
        for x in choices:
            yield x


def _all_unique_texts(text, final):
    """
    Compute all the possible unique texts

    @type text: str
    @param text: Text written used spin syntax

    @type final: list
    @param final: An empty list where all the unique texts will be stored
    @return: Nothing. The result will be in the 'final' list
    """
    if not char_opening in text:
        if not text in final:
            final.append(text)
        return

    stack = []
    indexes = []
    for i, c in enumerate(text):
        if c == char_closing:
            if stack[-1] == char_opening:
                start_index = indexes.pop()
                substring = '' if i == start_index + 1 else text[start_index:i + 1]
                # get some random combination
                combination = next(_choices(substring))
                new_text = text.replace(substring, combination)
                _all_unique_texts(new_text, final)
                return
        elif c == char_opening:
            stack.append(c)
            indexes.append(i)


def _is_correct(text):
    """
    Check if the specified text has a correct spin syntax

    @type text: str
    @param text: Text written used spin syntax

    @rtype: tuple
    @return: A tuple: (is_correct, error). First position contains the result, and second one the error if not correct.
    """
    error = ''
    stack = []
    for i, c in enumerate(text):
        if c == char_opening:
            stack.append(c)
        elif c == char_closing:
            if stack.count == 0:
                error = 'Syntax incorrect. Found "}" before "{"'
                break
            last_char = stack.pop()
            if last_char != char_opening:
                error = 'Syntax incorrect. Found "}" before "{"'
                break
    if len(stack) > 0:
        error = 'Syntax incorrect. Some "{" were not closed'
    return not error, error
