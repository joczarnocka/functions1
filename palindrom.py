def is_palindrom(word):
    """
        Function detects whether a given word is palindrome,
        which means that reading it from the beginning
        and from the end return the same value
        Arguments:
        word
    """
    return word[::-1] == word


print(is_palindrom("kajak"))
print(is_palindrom("123456789o987654321"))
print(is_palindrom("niekajak"))
