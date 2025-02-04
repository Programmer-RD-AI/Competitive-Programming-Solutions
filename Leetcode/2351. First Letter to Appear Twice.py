class Solution:
    def repeatedCharacter(self, s: str) -> str:
        appeared = []
        for letter in s:
            if letter in appeared:
                return letter
            appeared.append(letter)
