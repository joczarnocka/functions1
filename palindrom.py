def is_palindrom(word):
    """
        Returns answer whether a word is palindrome,
        which means that reading it from the beginning
        and from the end return the same value
    """
    return word[::-1] == word


print(is_palindrom("kajak"))
print(is_palindrom("123456789o987654321"))
print(is_palindrom("niekajak"))
