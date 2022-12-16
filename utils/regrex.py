import re


def validate_name(name):
    """ Returns true if the name matches the regrex pattern or else it returns false"""
    if re.match('[A-Za-z]{2,25}( [A-Za-z]{2,25})?', name):
        return True
    else:
        return False


def validate_phone_number(contact_number):
    """ Returns true if the contact number matches the regrex pattern or else it returns false"""
    if re.fullmatch('^(?:(?:\+|0{0,2})91(\s*[\-]\s*)?|[0]?)?[789]\d{9}$', contact_number):
        return True
    else:
        return False
