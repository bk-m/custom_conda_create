# -*- coding: utf-8 -*-

"""
Click functions for the module.
"""

import click

def click_prompt_yes_no(question, default):
    """
    Click prompt to ask the user a yes/no question.

    http://click.pocoo.org/4/api/#click.prompt

    :param str question: Question to ask the user.
    :param default: Default value which will be returned if the user doesn't input anything.
    :returns: Returns True/False depending on user selection.
    """
    return _resolve_yes_no(click.prompt(question, default=default, type=click.BOOL))

def _resolve_yes_no(value):
    """
    Fix for default values other than True or False for click_prompt_yes_no().

    :param value: Return value of click.prompt(..., ..., type=click.BOOL)
    :returns: Returns True/False.
    """
    return True if value in [True, 'True', 1, '1', 'yes', 'y'] else False

def click_prompt_custom_var(var_name, default):
    """
    Click prompt to ask the user for the value of a given variable.

    http://click.pocoo.org/4/api/#click.prompt

    :param str var_name: Variable that gets assigned by the user.
    :param default: Default value which will be returned if the user doesn't input anything.
    :returns: The given value or the default.
    """
    return click.prompt(var_name, default=default)
