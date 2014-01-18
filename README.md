pyspinner
=========

[![PyPI version](https://badge.fury.io/py/pyspinner.png)](http://badge.fury.io/py/pyspinner)

pyspinner is simple library for parsing text that uses spin-syntax.

### Installation

To install pyspinner, simply:

    $ pip install pyspinner

or download the source code and do:

    $ python setup.py install

### How to use it

    >>> import spinning
    >>> spinning.unique('The {quick|fast} {brown|gray|red} fox jumped over the lazy dog.')      
    'The quick gray fox jumped over the lazy dog.'

### Running tests

    $ python spinning-tests.py
    ....
    ----------------------------------------------------------------------
    Ran 2 tests in 0.000s
    
    OK

### Features
- Supports nested syntax.
- Supports custom opening, closing and separator characters by using the `override_params` function.

### TO-DO

- Allow optional phrases: `The quick{ red|} fox...`
- Allow special characters `{,|,}` inside text by escaping them.
- Write more tests
