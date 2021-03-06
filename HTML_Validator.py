#!/bin/python3


def validate_html(html):
    '''
    This function performs a limited version of html validation by checking
    whether every opening tag has a corresponding closing tag.

    >>> validate_html('<strong>example</strong>')
    True
    >>> validate_html('<strong>example')
    False
    '''

    # HINT:
    # use the _extract_tags function below to generate a list of
    # html tags without any extra text;
    # then process these html tags using the balanced parentheses algorithm
    # from the class/book
    # the main difference between your code and the code from class will be
    # that you will have to keep track of not just the 3 types of parentheses,
    # but arbitrary text located between the html tags

    stack = []
    tags = _extract_tags(html)

    for tag in tags:
        end_tag = False
        for i, symbol in enumerate(tag):
            if symbol == '/':
                end_tag = True

        if end_tag:
            if len(stack) == 0:
                return False
            opening_tag = stack.pop()
            if opening_tag[1:-1] != tag[2:-1]:
                return False
        else:
            stack.append(tag)

    if len(stack) == 0:
        return True
    else:
        return False


def _extract_tags(html):
    '''
    This is a helper function for `validate_html`.
    By convention in Python, helper functions that are not meant to be used
    directly by the user are prefixed with an underscore.

    This function returns a list of all the html tags contained in the input
    string,
    stripping out all text not contained within angle brackets.

    >>> _extract_tags('Python <strong>rocks</strong>!')
    ['<strong>', '</strong>']
    '''

    tags = []
    tag = None
    inside = False

    for i in range(len(html)):
        if html[i] == '<':
            tag = ''
            inside = True

        if inside:
            if html[i] != ' ':
                tag += html[i]

        if inside:
            if html[i] == '>':
                tags.append(tag)
                inside = False

    if inside:
        tags.append("error")

    return tags
