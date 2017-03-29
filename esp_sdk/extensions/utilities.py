def singularize(name):
    """
    This is a total hack that will only work with ESP resources. Don't use
    this for anything else.
    """
    n = str(name)
    if n[-1:] == 's':
        return n[:-1]
    return n


def underscore_to_titlecase(value):
    return ''.join(x.capitalize() for x in value.split("_"))
