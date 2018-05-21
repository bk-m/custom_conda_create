# -*- coding: utf-8 -*-

"""
Click functions for the module.
"""

import click

def read_user_yes_no(question, default_value):
    """
    Prompt the user to reply with 'yes' or 'no' (or equivalent values).

    Note:
      Possible choices are 'true', '1', 'yes', 'y' or 'false', '0', 'no', 'n'

    http://click.pocoo.org/4/api/#click.prompt

    :param question: Question to the user
    :param default_value: Value that will be returned if no input happens
    """
    return click.prompt(question, default=default_value, type=click.BOOL)

def resolve_yes_no(value):
    """
    """
    ret_val = False
    if value in [True, 'True', 1, '1', 'yes', 'y']:
        ret_val = True
    return ret_val
