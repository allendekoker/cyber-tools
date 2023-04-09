import re

# define password strength rules
rules = {
    'length': 8,  # minimum password length
    'lower': True,  # password must contain at least one lowercase character
    'upper': True,  # password must contain at least one uppercase character
    'digit': True,  # password must contain at least one digit
    'special': True  # password must contain at least one special character
}

def password_strength(password):
    score = 0
    message = ''

    # check password length
    if len(password) >= rules['length']:
        score += 1
    else:
        message += 'Password must be at least {} characters long. '.format(rules['length'])

    # check for lowercase characters
    if rules['lower'] and re.search('[a-z]', password):
        score += 1
    else:
        message += 'Password must contain at least one lowercase letter. '

    # check for uppercase characters
    if rules['upper'] and re.search('[A-Z]', password):
        score += 1
    else:
        message += 'Password must contain at least one uppercase letter. '

    # check for digits
    if rules['digit'] and re.search('[0-9]', password):
        score += 1
    else:
        message += 'Password must contain at least one digit. '

    # check for special characters
    if rules['special'] and re.search('[^a-zA-Z0-9]', password):
        score += 1
    else:
        message += 'Password must contain at least one special character. '

    # return score and message
    if score == len(rules):
        return 'Password is strong.'
    else:
        return 'Password is weak. ' + message
