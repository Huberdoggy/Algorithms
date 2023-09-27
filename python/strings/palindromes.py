import re


class Word:
    def __init__(self) -> None:
        self._user_word = input("Enter a word => ")
        # Anything shorter wouldn't really make sense to eval
        self._regex = re.compile(r"[a-zA-Z]{3,}")
        self._is_pal = self._checkPalindrome(self._user_word, self._regex, self._Iterate)

    def _Iterate(self, str_word: str):
        start, end = 0, len(str_word) - 1
        while start < end:
            if str_word[start].lower() != str_word[end].lower():
                return False
            start += 1
            end -= 1
        return True

    def _checkPalindrome(self, str_word: str, reg, my_func):
        if not str_word:
            print("Null string entered")
            return False
        elif not re.fullmatch(reg, str_word):
            print(
                "\nYou must enter a SINGLE word of at least 3 characters\nOnly letters are accepted"
            )
            return False
        else:
            return my_func(str_word)  # Pass the bool back caller, stored in class attrib


x = Word()
print(
    f"The word you entered: '{x._user_word}' is identical in reverse"
) if x._is_pal else ""
