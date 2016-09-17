"""
_parsing.py module for version_utils
"""

# Standard library imports
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
import logging

# Third party imports

# Local imports


LOG = logging.getLogger(__name__)


def pop_letters(char_list):
    """Pop consecutive letters from the front of a list and return them

    Pops any and all consecutive letters from the start of the provided
    character list and returns them as a list of characters. Operates
    on (and possibly alters) the passed list

    :param list char_list: a list of characters
    :return: a list of characters
    :rtype: list
    """
    LOG.debug('_pop_letters(%s)', char_list)
    letters = []
    while len(char_list) != 0 and char_list[0].isalpha():
        letters.append(char_list.pop(0))
    LOG.debug('got letters: %s', letters)
    LOG.debug('updated char list: %s', char_list)
    return letters

