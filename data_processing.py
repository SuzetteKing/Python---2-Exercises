def return_post_codes(text):
    """
    Write a function that takes an arbitrary text and returns a list of
    post-codes that appear in that text. Postcodes, in the UK, are of one of
    the following form where `X` means a letter appears and `9` means a number
    appears:

    X9 9XX
    X9X 9XX
    X99 9XX
    XX9 9XX
    XX9X 9XX
    XX99 9XX

    Note that even though the standard layout is to include one single space
    in between the two halves of the post code, there are occasional formating
    errors where an arbitrary number of space is included (0, 1, or more). You
    should parse those codes as well.

    :param text: a raw, arbitrary text
    :return: list of post-codes
    :rtype: list
    """

import re
    
#regex = '[A-Z]([A-Z](\d{1,2}|\d[A-Z])|\d{1,2})\s\d[A-Z]{2}'
regex = '[A-Z]{1,2}[0,9][A-Z0-9]? [0-9][ABD-HJLNP-UW-Z]{2}'
text = """Postcodes, in the UK, are of one of
    the following form where `X` means a letter appears and `9` means a number
    appears:

    X9 9XX
    X9X 9XX
    X99 9XX
    XX9 9XX
    XX9X 9XX
    XX99 9XX

    Note that even though the standard layout is to include one single space
    in between the two halves of the post code"""
    
result = re.findall(regex,text)
print(result)
    


