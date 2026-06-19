import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        no_spaces = s.lower()

        if len(no_spaces) < 2:
            return True
        front = 0
        back = len(no_spaces) - 1
        print(no_spaces)
        while front < back:
            print(no_spaces[front])
            print(no_spaces[back])
            if no_spaces[front] == no_spaces[back]:
                front += 1
                back -= 1
            else:
                return False
        return True