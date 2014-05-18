import random
import re
import itertools

SEPARATOR_CHAR = '|'
CLOSING_CHAR = '}'
OPENING_CHAR = '{'


def override_params(opening_char='{', closing_char='}', separator_char='|'):
    global SEPARATOR_CHAR, OPENING_CHAR, CLOSING_CHAR

    SEPARATOR_CHAR = separator_char
    OPENING_CHAR = opening_char
    CLOSING_CHAR = closing_char


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
            re.escape(OPENING_CHAR),
            re.escape(CLOSING_CHAR),
            re.escape(SEPARATOR_CHAR)
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
    if not OPENING_CHAR in text:
        if not text in final:
            final.append(text)
        return

    stack = []
    indexes = []
    for i, c in enumerate(text):
        if c == CLOSING_CHAR:
            if stack[-1] == OPENING_CHAR:
                start_index = indexes.pop()
                substring = '' if i == start_index + 1 else text[start_index:i+1]
                # get some random combination
                combination = next(_choices(substring))
                new_text = text.replace(substring, combination)
                _all_unique_texts(new_text, final)
                return
        elif c == OPENING_CHAR:
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
        if c == OPENING_CHAR:
            stack.append(c)
        elif c == CLOSING_CHAR:
            if stack.count == 0:
                error = 'Syntax incorrect. Found "}" before "{"'
                break
            last_char = stack.pop()
            if last_char != OPENING_CHAR:
                error = 'Syntax incorrect. Found "}" before "{"'
                break
    if len(stack) > 0:
        error = 'Syntax incorrect. Some "{" were not closed'
    return not error, error