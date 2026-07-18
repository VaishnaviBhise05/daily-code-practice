def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


if __name__ == "__main__":
    print(is_palindrome("madam"))    # True
    print(is_palindrome("hello"))    # False
    print(is_palindrome("Racecar"))  # True
