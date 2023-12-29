class Solution:
    def isPalindrome(self, string: str) -> bool:
        new_string = ""
        for s in range(len(string) - 1, -1, -1):
            new_string += string[s]
        return new_string == string

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
        return ""
